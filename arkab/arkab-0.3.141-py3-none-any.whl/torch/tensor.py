"""Extended tools for tensor"""
import torch as th
from torch import Tensor

__all__ = ['count_zero', 'zero_index', 'mask']


def is_zero(t: Tensor):
    return not (t == 0).any()


def count_zero(t: Tensor):
    """
    Count zero item count.
    Args:
        t: source tensor

    Returns:
        count of zero in tensor t
    """
    return (t == 0).sum().item()


def zero_index(t: Tensor, as_index: bool):
    """
    Return zero indexes

    :param t: source tensor
    :param as_index: if true, the return result can be use as index of a tensor
    :return: all zero index of t
    """
    return (t == 0).nonzero(as_tuple=as_index)


def mask(src: Tensor, masked_signal: int = 0, return_bool: bool = False) -> Tensor:
    """

    :param src: mask tensor src and return
    :param masked_signal: signal for mask, default is 0
    :param return_bool: decide return bool or long type
    :return: masked tensor for src, return tensor has same shape with src
    """
    if return_bool:
        return (src != masked_signal).bool()
    return (src != masked_signal).long()
