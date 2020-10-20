from functools import partial

import tensorflow as tf
from tensorflow.python.keras.losses import LossFunctionWrapper
import tensorflow.keras.backend as K



def soft_fscore(activation_function, y_true, y_pred, from_logits=False, label_smoothing=0):
    if from_logits:
        y_pred = activation_function(y_pred)
    tp = K.sum(y_true * y_pred, axis=0)
    fp = K.sum((1 - y_true) * y_pred, axis=0)
    tn = K.sum((1 - y_true) * (1 - y_pred), axis=0)
    fn = K.sum(y_true * (1 - y_pred), axis=0)
    return (
        1
        - tp / (2 * tp + fn + fp + K.epsilon())
        - tn / (2 * tn + fn + fp + K.epsilon())
    )


class SoftFScoreLoss(LossFunctionWrapper):
    def __init__(self,
                 is_multilabel=False,
                 from_logits=False,
                 label_smoothing=0,
                 reduction=tf.keras.losses.Reduction.NONE,
                 name="soft-f-score"):
        func = K.softmax
        if is_multilabel:
            func = K.sigmoid
        super().__init__(
            partial(soft_fscore, func),
            name=name,
            reduction=reduction,
            from_logits=from_logits,
            label_smoothing=label_smoothing)
        self.from_logits = from_logits
