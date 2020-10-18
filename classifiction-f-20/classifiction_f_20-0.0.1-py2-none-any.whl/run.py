from sklearn.externals import joblib
from rdkit import Chem
from rdkit.Chem import AllChem
import pandas as pd
import numpy as np
import csv

def Model_selection(current_path,model): 
    cf = joblib.load(current_path+model)
    return cf
current_path = '/home/user/jiangrong/ADMETlab-master/classification/classification_model/classification_model/F-20/'
model = 'model_0.pkl'

def MACCS_generate(filename,savefile):


    df = pd.read_csv(filename,engine='python').iloc[:, 0]  
    smiles_list = np.array(df)
    MACCS=[]
    for i in range(len(smiles_list)):
        Smiles=smiles_list[i]
        m= Chem.MolFromSmiles(Smiles)
        fp = AllChem.GetMACCSKeysFingerprint(m)
        fp = list(map(int,list(fp.ToBitString())))
        MACCS.append(fp)
    f = open(savefile,'w')
    csv_writer = csv.writer(f)
    b=[]
    for i in range(0,167):
        b.append(i) 
    csv_writer.writerow(b)
    for i in range(len(MACCS)):
        csv_writer.writerow(MACCS[i])
    f.close()
    fingerprint_content = pd.read_csv(savefile)
    des_list = np.array(fingerprint_content)
    return des_list


filename = 'zy3.csv'
savefile = 'Molecular fingerprint.csv'

MACCS_generate(filename,savefile)
###################################### Prediction ##########
cf = Model_selection(current_path,model)
des_list = MACCS_generate(filename,savefile)
y_predict_label = cf.predict(des_list)
y_predict_proba = cf.predict_proba(des_list)
print '#'*10+'Results labels'+'#'*10
print y_predict_label
print '#'*10+'Results probabilities'+'#'*10
print y_predict_proba    