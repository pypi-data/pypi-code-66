# Recommender system for Penn AI.
import pandas as pd
# import json
# import urllib.request, urllib.parse
from .base import BaseRecommender
#from ..metalearning import get_metafeatures
from sklearn.preprocessing import RobustScaler
from sklearn.pipeline import Pipeline
import numpy as np
from collections import defaultdict, OrderedDict
from sklearn.neighbors import NearestNeighbors
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
formatter = logging.Formatter('%(module)s: %(levelname)s: %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

class KNNMetaRecommender(BaseRecommender):
    """Penn AI KNN meta recommender.
    Recommends machine learning algorithms and parameters as follows:
        - store the best ML + P on every dataset.
        - given a new dataset, measure its distance to all results in
        metafeature space.
        - recommend ML + P with best performance on closest dataset.

    Parameters
    ----------
    ml_type: str, 'classifier' or 'regressor'
        Recommending classifiers or regressors. Used to determine ML options.
    metric: str (default: accuracy for classifiers, mse for regressors)
        The metric by which to assess performance on the datasets.
    ml_p: DataFrame (default: None)
        Contains all valid ML parameter combos, with columns 'algorithm' and
        'parameters'
    """
    def __init__(self,
            ml_type='classifier',
            metric=None,
            ml_p=None,
            random_state=None,
            knowledgebase_results=None,
            knowledgebase_metafeatures=None,
            load_serialized_rec="if_exists",
            serialized_rec_directory=None,
            serialized_rec_filename=None):

        """ set default recommender specific parameters; might be overwritten by loading serialized recommender"""

        # lookup table: dataset name to best ML+P
        self.best_mlp = pd.DataFrame(columns=['_id','algorithm',
            'parameters', 'score'])
        self.best_mlp.set_index('_id',inplace=True)

        # local dataframe of datasets and their metafeatures
        self.all_dataset_mf = pd.DataFrame()


        """Initialize recommendation system."""
        super().__init__(
            ml_type,
            metric,
            ml_p,
            random_state=random_state,
            knowledgebase_results=knowledgebase_results,
            knowledgebase_metafeatures=knowledgebase_metafeatures,
            load_serialized_rec=load_serialized_rec,
            serialized_rec_directory=serialized_rec_directory,
            serialized_rec_filename=serialized_rec_filename)


    def update(self, results_data, results_mf, source='pennai'):
        """Update ML / Parameter recommendations.

        Parameters
        ----------
        results_data: DataFrame
                columns corresponding to:
                'algorithm'
                'parameters'
                self.metric

        results_mf: DataFrame
               columns corresponding to metafeatures of each dataset in
               results_data.
        """
        # update trained dataset models and hash table
        super().update(results_data, results_mf, source)

        # save a copy of the results_mf with NaNs filled with zero
        drop_cols = [c for c in results_mf.columns
                if c[0] == '_' and c !='_id']
        self.all_dataset_mf = \
        results_mf.drop(columns=drop_cols).fillna(0.0).set_index('_id')

        # update internal model
        self.update_model(results_data)

    def update_model(self,results_data):
        """Stores best ML-P on each dataset."""
        logger.debug('len(self.hash_2_param)): ' + str(len(self.hash_2_param)))
        for d,dfg in results_data.groupby('_id'):
            if (len(self.best_mlp) == 0 or
                d not in self.best_mlp.index or
                dfg[self.metric].max() > self.best_mlp.loc[d,'score']):
                self.best_mlp.loc[d,'score'] = dfg[self.metric].max()
                dfg = dfg.reset_index()
                idx = dfg[self.metric].idxmax()
                # print('dfg:\n',dfg)
                logger.debug('new best for '+d+': '+
                        dfg.loc[idx,'algorithm']+', idx:'+str(idx))
                self.best_mlp.loc[d,'algorithm'] = dfg.loc[idx,'algorithm']
                self.best_mlp.loc[d,'parameters'] = dfg.loc[idx,
                        'parameter_hash']
            else:
                logger.debug('skipping'+d)
        # print('model updated')

    def recommend(self, dataset_id, n_recs=1, dataset_mf = None):
        """Return a model and parameter values expected to do best on dataset.

        Parameters
        ----------
        dataset_id: string
            ID of the dataset for which the recommender is generating
            recommendations.
        n_recs: int (default: 1), optional
            Return a list of length n_recs in order of estimators and parameters
            expected to do best.
        """
        if dataset_mf is None:
            raise ValueError('dataset_mf is None for',dataset_id,
                    "can't recommend")

        # dataset hash table
        super().recommend(dataset_id, n_recs, dataset_mf)

        logger.debug('dataset_mf columns:{}'.format(dataset_mf.columns))
        drop_cols = [c for c in dataset_mf.columns
                if c[0] == '_' and c !='_id']
        dataset_mf = dataset_mf.drop(columns=drop_cols)
        logger.debug('dataset_mf columns:{}'.format(dataset_mf.columns))
        try:
            ml_rec, phash_rec, rec_score = self.best_model_prediction(
                    dataset_id, dataset_mf)
            if len(ml_rec) < n_recs:
                logger.info(f'len(ml_rec)={len(ml_rec)}, recommending random')
            iters = 0
            while len(ml_rec) < n_recs and iters < 1000:
                # add random ml_p recommendations until n_recs is met
                new_ml_rec = np.random.choice(self.ml_p['algorithm'].unique())
                new_phash_rec = self._hash_simple_dict(np.random.choice(
                        self.ml_p.loc[self.ml_p['algorithm']==new_ml_rec]
                                              ['parameters'].values))
                if (dataset_id + '|' + new_ml_rec + '|' + new_phash_rec
                        not in self.trained_dataset_models):
                    ml_rec.append(new_ml_rec)
                    phash_rec.append(new_phash_rec)
                    rec_score.append(np.nan)
                iters = iters+1
            if iters == 1000:
                logger.info(f'couldn''t find {n_recs} unique recommendations! '
                      'returning',len(ml_rec))
                subset = \
                    [dataset_id in tdm for tdm in self.trained_dataset_models]
                num_results = len(
                    [tdm for i,tdm in enumerate(self.trained_dataset_models)
                           if subset[i]])
                logger.info(f'btw, there are {num_results} results for '
                        '{dataset_id} already')
            ml_rec, p_rec, rec_score = (ml_rec[:n_recs],
                    [self.hash_2_param[p] for p in phash_rec[:n_recs]],
                                       rec_score[:n_recs])
            assert(len(ml_rec) == n_recs)

        except Exception as e:
            logger.error('error running self.best_model_prediction for'
                    +dataset_id)
            raise e
            # logger.error('ml_rec:'+ ml_rec)
            # logger.error('p_rec'+ p_rec)
            # logger.error('rec_score'+rec_score)

        # update the recommender's memory with the new algorithm-parameter
        # combos that it recommended
        self._update_trained_dataset_models_from_rec(
                                                    dataset_id,
                                                    ml_rec,
                                                    phash_rec
                                                    )

        return ml_rec, p_rec, rec_score

    def best_model_prediction(self, dataset_id, df_mf, n_recs=1):
        """Predict scores over many variations of ML+P and pick the best"""
        # get dataset metafeatures
        for cols in ['dataset','_id']:
            if cols in df_mf.columns:
                df_mf = df_mf.drop(cols,axis=1)
        mf = df_mf.fillna(0.0).values.flatten()
        # compute the neighbors of past results
        nbrs = NearestNeighbors(n_neighbors=len(self.all_dataset_mf),
                algorithm='ball_tree')
        rs = RobustScaler()

        X = rs.fit_transform(self.all_dataset_mf.values)
        nbrs.fit(X)
        # find n_recs nearest neighbors to new dataset
        # print('querying neighbors with mf of shape',mf.shape)
        distances,indices = nbrs.kneighbors(rs.transform(mf.reshape(1,-1)))
        # print('distances:',distances)
        # print('indices:',indices)
        dataset_idx = [self.all_dataset_mf.index[i] for i in indices[0]]
        # recommend the mlp results closest to the dataset in metafeature space
        ml_recs, p_recs, scores = [],[],[]

        # print('self.best_mlp:',self.best_mlp)
        for i,(d,dist) in enumerate(zip(dataset_idx,distances[0])):
            if d not in self.best_mlp.index:
                continue
            if i < 10:
                logger.debug('closest dataset:'+d+'; distance:'+ str(dist))
            # don't recommend based on the same dataset
            if round(dist,6) > 0.0:
                alg_params = (self.best_mlp.loc[d,'algorithm'] + '|' +
                              self.best_mlp.loc[d,'parameters'])
                # only recommend if not already recommended
                if (dataset_id+'|'+alg_params
                        not in self.trained_dataset_models):
                    ml_recs.append(self.best_mlp.loc[d,'algorithm'])
                    p_recs.append(self.best_mlp.loc[d,'parameters'])
                    scores.append(dist)

        return ml_recs,p_recs,scores
