# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 16:04:40 2020

@author: 41207
"""
from sklearn.externals import joblib
from rdkit import Chem
from rdkit.Chem import AllChem
import pandas as pd
import numpy as np
import csv

def Model_selection(current_path): 
    model1 = joblib.load(current_path+'CYP_inhibitor_1A2.pkl')
    model2 = joblib.load(current_path+'CYP_inhibitor_2C9.pkl')
    model3 = joblib.load(current_path+'CYP_inhibitor_3A4.pkl')
    model4 = joblib.load(current_path+'PGP_inhibitor.pkl')
    model5 = joblib.load(current_path+'CYP_substrate_1A2.pkl')
    model6 = joblib.load(current_path+'CYP_substrate_2C9.pkl')
    model7 = joblib.load(current_path+'CYP_substrate_2C19.pkl')
    model8 = joblib.load(current_path+'CYP_substrate_3A4.pkl')
    model9 = joblib.load(current_path+'CYP_substrate_2D6.pkl')
    model10 = joblib.load(current_path+'CYP_inhibitor_2D6.pkl')
    model11 = joblib.load(current_path+'BBB.pkl')
    model12 = joblib.load(current_path+'CYP_inhibitor_2C19.pkl')
    return model1,model2,model3,model4,model5,model6,model7,model8,model9,model10,model11,model12
    
def ECFP_generate(filename,radius,dimension):
    df = pd.read_csv(filename,engine='python').iloc[:, 0]  
#Import the column of Smiles formula
    smiles_list = np.array(df)
    ECFP=[]
    for i in range(len(smiles_list)):
        Smiles=smiles_list[i]
        m= Chem.MolFromSmiles(Smiles)
        fp = AllChem.GetMorganFingerprintAsBitVect(m, radius, nBits=dimension)
        fp = list(map(int,list(fp.ToBitString())))
        ECFP.append(fp)
    f = open('Molecular fingerprint.csv','w')
    csv_writer = csv.writer(f)
    b=[]
    for i in range(dimension):
        b.append(i) 
    csv_writer.writerow(b)
    for i in range(len(ECFP)):
        csv_writer.writerow(ECFP[i])
    f.close()
    fingerprint_content = pd.read_csv('Molecular fingerprint.csv')
    des_list = np.array(fingerprint_content)
    return des_list
    
def predict(filename,savename):
	model1,model2,model3,model4,model5,model6,model7,model8,model9,model10,model11,model12 = Model_selection(current_path)
	dimension=2048
	radius=2
	
	des_list1 = ECFP_generate(filename,radius,dimension)
	y_predict_label1 = model1.predict(des_list1)

	y_predict_label2 = model2.predict(des_list1)

	y_predict_label3 = model3.predict(des_list1)

	y_predict_label4 = model4.predict(des_list1)

	dimension=1024
	radius=2
	des_list2 = ECFP_generate(filename,radius,dimension)
	y_predict_label5 = model5.predict(des_list2)

	y_predict_label6 = model6.predict(des_list2)

	y_predict_label7 = model7.predict(des_list2)

	y_predict_label8 = model8.predict(des_list2)

	y_predict_label9 = model9.predict(des_list2)

	y_predict_label10 = model10.predict(des_list2)

	dimension=2048
	radius=1
	des_list3 = ECFP_generate(filename,radius,dimension)
	y_predict_label11 = model11.predict(des_list3)

	y_predict_label12 = model12.predict(des_list3)
	df = pd.read_csv(filename,engine='python').iloc[:, 0]  
	f = open(savename,'w')
	csv_writer = csv.writer(f)
	csv_writer.writerow(["Smiles","CYP_inhibitor_1A2","CYP_inhibitor_2C9","CYP_inhibitor_3A4","PGP_inhibitor","CYP_substrate_1A2","CYP_substrate_2C9","CYP_substrate_2C19","CYP_substrate_3A4","CYP_substrate_2D6","CYP_inhibitor_2D6","BBB","CYP_inhibitor_2C19"])
	for i in range(len(df)):
		csv_writer.writerow([df[i],y_predict_label1[i],y_predict_label2[i],y_predict_label3[i],y_predict_label4[i],y_predict_label5[i],y_predict_label6[i],y_predict_label7[i],y_predict_label8[i],y_predict_label9[i],y_predict_label10[i],y_predict_label11[i],y_predict_label12[i]])
	f.close()
if __name__ == '__main__':
	current_path = '/home/user/zhuyang/Use_ECFP4/' 
	filename = '/home/user/zhuyang/ECFP/zy3.csv'
	savename='/home/user/zhuyang/ECFP/result.csv'
	predict(filename,savename)
