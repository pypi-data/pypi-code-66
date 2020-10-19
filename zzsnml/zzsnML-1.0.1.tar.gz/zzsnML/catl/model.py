# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 2018

@author: WuDaqing
"""

import numpy as np
import heapq
from sklearn import linear_model
from sklearn.externals import joblib
import matplotlib.pyplot as plt
from sklearn import metrics

class ensemble(object):
    def __init__(self,name,r,data,labels,model_save_path,results_save_path):
        self.Name = name
        self.Data = data
        self.Labels = labels
        self.model_save_path = model_save_path
        self.results_save_path = results_save_path

        self.Num = len(labels)
        self.Index = [i for i in range(self.Num)]

        print(self.Name+' | Train |  Title  | Number of Data     | '+str(self.Num))
        self.Num_Positive = self.Labels.count(1)
        self.Num_Negative = self.Labels.count(0)
        print(self.Name+' | Train |  Title  | Number of Positive | '+str(self.Num_Positive))
        print(self.Name+' | Train |  Title  | Number of Negative | '+str(self.Num_Negative))
        print(self.Name+' | Train |  Title  | Data Loaded'+'\n')

        self.Ite = 1
        self.Index_Retain_Train = [i for i in range(self.Num)]
        self.Index_Retain_Predict = [i for i in range(self.Num)]
        self.Index_Delete = {}
        self.Recall = []
        self.Precision = []
        self.F1 = []
        self.Threshold = {}
        self.recall = r
        
        self.config = True

    def classifier(self,data,labels):
        clf = linear_model.SGDClassifier(loss='log',penalty='l1',alpha=1e-3,class_weight='balanced',learning_rate='optimal',eta0=0.0)
        clf.fit(data,labels)
        probabilities = []
        probabilities_positive = []
        probabilities_negative = []
        tmp = clf.predict_proba(data)
        for i in range(len(data)):
            if labels[i] == 1:
                probabilities.append(tmp[i][1])
                probabilities_positive.append(tmp[i][1])
            else:
                probabilities.append(tmp[i][1])
                probabilities_negative.append(tmp[i][1])         
        return clf,probabilities,probabilities_positive,probabilities_negative

    def unit(self):
        data_train = [self.Data[idx] for idx in self.Index_Retain_Train]
        labels_train = [self.Labels[idx] for idx in self.Index_Retain_Train]

        num_positive = labels_train.count(1)
        num_negative = labels_train.count(0)

        print(self.Name+' | Train |  Title  | iteration | '+str(self.Ite)+' | Logistic Regression ... ...')
        clf_lr,probabilities_train,probabilities_positive_train,probabilities_negative_train = self.classifier(data=data_train,labels=labels_train)
        
        print(self.Name+' | Train |  Title  | iteration | '+str(self.Ite)+' | Adjust Threshold ... ...')

        threshold = heapq.nsmallest(int(0.01*self.Num_Positive),probabilities_positive_train)[-1]
        
        Index_Retain_Train = []
        for i in range(num_positive+num_negative):
            if labels_train[i] == 1:
                Index_Retain_Train.append(self.Index_Retain_Train[i])
            elif probabilities_train[i] > threshold:
                Index_Retain_Train.append(self.Index_Retain_Train[i])
        self.Index_Retain_Train = Index_Retain_Train
        
        data_predict = [self.Data[idx] for idx in self.Index_Retain_Predict]
        tmp = clf_lr.predict_proba(data_predict).tolist()
        probabilities_predict = list(map(list,zip(*tmp)))[1]

        Predictions = [0 for i in range(self.Num)]        
        Index_Retain_Predict = []
        self.Index_Delete[self.Ite] = []
        for i in range(len(data_predict)):
            if probabilities_predict[i] >= threshold:
                Index_Retain_Predict.append(self.Index_Retain_Predict[i])
                Predictions[self.Index_Retain_Predict[i]] = 1
            else:
                self.Index_Delete[self.Ite].append(self.Index_Retain_Predict[i])
        self.Index_Retain_Predict = Index_Retain_Predict

        recall = metrics.recall_score(self.Labels,Predictions,pos_label=1)
        precision = metrics.precision_score(self.Labels,Predictions,pos_label=1)
        f1 = metrics.f1_score(self.Labels,Predictions,pos_label=1)

        if recall >= self.recall:
            self.f1 = f1
            print(self.Name+' | Train |  Title  | iteration | '+str(self.Ite)+' | Positive Recall    | ' + '%.4f'%recall)
            print(self.Name+' | Train |  Title  | iteration | '+str(self.Ite)+' | Positive Precision | ' + '%.4f'%precision)
            print(self.Name+' | Train |  Title  | iteration | '+str(self.Ite)+' | Positive F1        | ' + '%.4f'%f1+'\n')  
            self.Recall.append(recall)
            self.Precision.append(precision)
            self.F1.append(f1)
            joblib.dump(clf_lr,self.model_save_path+self.Name+'_iteration_'+str(self.Ite)+'_train_title_classifier.m')
            self.Threshold[self.Ite] = threshold
            self.Ite += 1
        else:
            print(self.Name+' | Train |  Title  | iteration | '+str(self.Ite)+' | Positive Recall Less Than Given Recall'+'\n')
            self.Index_Retain_Predict += self.Index_Delete[self.Ite]
            del self.Index_Delete[self.Ite]
            self.config = False

    def train_title(self):
        while self.config == True:
            self.unit()

        plt.figure(figsize=(8,8),dpi=100)
        plt.xlim(0,self.Ite+1)
        plt.scatter(range(1,self.Ite),self.Recall,s=100,marker='+',color='r')
        plt.plot(range(1,self.Ite),self.Recall,linestyle='-',color='r',linewidth=1.5,label='recall')
        plt.scatter(range(1,self.Ite),self.Precision,s=100,marker='+',color='g')
        plt.plot(range(1,self.Ite),self.Precision,linestyle='-',color='g',linewidth=1.5,label='precision')
        plt.scatter(range(1,self.Ite),self.F1,s=100,marker='+',color='b')
        plt.plot(range(1,self.Ite),self.F1,linestyle='-',color='b',linewidth=1.5,label='f1')
        plt.legend(loc='lower right',fontsize=10)
        plt.savefig(self.results_save_path+self.Name+'_train_title_results.png')
        
        return self.Threshold,self.Index_Retain_Predict,self.Index_Delete
    
    def train_content(self,data,r):
        data_train = data
        labels_train = [self.Labels[idx] for idx in self.Index_Retain_Predict]

        print(self.Name+' | Train | Content | Number of Data     | '+str(len(labels_train)))
        num_positive = labels_train.count(1)
        num_negative = labels_train.count(0)
        print(self.Name+' | Train | Content | Number of Positive | '+str(num_positive))
        print(self.Name+' | Train | Content | Number of Negative | '+str(num_negative)+'\n')

        clf_xg = linear_model.SGDClassifier(loss='log',penalty='l1',alpha=1e-3,class_weight='balanced',learning_rate='optimal',eta0=0.0)
        clf_xg.fit(data_train,labels_train)

        joblib.dump(clf_xg,self.model_save_path+self.Name+'_train_content_classifier.m')

        tmp = clf_xg.predict_proba(np.array(data_train)).tolist()
        probabilities_predict = list(map(list,zip(*tmp)))[1]

        Recall = []
        Precision = []
        F1 = []
        Threshold = []
        for t in [x/1000 for x in range(1001)]:
            Predictions = [0 for i in range(self.Num)]
            for i in range(len(data_train)):
                if probabilities_predict[i] >= t:
                    Predictions[self.Index_Retain_Predict[i]] = 1
            recall = metrics.recall_score(self.Labels,Predictions,pos_label=1)
            precision = metrics.precision_score(self.Labels,Predictions,pos_label=1)
            f1 = metrics.f1_score(self.Labels,Predictions,pos_label=1)
            Recall.append(recall)
            Precision.append(precision)
            F1.append(f1)
            Threshold.append(t)
            if recall < r:
                break

        print(self.Name+' | Train | Content |  Finally   | Threshold          | ' + '%.4f'%Threshold[-1]+'\n') 
        
        print(self.Name+' | Train | Content |  Finally   | Positive Recall    | ' + '%.4f'%Recall[-1])
        print(self.Name+' | Train | Content |  Finally   | Positive Precision | ' + '%.4f'%Precision[-1])
        print(self.Name+' | Train | Content |  Finally   | Positive F1        | ' + '%.4f'%F1[-1]+'\n')  

        plt.figure(figsize=(8,8),dpi=100)
        plt.plot(Threshold,Recall,linestyle='-',color='r',linewidth=1.5,label='recall')
        plt.plot(Threshold,Precision,linestyle='-',color='g',linewidth=1.5,label='precision')
        plt.plot(Threshold,F1,linestyle='-',color='b',linewidth=1.5,label='f1')
        plt.legend(loc='lower center',fontsize=10)
        plt.savefig(self.results_save_path+self.Name+'_train_content_results.png')       

        Index_Retain_Predict = []
        Index_Delete = []
        for i in range(len(data_train)):
            if probabilities_predict[i] >= Threshold[-1]:
                Index_Retain_Predict.append(self.Index_Retain_Predict[i])
            else:
                Index_Delete.append(self.Index_Retain_Predict[i])
        
        return Threshold[-1],Index_Retain_Predict,Index_Delete
