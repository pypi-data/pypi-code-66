import sys
import math
import os
import numpy as np
import scipy
import scipy.stats
from scipy.stats import zscore
from scipy.spatial.distance import euclidean,squareform,pdist
sys.setrecursionlimit(10000)
import smfishHmrf.reader as reader
from smfishHmrf.HMRFInstance import HMRFInstance
from smfishHmrf.DatasetMatrix import DatasetMatrix, DatasetMatrixSingleField

if __name__=="__main__":
	cortex_FDs = [100]
	directory = "hmrfem.whole.brain.e.fd0-48.correlated.gene"
	roi = "whole.brain.e"
	FDs = cortex_FDs
	workdir = "/home/qz64/hmrf.submit"
	genes = reader.read_genes("%s/%s/genes" % (workdir, directory))
	Xcen, field = reader.read_coord("%s/%s/f%s.coordinates.txt" % (workdir, directory, roi)) #note the stitched version use the .2 version

	expr = np.empty((len(genes), Xcen.shape[0]), dtype="float32")
	for ind,g in enumerate(genes):
		expr[ind,:] = reader.read_expression("%s/%s/pca_corrected/f%s.gene.%s.txt" % (workdir, directory, roi, g))

	good_i = np.array([i for i in range(Xcen.shape[0]) if field[i] in set(cortex_FDs)])
	expr = expr[:,good_i]
	Xcen = Xcen[good_i]
	field = field[good_i]

	ngene = len(genes)
	ncell = Xcen.shape[0]

	expr = zscore(expr, axis=1)	 #z-score per row (gene)
	expr = zscore(expr, axis=0)  #z-score per column (cell)

	this_dset = DatasetMatrixSingleField(expr, genes, None, Xcen)
	this_dset.test_adjacency_list([0.3, 0.5, 1], metric="euclidean")
	this_dset.calc_neighbor_graph(0.3, metric="euclidean")
	this_dset.calc_independent_region()

	new_genes = reader.read_genes("../HMRF.genes")
	new_dset = this_dset.subset_genes(new_genes)
	
	'''	
	print "Running HMRF..."
	outdir = "../spatial.jul20"
	if not os.path.isdir(outdir):
		os.mkdir(outdir)
	this_hmrf = HMRFInstance("cortex", outdir, new_dset, 9, 0, 1.0, 23, tolerance=1e-60)
	this_hmrf.init(nstart=1000)
	this_hmrf.run()
	
	
	print "Running pertubed HMRF..."
	outdir = "../perturbed.jul20"
	if not os.path.isdir(outdir):
		os.mkdir(outdir)
	perturbed_dset = new_dset.shuffle(0.99)
	perturbed_hmrf = HMRFInstance("cortex", outdir, perturbed_dset, 9, 0, 1.0, 23, tolerance=1e-20)
	perturbed_hmrf.init(nstart=1000)
	perturbed_hmrf.run()
	'''

	
	this_hmrf = HMRFInstance.ReadFrom("cortex", "../spatial.jul20", new_dset, 9, (0, 1.0, 23))

	perturb_expr = reader.read_expression_matrix("%s/f%s.expression.txt" % ("../perturbed.jul20", "cortex"))
	perturb_dset = DatasetMatrixSingleField(perturb_expr, genes, None, Xcen)

	perturb_hmrf = HMRFInstance.ReadFrom("cortex", "../perturbed.jul20", perturb_dset, 9, (0, 1.0, 23))
	
	for b in range(0, 15):
		print this_hmrf.likelihood[(9, b)], perturb_hmrf.likelihood[(9, b)]
