# Imports --------------------------------------------------------------------------------------------------------------
import pickle
import pandas as pd
from pandas.api.types import is_sparse


# Constants ------------------------------------------------------------------------------------------------------------
NONSPARSE_COLUMNS = {"sample_id", "type"}


# Functions ------------------------------------------------------------------------------------------------------------
def to_sparse(dataframe, fill_value=False, nonsparse=NONSPARSE_COLUMNS):
    """
    Convert a dense CLICnet dataframe to sparse.
    """
    nonsparse = nonsparse & set(dataframe.columns)
    saved_columns = {}
    for column in nonsparse:
        saved_columns[column] = dataframe.loc[:, column].tolist()
    dataframe = dataframe.drop(columns=nonsparse)

    ret = dataframe.astype(pd.SparseDtype(bool, fill_value=fill_value))

    for column, value in saved_columns.items():
        ret.loc[:, column] = value
    return ret

def to_dense(dataframe, nonsparse=NONSPARSE_COLUMNS):
    """
    Convert a sparse CLICnet dataframe to dense.
    """
    nonsparse = nonsparse & set(dataframe.columns)
    saved_columns = {}
    for column in nonsparse:
        saved_columns[column] = dataframe.loc[:, column].tolist()
    dataframe = dataframe.drop(columns=nonsparse)
    if is_sparse(dataframe.iloc[:, 0]):
        ret = dataframe.sparse.to_dense()
    else:
        ret = dataframe
    for column, value in saved_columns.items():
        ret.loc[:, column] = value
    return ret

def load_presets(path):
    """
    Load preset genes from CLICnet manuscript.
    """
    with open(path, "rb") as handle:
        ret = pickle.load(handle)
    return ret


# Classes ------------------------------------------------------------------------------------------------------------
class CancerData:
    """
    Class representing cancer data, including clinical data and mutations.
    """
    def __init__(self, path, dtype):
        """
        Load pickled data.
        """
        with open(path, "rb") as handle:
            loaded = pickle.load(handle)

        self.mutation_table = loaded.mutation_table
        self.clinical_table = loaded.clinical_table
        self._type = dtype

        self.all_genes = set(self.mutation_table.keys())
        self.ctypes = set(self.clinical_table['type'])

        self._is_sparse = True
        self._to_dense()


    def _to_sparse(self):
        """
        Convert self to sparse.
        """
        assert not self._is_sparse

        self.mutation_table = to_sparse(self.mutation_table)
        self._is_sparse = True

    def _to_dense(self):
        """
        Convert self to dense.
        """
        assert self._is_sparse
        self.mutation_table = to_dense(self.mutation_table)
        self._is_sparse = False

    def save(self, path, version):
        """
        Save self to file.
        """
        self._to_sparse()
        with open(path, "wb") as handle:
            pickle.dump(self, handle, version)
        self._to_dense()

    def assert_cancer_in_data(self, cancer_name):
        return cancer_name in self.ctypes

    def assert_genes_in_data(self, genes):
        return len(self.all_genes & set(genes)) > 0

    def extract_cancer(self, cancer_name, genes):
        """
        Extract mutation and clinical data for a specific cancer type.
        """
        if cancer_name == "PANCANC":
            idxs = [j for j, i in enumerate(self.clinical_table['type'])]
        else:
            idxs = [j for j, i in enumerate(self.clinical_table['type']) if i == cancer_name]

        subset_mutations = self.mutation_table.iloc[idxs]
        cancer_gene_set = [i for i in genes if i in subset_mutations.keys()]
        mutations_ret = subset_mutations[cancer_gene_set].copy()

        if cancer_name == "PANCANC":
            clinical_ret = self.clinical_table.set_index('type', drop=False).copy()
        else:
            clinical_ret = self.clinical_table.set_index('type', drop=False).loc[cancer_name].copy()

        return mutations_ret, clinical_ret


class TCGA(CancerData):
    """Class representing TCGA data."""
    def __init__(self, path):
        super().__init__(path, "tcga")


class MSK(CancerData):
    """Class representing MSK data."""
    def __init__(self, path):
        super().__init__(path, "msk")


class MSKTMB(CancerData):
    """Class representing MSK TMB data."""
    def __init__(self, path):
        super().__init__(path, "msktmb")

class LIU(CancerData):
    """Class representing Liu et al data."""
    def __init__(self, path):
        super().__init__(path, "liu")

class RIAZ(CancerData):
    """Class representing Riaz et al data."""
    def __init__(self, path):
        super().__init__(path, "riaz")
