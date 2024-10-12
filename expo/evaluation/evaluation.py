import numpy as np
from sklearn.metrics import accuracy_score, f1_score, mean_squared_error, roc_auc_score


def evaluate_score(pred, gt, metric):
    if metric == "accuracy":
        return accuracy_score(gt, pred)
    elif metric == "f1":
        unique_classes = sorted(list(np.unique(gt)))
        if 1 in unique_classes and 0 in unique_classes:
            pos_label = 1
        else:
            pos_label = unique_classes[0] if len(unique_classes) == 2 else None
        return f1_score(gt, pred, pos_label=pos_label)
    elif metric == "f1 weighted":
        return f1_score(gt, pred, average="weighted")
    elif metric == "roc_auc":
        return roc_auc_score(gt, pred)
    elif metric == "rmse":
        return mean_squared_error(gt, pred, squared=False)
    elif metric == "log rmse":
        return mean_squared_error(np.log1p(gt), np.log1p(pred), squared=False)
    else:
        raise ValueError(f"Metric {metric} not supported")


def node_evaluate_score_sela(node):
    preds = node.get_and_move_predictions("test")["target"]
    gt = node.get_gt("test")["target"]
    metric = node.state["dataset_config"]["metric"]
    return evaluate_score(preds, gt, metric)


def node_evaluate_score_mlebench(node):
    # TODO
    return 0
