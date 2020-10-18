from DSAE_Impute.DSAE import Discriminative_SAE
import DSAE_Impute.DSAE.Pre_process as Pre_process
import DSAE_Impute.DSAE.To_full as To_full
import DSAE_Impute.DSAE.Dropout as Dropout
import pandas as pd
import numpy as np 
from sklearn.metrics import mean_absolute_error, mean_squared_error
from scipy.stats import pearsonr
from sklearn.metrics.pairwise import cosine_similarity
import os
path = __file__
path = path[:-7]
def main(inputs=os.path.join(path,'data/test.csv'), outputdir=os.path.join(path,'data'),
         dim1=600, dim2=256, epoch1=3000, epoch2=1000, lr=4e-3, batch=64, print_step=200):
    ########################    Read Data     ########################
    data_T = pd.read_csv(inputs, index_col=0)  ## 真实矩阵
    data_raw = Dropout.main(data_T, outputdir)

    adj = cosine_similarity(data_raw.values)
    print(adj) 

    ########################    Data Preprocessing    ######################
    data_raw_process, row, col, data_true_part = Pre_process.normalize(data_raw, data_T)  # 500x3000 → 500x1344

    ########################        Imputation         ###################### 
    model = Discriminative_SAE(dims = [dim1, dim2],  
                            activations = ['sigmoid', 'relu'],
                            epoch = [epoch1, epoch2], 
                            loss = 'rmse',
                            lr = lr,
                            noise = None,   
                            batch_size = batch, 
                            print_step = print_step,
                            Adj = adj)

    model.fit(data_raw_process, data_true_part)   
    predict = model.predict(data_raw_process)     

    impute_part = pd.DataFrame(predict, index=row, columns=col)
    impute = To_full.getAll(impute_part, data_raw)  ## (500, 1346) → (500, 3000) & 负值 → 绝对值
    impute.to_csv(outputdir + '/impute.csv')

    print("------------------------- The metrics of this {}x{}--------------------------- ".format(data_T.values.shape[0], data_T.values.shape[1]))
    print("Mean Absolute Error: MAE = {0:.3f}".format( mean_absolute_error(data_T, impute) ))
    print("Mean square error: MSE = {0:.3f}".format( mean_squared_error(data_T, impute) ** 0.5 ))
    print("Pearson correlation coefficient: PCC = {0:.3f}".format( pearsonr(data_true_part.reshape(-1), impute_part.values.reshape(-1))[0] ))