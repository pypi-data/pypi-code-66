# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from ._utils import _is_uuid
from azureml.exceptions._azureml_exception import UserErrorException
from ._module_dto import ModuleDto


def get_refined_module_dto_identifiers(module_dto: ModuleDto, workspace_name):
    identifiers = [module_dto.module_name, (module_dto.module_name, module_dto.namespace),
                   (module_dto.module_name, module_dto.namespace, module_dto.module_version)]
    _, identifiers = _refine_batch_load_input([], identifiers, workspace_name)
    return identifiers


def _refine_batch_load_input(ids, identifiers, workspace_name):
    """
    Refine batch load input.

    1.replace None value with empty list
    2.standardized tuple length to 3

    :param ids: module_version_ids
    :type ids: List[str]
    :param identifiers: (name,namespace,version) list
    :type identifiers: List[tuple]
    :param workspace_name: default namespace to fill
    :type workspace_name: str
    :return: input after refined
    :rtype: List[str], List[tuple]
    """
    _ids = [] if ids is None else ids
    _identifiers = []

    badly_formed_id = [_id for _id in _ids if not _is_uuid(_id)]
    if len(badly_formed_id) > 0:
        raise UserErrorException('Badly formed module_version_id found, '
                                 'expected hexadecimal guid, error list {0}'.format(badly_formed_id))

    if identifiers is not None:
        for item in identifiers:
            if isinstance(item, tuple):
                if len(item) > 3:
                    raise UserErrorException('Ambiguous identifier tuple found, '
                                             'expected tuple length <= 3, actually {}'.format(item))
                while len(item) < 3:
                    item += (None,)
                _identifiers.append(item)
            else:
                _identifiers.append((item, workspace_name, None))
    return _ids, _identifiers


def _refine_batch_load_output(module_dtos, ids, identifiers, workspace_name):
    """
    Copy result for duplicate module_version_id.

    Refine result order.

    :param module_dtos: origin result list
    :type List[azure.ml.component._restclients.designer.models.ModuleDto]
    :param ids: module_version_ids
    :type List[str]
    :param identifiers: (name,namespace,version) list
    :type List[tuple]
    :return: refined output and filed module version ids and identifiers
    :rtype: List[azure.ml.component._restclients.designer.models.ModuleDto], List[str], List[tuple]
    """
    id_set = set(ids)
    id_dto_dict = {module_dto.module_version_id: module_dto
                   for module_dto in module_dtos
                   if module_dto.module_version_id in id_set}
    idf_dto_dict = {_idf: _dto for _dto in module_dtos
                    for _idf in get_refined_module_dto_identifiers(_dto, workspace_name)}

    failed_ids = []
    failed_identifiers = []
    refined_output = []
    for _id in ids:
        if _id in id_dto_dict.keys():
            refined_output.append(id_dto_dict[_id])
        else:
            failed_ids.append(_id)

    for _idf in identifiers:
        if _idf in idf_dto_dict.keys():
            refined_output.append(idf_dto_dict[_idf])
        else:
            failed_identifiers.append(_idf)
    return refined_output, failed_ids, failed_identifiers
