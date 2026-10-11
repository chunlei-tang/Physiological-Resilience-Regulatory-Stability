"""Reference template for exploratory nine-pattern classification.

NOT the original study code. Does not reproduce reported results.

Usage:
  python regulatory_pattern_model_template.py --csv path/to/approved_deidentified_data.csv --target regulatory_pattern --id participant_id

Required: pandas, numpy, scikit-learn. Optional: xgboost, lightgbm.
Do not upload individual-level clinical data to a public repository.
"""
import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, balanced_accuracy_score, classification_report, roc_auc_score
from sklearn.model_selection import GroupShuffleSplit, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler, label_binarize


def model_candidates():
    models = {
        "random_forest": RandomForestClassifier(n_estimators=200, random_state=42, class_weight="balanced"),
        "logistic_regression": LogisticRegression(max_iter=2000, class_weight="balanced"),
        "knn": KNeighborsClassifier(n_neighbors=5),
    }
    try:
        from xgboost import XGBClassifier
        models["xgboost"] = XGBClassifier(n_estimators=200, max_depth=4, learning_rate=0.05, random_state=42, eval_metric="mlogloss")
    except ImportError:
        print("Skipping XGBoost: install xgboost to enable it.")
    try:
        from lightgbm import LGBMClassifier
        models["lightgbm"] = LGBMClassifier(n_estimators=200, learning_rate=0.05, random_state=42, verbose=-1)
    except ImportError:
        print("Skipping LightGBM: install lightgbm to enable it.")
    return models


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", required=True, help="Approved, de-identified analytical CSV")
    parser.add_argument("--target", default="regulatory_pattern")
    parser.add_argument("--id", default=None, help="Pseudonymous participant ID for group-based split")
    parser.add_argument("--features", nargs="+", default=None, help="Explicit approved feature column names")
    parser.add_argument("--out", default="model_template_metrics.json")
    args = parser.parse_args()

    data = pd.read_csv(args.csv)
    if args.target not in data:
        raise ValueError(f"Missing target column: {args.target}")
    if args.id and args.id not in data:
        raise ValueError(f"Missing participant ID column: {args.id}")
    if not args.id:
        raise ValueError("Provide --id with a pseudonymous participant ID to prevent subject-level leakage.")
    if not args.features:
        raise ValueError("Provide --features explicitly; automatic selection may leak outcomes or identifiers.")
    forbidden = {args.target, args.id, "death_status", "event_death", "name", "姓名"}
    if forbidden.intersection(args.features):
        raise ValueError("Feature list includes target, identifier, or outcome information.")
    missing = set(args.features) - set(data.columns)
    if missing:
        raise ValueError(f"Missing feature columns: {sorted(missing)}")

    data = data.dropna(subset=[args.target, args.id]).copy()
    X = data[args.features]
    y_raw = data[args.target]
    labels = sorted(y_raw.unique().tolist(), key=str)
    if len(labels) < 2:
        raise ValueError("At least two target classes are required.")
    label_to_index = {label: idx for idx, label in enumerate(labels)}
    y = y_raw.map(label_to_index).to_numpy()
    groups = data[args.id].to_numpy()
    splitter = GroupShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
    train_idx, test_idx = next(splitter.split(X, y, groups=groups))
    X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
    y_train, y_test = y[train_idx], y[test_idx]
    if len(np.unique(y_train)) != len(labels):
        raise ValueError("Training split lacks one or more classes; revise splitting strategy.")

    numeric = X.select_dtypes(include=np.number).columns.tolist()
    categorical = [c for c in X.columns if c not in numeric]
    prep = ColumnTransformer([
        ("numeric", Pipeline([("imputer", SimpleImputer(strategy="median")), ("scale", StandardScaler())]), numeric),
        ("categorical", Pipeline([("imputer", SimpleImputer(strategy="most_frequent")), ("onehot", OneHotEncoder(handle_unknown="ignore"))]), categorical),
    ])
    results = {"disclaimer": "Exploratory template results only; not a reproduction of original manuscript findings.",
               "n_train_records": len(train_idx), "n_test_records": len(test_idx),
               "n_train_participants": len(set(groups[train_idx])), "n_test_participants": len(set(groups[test_idx])),
               "classes": [str(x) for x in labels], "models": {}}

    for name, estimator in model_candidates().items():
        pipeline = Pipeline([("preprocess", prep), ("model", estimator)])
        try:
            pipeline.fit(X_train, y_train)
            pred = pipeline.predict(X_test)
            metrics = {"accuracy": float(accuracy_score(y_test, pred)),
                       "balanced_accuracy": float(balanced_accuracy_score(y_test, pred)),
                       "classification_report": classification_report(y_test, pred, labels=list(range(len(labels))), zero_division=0, output_dict=True)}
            if hasattr(pipeline, "predict_proba"):
                proba = pipeline.predict_proba(X_test)
                try:
                    if len(labels) == 2:
                        metrics["roc_auc"] = float(roc_auc_score(y_test, proba[:, 1]))
                    else:
                        metrics["roc_auc_ovr_macro"] = float(roc_auc_score(y_test, proba, labels=list(range(len(labels))), multi_class="ovr", average="macro"))
                except ValueError as err:
                    metrics["auc_note"] = f"Not estimable on this split: {err}"
            results["models"][name] = metrics
            print(f"{name}: accuracy={metrics['accuracy']:.3f}; balanced_accuracy={metrics['balanced_accuracy']:.3f}")
        except Exception as err:
            results["models"][name] = {"error": str(err)}
            print(f"{name}: could not fit/evaluate: {err}")

    Path(args.out).write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Saved exploratory metrics to {args.out}")


if __name__ == "__main__":
    main()
