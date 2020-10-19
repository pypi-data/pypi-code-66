from typing import Callable

import tensorflow as tf
from tensorflow.python.keras.losses import LossFunctionWrapper, binary_crossentropy
from tensorflow.python.keras.utils import losses_utils


def my_loss_fn(y_true, y_pred):
    squared_difference = tf.square(y_true - y_pred)
    return tf.reduce_mean(squared_difference, axis=-1)  # Note the `axis=-1`


class BinaryBoundaryCrossentropy(LossFunctionWrapper):
    def __init__(
        self,
        from_logits=False,
        label_smoothing=0,
        reduction=losses_utils.ReductionV2.AUTO,
        name="binary_boundary_crossentropy",
    ):
        super(BinaryBoundaryCrossentropy, self).__init__(
            binary_boundary_crossentropy,
            name=name,
            reduction=reduction,
            from_logits=from_logits,
            label_smoothing=label_smoothing,
        )
        self.from_logits = from_logits


def binary_boundary_crossentropy(
    y_true,
    y_pred,
    from_logits=False,
    label_smoothing=0,
    range: int = 0,
    max: float = 2.0,
):
    """
    [summary]

    Parameters
    ----------
    y_true : [type]
        [description]
    y_pred : [type]
        [description]
    from_logits : bool, optional
        [description], by default False
    label_smoothing : int, optional
        [description], by default 0
    range : int, optional
        [description], by default 0
    max : float, optional
        [description], by default 1.0

    Returns
    -------
    [type]
        [description]

    Examples
    --------
    >>> from image_keras.custom.losses_binary_boundary_crossentropy import binary_boundary_crossentropy
    >>> import cv2
    >>> a = cv2.imread("a.png", cv2.IMREAD_GRAYSCALE)
    >>> a_modified = (a / 255).reshape(1, a.shape[0], a.shape[1], 1)
    >>> binary_boundary_crossentropy(a_modified, a_modified, range=1, max=2)
    """
    bce = binary_crossentropy(
        y_true=y_true,
        y_pred=y_pred,
        from_logits=from_logits,
        label_smoothing=label_smoothing,
    )

    def count_around_blocks(arr, range: int = 1):
        ones = tf.fill(tf.constant(arr).shape, 1)
        size = range * 2 + 1
        if range < 1:
            size = 1
        extracted = tf.image.extract_patches(
            images=ones,
            sizes=[1, size, size, 1],
            strides=[1, 1, 1, 1],
            rates=[1, 1, 1, 1],
            padding="SAME",
        )
        result = tf.reduce_sum(extracted, axis=-1)
        if range > 0:
            result -= 1
        return result

    def count_around_blocks2(arr, range: int = 1):
        size = range * 2 + 1
        if range < 1:
            size = 1
        extracted = tf.image.extract_patches(
            images=arr,
            sizes=[1, size, size, 1],
            strides=[1, 1, 1, 1],
            rates=[1, 1, 1, 1],
            padding="SAME",
        )
        e_base = extracted[:, :, :, extracted.shape[-1] // 2]
        e_base = tf.reshape(e_base, (-1, arr.shape[1], arr.shape[2], 1))
        e_base_expanded = tf.reshape(
            tf.repeat(e_base, extracted.shape[-1]),
            (-1, arr.shape[1], arr.shape[2], extracted.shape[-1]),
        )
        same_values = tf.math.equal(extracted, e_base_expanded)
        result_1 = tf.reshape(
            extracted.shape[-1] - tf.math.count_nonzero(same_values, axis=-1),
            (-1, arr.shape[1], arr.shape[2], 1),
        )
        result_1 = tf.cast(result_1, tf.int32)
        block_counts = tf.reshape(
            count_around_blocks(arr, range), (-1, arr.shape[1], arr.shape[2], 1)
        )
        modify_result_1 = -(size ** 2 - block_counts)
        modify_result_1 = modify_result_1 * arr
        modify_result_1 = tf.cast(modify_result_1, tf.int32)
        diff_block_count = result_1 + modify_result_1
        return diff_block_count

    around_block_count = count_around_blocks(y_true, range=range)
    around_block_count = tf.reshape(
        around_block_count, (-1, y_true.shape[1], y_true.shape[2], 1)
    )
    around_block_count = tf.cast(around_block_count, tf.float64)

    diff_block_count = count_around_blocks2(y_true, range=range)
    diff_block_count = tf.reshape(
        diff_block_count, (-1, y_true.shape[1], y_true.shape[2], 1)
    )
    diff_block_count = tf.cast(diff_block_count, tf.float64)

    diff_ratio = diff_block_count / around_block_count
    diff_ratio = 1.0 + tf.cast(tf.math.maximum(max - 1.0, 0), tf.float64) * diff_ratio

    return bce * diff_ratio


# def categorical_boundary_crossentropy(
#     y_true,
#     y_pred,
#     from_logits: bool = False,
#     label_smoothing: float = 0,
#     range: int = 0,
#     min: float = 1.0,
#     max: float = 1.0,
#     gradient: Callable[[float], float] = lambda el: el,
# ):
#     """
#     [summary]

#     Parameters
#     ----------
#     y_true : [type]
#         [description]
#     y_pred : [type]
#         [description]
#     range : int, optional
#         [description], by default 0
#     min : float, optional
#         [description], by default 1.0
#     max : float, optional
#         [description], by default 1.0
#     gradient : Callable[[float], float], optional
#         [description], by default lambdael:el

#     Examples
#     --------
#     >>> y_true = [[1, 1, 0], [0, 0, 1]]
#     >>> y_pred = [[0.05, 0.95, 0], [0.1, 0.8, 0.1]]
#     """
#     cce = categorical_crossentropy(
#         y_true=y_true,
#         y_pred=y_pred,
#         from_logits=from_logits,
#         label_smoothing=label_smoothing,
#     )

#     print("a")


# # ---------------

# import tensorflow as tf

# n = 5
# images = [[[[x * n + y + 1] for y in range(n)] for x in range(n)]]
# images_tf = tf.constant(images)


# def count_around_blocks(arr, range: int = 1):
#     ones = tf.fill(tf.constant(arr).shape, 1)
#     size = range * 2 + 1
#     if range < 1:
#         size = 1
#     extracted = tf.image.extract_patches(
#         images=ones,
#         sizes=[1, size, size, 1],
#         strides=[1, 1, 1, 1],
#         rates=[1, 1, 1, 1],
#         padding="SAME",
#     )
#     result = tf.reduce_sum(extracted, axis=-1)
#     if range > 0:
#         result -= 1
#     return result


# def count_around_blocks2(arr, range: int = 1):
#     size = range * 2 + 1
#     if range < 1:
#         size = 1
#     extracted = tf.image.extract_patches(
#         images=arr,
#         sizes=[1, size, size, 1],
#         strides=[1, 1, 1, 1],
#         rates=[1, 1, 1, 1],
#         padding="SAME",
#     )
#     e_base = extracted[:, :, :, extracted.shape[-1] // 2]
#     e_base = tf.reshape(e_base, (-1, arr.shape[1], arr.shape[2], 1))
#     e_base_expanded = tf.reshape(
#         tf.repeat(e_base, extracted.shape[-1]),
#         (-1, arr.shape[1], arr.shape[2], extracted.shape[-1]),
#     )
#     same_values = tf.math.equal(extracted, e_base_expanded)
#     result_1 = tf.reshape(
#         extracted.shape[-1] - tf.math.count_nonzero(same_values, axis=-1),
#         (-1, arr.shape[1], arr.shape[2], 1),
#     )
#     result_1 = tf.cast(result_1, tf.int32)
#     block_counts = tf.reshape(
#         count_around_blocks(arr, range), (-1, arr.shape[1], arr.shape[2], 1)
#     )
#     modify_result_1 = -(size ** 2 - block_counts)
#     modify_result_1 = modify_result_1 * arr
#     modify_result_1 = tf.cast(modify_result_1, tf.int32)
#     diff_block_count = result_1 + modify_result_1
#     return diff_block_count


# import cv2

# a = cv2.imread("a.png", cv2.IMREAD_GRAYSCALE)
# a_modified = (a / 255).reshape(1, a.shape[0], a.shape[1], 1)

# ss = 1

# # around block count
# around_block_count = count_around_blocks(a_modified, range=ss)
# around_block_count = tf.reshape(around_block_count, (1, a.shape[0], a.shape[1], 1))
# around_block_count = tf.cast(around_block_count, tf.float64)

# # diff block count
# diff_block_count = count_around_blocks2(a_modified, range=ss)
# diff_block_count = tf.reshape(diff_block_count, (1, a.shape[0], a.shape[1], 1))
# diff_block_count = tf.cast(diff_block_count, tf.float64)

# # ratio
# diff_block_count / around_block_count

# ---------------

# def categorical_crossentropy(y_true,
#                              y_pred,
#                              from_logits=False,
#                              label_smoothing=0):
#   """Computes the categorical crossentropy loss.

#   Standalone usage:

#   >>> y_true = [[0, 1, 0], [0, 0, 1]]
#   >>> y_pred = [[0.05, 0.95, 0], [0.1, 0.8, 0.1]]
#   >>> loss = tf.keras.losses.categorical_crossentropy(y_true, y_pred)
#   >>> assert loss.shape == (2,)
#   >>> loss.numpy()
#   array([0.0513, 2.303], dtype=float32)

#   Args:
#     y_true: Tensor of one-hot true targets.
#     y_pred: Tensor of predicted targets.
#     from_logits: Whether `y_pred` is expected to be a logits tensor. By default,
#       we assume that `y_pred` encodes a probability distribution.
#     label_smoothing: Float in [0, 1]. If > `0` then smooth the labels.

#   Returns:
#     Categorical crossentropy loss value.
#   """
#   y_pred = ops.convert_to_tensor_v2(y_pred)
#   y_true = math_ops.cast(y_true, y_pred.dtype)
#   label_smoothing = ops.convert_to_tensor_v2(label_smoothing, dtype=K.floatx())

#   def _smooth_labels():
#     num_classes = math_ops.cast(array_ops.shape(y_true)[-1], y_pred.dtype)
#     return y_true * (1.0 - label_smoothing) + (label_smoothing / num_classes)

#   y_true = smart_cond.smart_cond(label_smoothing,
#                                  _smooth_labels, lambda: y_true)
#   return K.categorical_crossentropy(y_true, y_pred, from_logits=from_logits)
