"""
Tools for padding
"""

import itertools
import json
import collections
import random
from typing import List, Tuple, Dict
import torch
import copy

from torch.utils.data import Dataset, DataLoader, Sampler
# from data.utils import CustomTokenizer
from functools import partial


def pad_tensor(vec: torch.Tensor, pad: int, dim: int) -> torch.Tensor:
    """
    args:
        vec - tensor to pad
        pad - the size to pad to
        dim - dimension to pad

    return:
        a new tensor padded to 'pad' in dimension 'dim'
    """
    if pad - vec.size(
            dim) == 0:  # reach max no need to pad (This is used to avoid pytorch0.4.1's bug)
        return vec
    pad_size = list(vec.shape)
    pad_size[dim] = pad - vec.size(dim)
    ret = torch.cat([vec, torch.zeros(*pad_size, dtype=vec.dtype)], dim=dim)
    return ret


class PadCollate:
    """
    a variant of callate_fn that pads according to the longest sequence in a batch of sequences.
    Notice:
        - Use 0 as pad value.
        - Support 2 pad position at same time with optional args.
        - Batch format slight different from "TensorDataset"
        (where batch is (Tensor1, Tensor2, ..., Tensor_n), and shape of Tensor_i is (batch_size, item_i_size),
        Here, batch format is List[List[torch.Tensor]], it's shape is (batch_size, item_num, item_size).
        This is better for padding at running, and write get_item() for dataset.
    """

    def __init__(self, dim: int = 0, sp_dim: int = None, sp_item_idx: List[int] = None):
        """
        args:
            dim - the dimension to be padded

            sp_dim - the dimension to be padded for some special item
            in batch(this leaves some flexibility for pad dim)

            sp_item_idx - the index for some special item
                          in batch(this leaves some flexibility for pad dim)
        """
        self.dim = dim
        self.sp_dim = sp_dim
        self.sp_item_idx = sp_item_idx

    def pad_collate(self, batch: List[List[torch.Tensor]]) -> List[torch.Tensor]:
        """
        args:
            batch - list of (tensor1, tensor2, ..., tensor3)

        reutrn:
            ret - tensors of all examples in 'batch' after padding,
            each tensor belongs to one items type.
        """
        ret = []
        for item_idx in range(len(batch[0])):  # pad each data item
            # find longest sequence
            max_len = max(map(lambda x: x[item_idx].shape[self.get_dim(item_idx)], batch))
            # if item_idx in self.sp_item_idx:
            #     print('debug padding:', "item_idx", item_idx, "max_len",
            #           max_len,'batch items', [x[item_idx].shape for x in batch])
            # pad according to max_len
            padded_item_lst = list(map(
                    lambda x: pad_tensor(x[item_idx], pad=max_len, dim=self.get_dim(item_idx)),
                    batch))
            # stack all
            padded_item_lst = torch.stack(padded_item_lst, dim=0)
            ret.append(padded_item_lst)
        return ret

    def get_dim(self, item_idx):
        """ this dirty function is design for bert non-word-piece index.
        This will be removed by move index construction to BertContextEmbedder
        """
        if self.sp_dim and self.sp_item_idx and item_idx in self.sp_item_idx:
            return self.sp_dim  # pad to the special dimension
        else:
            return self.dim  # pad to the dimension

    def __call__(self, batch):
        return self.pad_collate(batch)


class SimilarLengthSampler(Sampler):
    r"""
    Samples elements and ensure
        1. each batch element has similar length to reduce padding.
        2. each batch is in decent length order (useful to pack_sequence for RNN)
        3. batches are ordered randomly
    If without replacement, then sample from a shuffled dataset.
    If with replacement, then user can specify ``num_samples`` to draw.

    Arguments:
        data_source (Dataset): dataset to sample from
        batch_size (int): num of samples in one batch
    """

    def __init__(self, data_source, batch_size):
        super(SimilarLengthSampler, self).__init__(data_source=data_source)
        self.data_source = data_source
        self.batch_size = batch_size

        all_idxs = list(range(len(data_source)))
        all_lens = [self.get_length(idx) for idx in all_idxs]
        self.all_index = self.sort_and_batching(all_idxs, all_lens, batch_size)

    def sort_and_batching(self, all_idxs, all_lens, batch_size):
        sorted_idxs = sorted(zip(all_idxs, all_lens), key=lambda x: x[1], reverse=True)
        sorted_idxs = [item[0] for item in sorted_idxs]
        batches = self.chunk(sorted_idxs, batch_size)  # shape: (batch_num, batch_size)
        random.shuffle(batches)  # shuffle batches
        flatten_batches = itertools.chain.from_iterable(batches)
        return flatten_batches

    def chunk(self, lst, n):
        return [lst[i: i + n] for i in range(0, len(lst), n)]

    def get_length(self, idx):
        return len(self.data_source[idx][0])  # we use the test length in sorting

    def __iter__(self):
        # if not deep copy, iteration will stop after first step
        return iter(copy.deepcopy(self.all_index))
        # return iter(range(len(self.data_source)))

    def __len__(self):
        return len(self.data_source)


def padding_dataloader(dataset: Dataset,
                       batch_size: int = 1,
                       num_wokers: int = 4) -> DataLoader:
    """
    Wrapping padding dataset.

    :param dataset: Sequence Dataset, which must contain sequence.
    :param batch_size: Batch_size for dataloader
    :param num_wokers:
    :return: dataloader with batch size
    """
    sampler = SimilarLengthSampler(data_source=dataset, batch_size=batch_size)
    collate_fn = PadCollate()
    dataloader = DataLoader(dataset=dataset, shuffle=False, num_workers=num_wokers,
                            batch_size=batch_size,
                            sampler=sampler, collate_fn=collate_fn)
    return dataloader
