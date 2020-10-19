import torch
from seqeval.metrics import f1_score, precision_score, recall_score, accuracy_score


def hit_at_k(predictions: torch.Tensor, ground_truth_idx: torch.Tensor,
             largest: bool = True,
             device: torch.device = torch.device('cpu'),
             k: int = 10) -> int:
    """Calculates number of hits@k.
    :param predictions: BxN tensor of prediction values where B is batch size
        and N number of classes. Predictions must be sorted in class ids order
    :param ground_truth_idx: Bx1 tensor with index of ground truth class
    :param device: device on which calculations are taking place
    :param k: number of top K results to be considered as hits
    :param largest: largest is the right if set True.
    :return: Hits@K score
    """
    assert predictions.size(0) == ground_truth_idx.size(0)

    zero_tensor = torch.tensor([0], device=device)
    one_tensor = torch.tensor([1], device=device)
    _, indices = predictions.topk(k=k, largest=largest)
    o = torch.where(indices == ground_truth_idx, one_tensor, zero_tensor)
    return o.sum().item()


def mrr(predictions: torch.Tensor, ground_truth_idx: torch.Tensor,
        descending: bool = True) -> float:
    """Calculates mean reciprocal rank (MRR) for given predictions and ground truth values.
    :param predictions: BxN tensor of prediction values where B is batch size and N number of classes. Predictions
    must be sorted in class ids order
    :param ground_truth_idx: Bx1 tensor with index of ground truth class
    :param descending: From large to small
    :return: Mean reciprocal rank score
    """
    assert predictions.size(0) == ground_truth_idx.size(0)

    indices = predictions.argsort(descending=descending)
    return (1.0 / (indices == ground_truth_idx).nonzero()[:, 1].float().add(1.0)).sum().item()


def _ner_metrics(golden_label: list, prediction: list) -> dict:
    """
    Convient metrics for NER tasks

    :param golden_label: the true label sequence, 2d with [N, length]
    :param prediction: prediction output by your model
    :return: dict type; including F1, Precision, Recall, Acc
    """
    result = dict()
    result['F1'] = f1_score(y_pred=prediction, y_true=golden_label)
    result['Precision'] = precision_score(y_true=golden_label, y_pred=prediction)
    result['Recall'] = recall_score(y_pred=prediction, y_true=golden_label)
    result['Acc'] = accuracy_score(y_pred=prediction, y_true=golden_label)
    return result


def ner_metrics(golden_labels: torch.Tensor,
                predictions: torch.Tensor,
                debug: bool = False):
    """
    NER metrics

    :param golden_labels: Tensor
    :param predictions: Tensor
    :param debug: Bool, if true debug informations.
    :return:
    """
    assert golden_labels.dim() == predictions.dim(), \
        f"golden_labels dimensions should be same as predictions, but got predictions dim " \
        f"{predictions.dim()} and golden_labels dim {golden_labels.dim()}"
    assert golden_labels.dim() == 2, f"This metrics is for 2-d data shape like [N, seq_length]"
    golden_list = golden_labels.cpu().tolist()
    preds = predictions.cpu().tolist()
    return _ner_metrics(golden_list, preds)
