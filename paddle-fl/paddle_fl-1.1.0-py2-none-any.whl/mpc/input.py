# Copyright (c) 2020 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
This module provides embedding operation for paddle_mpc.
"""

from __future__ import print_function
import six
import numpy as np
from paddle import fluid
from paddle.fluid.data_feeder import check_variable_and_dtype, check_dtype

import warnings
from .framework import MpcVariable
from .mpc_layer_helper import MpcLayerHelper
from .data_utils import aby3

__all__ = ['embedding']

def embedding(input,
              size,
              is_sparse=False,
              is_distributed=False,
              padding_idx=None,
              param_attr=None,
              dtype='int64'):
    """
    The operator is used to lookup embeddings vector of ids provided by :attr:`input` . 
    It automatically constructs a 2D embedding matrix based on the
    input :attr:`size` (vocab_size, emb_size) and :attr:`dtype` .
    The `input` is the mpc one-hot tensor of indexes, it last dimensions is equal to `emb_size`,
    its shape size must be 3, i.e., (2, x, emb_size)

    The shape of output Tensor is generated by replacing an emb_size dimension to the
    last dimension of the input Tensor shape.

    **Note:** The id in :attr:`input` must satisfy :math:`0 =< id < size[0]` , 
    otherwise the program will throw an exception and exit.
    ** Params of `is_sparse`, `is_distributed`, `padding_idx` have not been implemented.

    .. code-block:: text

        Case 1:

        input is a Tensor.
            input.data = aby3.make_share([[1, 0, 0], [0, 1, 0]])
            input.shape = [2, 2, 3]
            w.data = aby3.make_share([[1, 2], [2, 3], [3, 4]])
        Given size = [2, 3, 2]
        output is a Tensor:
            out.shape = [2, 2, 2]
            out.data.reconstruct = [[1, 2], [2, 3]]

    Args:
        input(MpcVariable): A Tensor or LoDTensor with type int64, which contains the id information.
            The value of the input id should satisfy :math:`0<= id < size[0]` .
        size(tuple|list): The shape of lookup table parameter. It should have two elements which
            indicates the size of the dictionary of embeddings and the size of each embedding vector respectively.
        is_sparse(bool, not implemented): The flag indicating whether to use sparse update. This parameter only
            affects the performance of the backwards gradient update. It is recommended to set 
            True because sparse update is faster. But some optimizer does not support sparse update,
            such as :ref:`api_fluid_optimizer_AdadeltaOptimizer` , :ref:`api_fluid_optimizer_AdamaxOptimizer` , 
            :ref:`api_fluid_optimizer_DecayedAdagradOptimizer` , :ref:`api_fluid_optimizer_FtrlOptimizer` ,
            :ref:`api_fluid_optimizer_LambOptimizer` and :ref:`api_fluid_optimizer_LarsMomentumOptimizer` .
            In these case, is_sparse must be False. Default: False.
        is_distributed(bool, not implemented): Whether to store the embedding matrix in a distributed manner. Only used
            in multi-machine distributed CPU training. Default: False.
        padding_idx(int|long|None, not implemented): padding_idx needs to be in the interval [-vocab_size, vocab_size). 
            If :math:`padding\_idx < 0`, the :math:`padding\_idx` will automatically be converted
            to :math:`vocab\_size + padding\_idx` . It will output all-zero padding data whenever lookup
            encounters :math:`padding\_idx` in id. And the padding data will not be updated while training.
            If set None, it makes no effect to output. Default: None.
        param_attr(ParamAttr): To specify the weight parameter property. Default: None, which means the
            default weight parameter property is used. See usage for details in :ref:`api_fluid_ParamAttr` . In addition,
            user-defined or pre-trained word vectors can be loaded with the :attr:`param_attr` parameter. 
            The local word vector needs to be transformed into numpy format, and the shape of local word
            vector shoud be consistent with :attr:`size` . Then :ref:`api_fluid_initializer_NumpyArrayInitializer`
            is used to load custom or pre-trained word vectors.
        dtype(str|core.VarDesc.VarType.INT64): It refers to the data type of output Tensor.
            It must be int64.

    Returns:
        Variable: Embedding Tensor or LoDTensor mapped by input. The data type is the same as :attr:`dtype` .

    Examples:
        .. code-block:: python

          import paddle.fluid as fluid
          import paddle_fl.mpc as pfl
          import numpy as np
          # data should be mpc one hot tensor
          data = pfl.data(name='x', shape=[4, 3], dtype='int64')

          # exampel 1
          emb_1 = fluid.embedding(input=data, size=[3, 4])

          # example 2: load custom or pre-trained word vectors
          weight_data = np.random.random(size=(2, 3, 4))  # mpc word vectors with numpy format
          w_param_attrs = fluid.ParamAttr(
              name="emb_weight",
              learning_rate=0.5,
              initializer=fluid.initializer.NumpyArrayInitializer(weight_data),
              trainable=True)
          emb_2 = fluid.embedding(input=data, size=(3, 4), param_attr=w_param_attrs, dtype='int64')
    """

    if is_sparse:
      warnings.warn("the process on sparse data is the same with dense data,"
                   " that is, 'is_sparse' always set as 'False' in paddle_encrypted.")
    if is_distributed:
      warnings.warn("distributed deployment of paddle_encrypted has not been implemented."
                   " that is, 'is_distributed' always set as 'False' in paddle_encrypted.")
    if padding_idx:
      warnings.warn("padding_idx is not supported in paddle_encrypted."
                   " that is, 'padding_idx' always set as 'None' in paddle_encrypted.")
    helper = MpcLayerHelper('embedding', **locals())
    check_variable_and_dtype(input, 'input', ['int64'], 'paddle_encrypted.embedding')
    check_dtype(dtype, 'dtype', ['int64'],
                 'paddle_encrypted.embedding')

    w = helper.create_mpc_parameter(
        attr=helper.param_attr, shape=size, dtype='int64', is_bias=False)

    tmp = helper.create_mpc_variable_for_type_inference(dtype)
    helper.append_op(
        type='mpc_lookup_table_v2',
        inputs={'Ids': input,
                'W': w},
        outputs={'Out': tmp},
        attrs={
            'is_sparse': False,
            'is_distributed': False,
            'remote_prefetch': False,
            'padding_idx': None
        })
    return tmp
