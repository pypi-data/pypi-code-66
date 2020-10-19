import networkx as nx
import pandas as pd
from collections import defaultdict
from itertools import combinations
from tqdm import tqdm
from joblib import parallel_backend, Parallel, delayed
from scipy.special import comb
import os
import pickle


def intersect_1(genes):
    if len(set.intersection(*[disease_genes[gene] for gene in genes])) > 20:
        return genes


def intersect_2(genes):
    if len(set.intersection(*[intersection_1[gene] for gene in genes])) > 10:
        return set(genes)


if __name__ == '__main__':
    os.chdir("/home/bio/groupshare/vinay/clep_benchmarking/adni/query_pats")

    edgelist_df = pd.read_table('weighted.edgelist')

    edgelist_df.columns = ['source', 'target', 'relation', 'label']
    edgelist_df = edgelist_df[['source', 'relation', 'target', 'label']]

    edgelist_df.drop(columns='label', inplace=True)

    design = pd.read_table('adni_targets.txt', index_col=0)
    pat_map = {design.at[row, 'FileName']: design.at[row, 'Target'] for row in design.index}

    network = nx.from_pandas_edgelist(
        df=edgelist_df,
        source='source',
        target='target',
        edge_attr='relation',
        create_using=nx.DiGraph
    )

    result = {}

    for patient in pat_map.keys():
        x = nx.single_source_shortest_path(
            G=network,
            source=patient,
            cutoff=1
        )

        x.pop(patient, None)

        result[patient] = x

    dps = [key for key, val in pat_map.items() if val == 'Disease']
    nps = [key for key, val in pat_map.items() if val == 'Control']
    genes_of_interest = ['APOE', 'APP', 'PSEN1', 'PSEN2', 'CLU']

    all_genes = defaultdict(set)
    disease_genes = defaultdict(set)
    normal_genes = defaultdict(set)

    for patient in pat_map.keys():
        for gene in result[patient].keys():
            all_genes[gene].add(patient)
            if patient in dps:
                disease_genes[gene].add(patient)
            elif patient in nps:
                normal_genes[gene].add(patient)

    all_counts = {gene: len(all_genes[gene]) for gene in all_genes.keys()}
    disease_counts = {gene: len(disease_genes[gene]) for gene in disease_genes.keys()}
    normal_counts = {gene: len(normal_genes[gene]) for gene in normal_genes.keys()}

    x = [gene for gene in disease_counts.keys() if (disease_counts[gene] / 484) - (normal_counts[gene] / 260) > 0.05]

    with parallel_backend("threading", n_jobs=4):
        final = Parallel()(delayed(intersect_1)(genes) for genes in tqdm(combinations(x, 3), total=comb(len(x), 3)))

    res = [item for item in final if item]

    intersection_1 = defaultdict(set)
    for combo in res:
        intersection_1[combo] = set.intersection(*[disease_genes[gene] for gene in combo])

    x = list(intersection_1.keys())

    with parallel_backend("threading", n_jobs=4):
        final = Parallel()(delayed(intersect_2)(genes) for genes in tqdm(combinations(x, 2), total=comb(len(x), 2)))

    res = [item for item in final if item]

    intersection_2 = defaultdict(set)
    for combo in res:
        intersection_2[combo] = set.intersection(*[intersection_1[gene] for gene in combo])

    with open('intersection_1.pkl', 'w') as a, open('intersection_2.pkl', 'w') as b:
        pickle.dump(intersection_1, a)
        pickle.dump(intersection_2, b)
