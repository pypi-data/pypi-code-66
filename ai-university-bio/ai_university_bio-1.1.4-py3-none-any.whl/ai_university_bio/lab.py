import pandas as pd
import numpy as np
from tensorflow.keras.models import Model, Sequential # загружаем абстрактный класс базовой модели сети от кераса и последовательную модель
# Из кераса загружаем необходимые слои для нейросети
from tensorflow.keras.layers import Dense, Flatten, Reshape, Input, Conv2DTranspose, concatenate, Activation, MaxPooling2D, Conv2D, BatchNormalization
from tensorflow.keras import backend as K # подтягиваем базовые керасовские функции
from tensorflow.keras.optimizers import Adam # загружаем выбранный оптимизатор
from tensorflow.keras import utils # загружаем утилиты кераса
from tensorflow.keras.datasets import mnist, fashion_mnist # загружаем готовые базы mnist

import matplotlib.pyplot as plt # из библиотеки для визуализации данных возьмём интерфейс для построения графиков простых функций
from tensorflow.keras.preprocessing import image # модуль для отрисовки изображения
import numpy as np # библиотека для работы с массивами данных
import pandas as pd # библиотека для анализа и обработки данных
from PIL import Image # модуль для отрисовки изображения
from sklearn.model_selection import train_test_split # модуль для разбивки выборки на тренировочную/тестовую
from sklearn.preprocessing import StandardScaler # модуль для стандартизации данных
import random as random # Импортируем библиотку генерации случайных значений
from pickle import load
from IPython.display import clear_output
import os #
import time
import requests
import seaborn as sns

sns.set_style('darkgrid')

class Dataset():
    def __init__(self, filename):
        type_dg = {
                    'InA':np.int32,'InB':np.int32,'InC':np.int32,'InD':np.int32,
                    'InE':np.float32,'InF':np.float32,'InG':np.float32,'InH':np.float32,'InI':np.float32,
                    'InJ':np.float32,'InK':np.float32,'InL':np.float32,
                    'OutM':np.int32,
                    'InCalcN':np.float32, 'InCalcO':np.float32,
                    'InCalcP':np.float32,
                    'InCalcQ':np.float32,'InCalcR':np.float32,
                    'InCalcS':np.float32    
                    }
        df = pd.read_csv(filename, header=1, dtype='str')
        for i in df.columns:
            df[i] = df[i].str.replace(',','.')
        df.fillna(0,inplace=True)
        df.astype(type_dg)
        data_x = df[['InA','InB','InC','InD', 'InE','InF','InG','InH','InI','InJ','InK','InL','InCalcN','InCalcO','InCalcP','InCalcQ','InCalcR','InCalcS']].values.astype('float32')
        data_y = df['OutM'].values.astype('float32')
        mask = self.data_y==1
        self.x_train = data_x[mask]
        self.y_train  = data_y[mask]
        self.x_false = data_x[~mask]        
        return
        
    def baseAutoencoder(self, x_train): # зададим функцию создания базового автокодировщика
        inp = Input((x_train.shape[1],)) # задаём входные размеры            
        x = Dense(64, activation='relu') (inp)
        x = Dense(x_train.shape[1], activation='linear') (x)
        
        model = Model(inp, x) # указываем модель, с оригинальным изображением на входе в сеть и сжатым-разжатым на выходе из сети
        model.compile(optimizer=Adam(lr=0.0001),
                      loss='mean_squared_error') # компилируем модель с оптимайзером Адам и среднеквадратичной ошибкой
        return model # функция вернёт заданную модель
        
class Laboratory():
    def __init__(self):
        self.min_value = 0.0141018815
        self.mean_value = 0.009435666
        self.max_value = 0.0011837325
        self.AE = self.load_model()
        self.scaler = self.load_scaler()
        self.result = []
        
    def load_model(self):        
        inp = Input((18,))        
        x = Dense(8, activation='relu') (inp)
        x = Dense(18, activation='linear') (x)
        
        model = Model(inp, x) # указываем модель, с оригинальным изображением на входе в сеть и сжатым-разжатым на выходе из сети
        model.compile(optimizer=Adam(lr=0.0001),
                      loss='mean_squared_error') # компилируем модель с оптимайзером Адам и среднеквадратичной ошибкой        
        url = 'https://drive.google.com/uc?export=download&confirm=no_antivirus&id=19ZZTwQ9kA0S1X0o9SXdrB2lCRJ1-ereH'
        r = requests.get(url)
        f = open('AE.h5','wb').write(r.content)
        model.load_weights('AE.h5')        
        return model # функция вернёт заданную модель
    
    def load_scaler(self):
        url = 'https://drive.google.com/uc?export=download&confirm=no_antivirus&id=1DprL_xY3YNm2pQn5iPbDO4TvkmihwGBZ'
        r = requests.get(url)
        f = open('scaler.pkl','wb').write(r.content)
        return load(open('scaler.pkl', 'rb'))
        
    def getSurvPopul(self,
        popul,
        val,
        nsurv,
        reverse
        ):
        newpopul = [] # Двумерный массив для новой популяции
        sval = sorted(val, reverse=reverse) # Сортируем зачения в val в зависимости от параметра reverse    
        for i in range(nsurv): # Проходимся по циклу nsurv-раз (в итоге в newpopul запишется nsurv-лучших показателей)
            index = val.index(sval[i]) # Получаем индекс i-того элемента sval в исходном массиве val
            newpopul.append(popul[index]) # В новую папуляцию добавляем элемент из текущей популяции с найденным индексом
        return newpopul, sval # Возвращаем новую популяцию (из nsurv элементов) и сортированный список

    def getParents(self,
        curr_popul,
        nsurv
        ):   
        indexp1 = random.randint(0, nsurv - 1) # Случайный индекс первого родителя в диапазоне от 0 до nsurv - 1
        indexp2 = random.randint(0, nsurv - 1) # Случайный индекс второго родителя в диапазоне от 0 до nsurv - 1    
        botp1 = curr_popul[indexp1] # Получаем первого бота-родителя по indexp1
        botp2 = curr_popul[indexp2] # Получаем второго бота-родителя по indexp2    
        return botp1, botp2 # Возвращаем обоих полученных ботов

    def crossPointFrom2Parents(self,
        botp1,
        botp2, 
        j
        ):
        pindex = random.random() # Получаем случайное число в диапазоне от 0 до 1
        if pindex < 0.5:
            x = botp1[j]
        else:
            x = botp2[j]
        return x # Возвращаем значние бота
       
    def getMSE(self, x1, x2): # создадим функцию среднеквадратичной ошибки
        x1 = x1.flatten() # сплющиваем в одномерный вектор
        x2 = x2.flatten() # сплющиваем в одномерный вектор
        delta = x1 - x2 # находим разницу
        return sum(delta ** 2) / len(delta) # и возвращаем сумму квадратов разницы, делённую на длину разницы
    
    def StartProcess(self, iteration, InA,	InB, InC, InD, InE, InF, InG, InH, InI, InJ, InK, InL):
        sample_in = np.array([InA,	InB, InC, InD, InE, InF, InG, InH, InI, InJ, InK, InL,0,0,0,0,0,0])
        sample_in = self.scaler.transform(sample_in.reshape(1,-1)).reshape(-1)
        n = 100 # Размер популяции
        nsurv = 20 # Количество выживших (столько лучших переходит в новую популяцию)
        nnew = n - nsurv # Количество новых (столько новых ботов создается)
        l = 6 # Длина бота
        epohs = iteration # Количество эпох

        mut = .15 # Коэфициент мутаций

        popul = [] # Двумерный массив популяции, размерностью [n, l]. 100 ботов по 8 компонентов каждый
        val = [] # Одномерный массив значений этих ботов

        for i in range(n): # Проходим по всей длине популяции    
            popul.append([]) # Создаем пустого бота
            for _ in range(l):
                popul[i].append(np.random.uniform(0,1.))
        
        for it in range(epohs): # Пробегаемся по всем эпохам
            if it==100:
                mut*=0.5
            if it==200:
                mut*=0.5
            if it==300:
                mut*=0.5
            val = [] # Создаем пустой список для значений ботов

            for i in range(n): # Проходим по всей длине популяции           
                bot = popul[i]
                sample = np.array(list(sample_in[:12])+bot)       
                error = 0
                for j in range(6):
                    if bot[j] > 1:
                        error+=1
                    if bot[j] < 0:
                        error+=1
                popul[i][-1]=0
                sample[-1]=0
                f = self.AE.predict(sample[None,...])
                f = self.getMSE(sample,f)
                f+= error
                val.append(f) # добавляем модуль значения в список на эпоху
                                   # в этой задаче будем искать 0 функции
            newpopul, sval = self.getSurvPopul(popul, val, nsurv, 0) # Получаем новую популяцию и сортированный список значнией            
            clear_output(wait=True)
            #print(it, " ", [round(s,5) for s in sval[0:10]]) # Выводим 5 лучших ботов
            print('Итерация: ',str(it+1),sep='')
            x_l = 0
            height = 0.02 - sval[0]
            plt.figure(figsize=(4,7))
            plt.bar(x_l, height, align='center', color='g', linewidth = 10, alpha=0.2) # align - выравнивание стержней по координатам х                                                 
            plt.title('Текущая точность')
            plt.ylim((0,0.03))
            #plt.xlim((-0.55,0.75))
            plt.hlines(0.02 - self.min_value, -.5, .5, color='r', label='Минимальная')
            plt.hlines(0.02 - self.mean_value, -.5, .5, color='y', label='Приемлемая')
            plt.hlines(0.02 - self.max_value, -.5, .5, color='g', label='Лучшая')
            #plt.yticks(np.arange(0, 0.03, step=0.03))
            #plt.xticks(np.arange(-.5, 0.5, step=0.25))
            #plt.yticks(x_l, ['Модель'])            
            plt.legend()
            plt.show()
            
            #print([round(s,2) for s in newpopul[0]])
            #print()
         
            for i in range(nnew): # Проходимся в цикле nnew-раз 
                botp1, botp2 = self.getParents(newpopul, nsurv) # Из newpopul(новой популяции) получаем двух случайных родителей-ботов
                newbot = [] # Массив для нового бота
                # проходимся по длине бота и осуществляем смешивание/скрещивание от родителей
                for j in range(l): # Проходим по всей длине бота
                    x = self.crossPointFrom2Parents(botp1, botp2, j) # Получаем значение для j-ого компонента бота
                    x += mut*(2*random.random() - 1.0)
                    newbot.append(x) # Добавялем новое значение в бота      
                newpopul.append(newbot) # Добавляем бота в новую популяцию 
                #(таким образом к nsurv-лучших ботов предыдующей популяции добавится nnew-новых ботов)
            
            popul = newpopul # Записываем в popul посчитанную новую популяцию
        
        self.result = popul[0].copy()       

    def getResult(self):
        title=['InCalcN','InCalcO','InCalcP','InCalcQ','InCalcR','InCalcS']
        inv = self.scaler.inverse_transform(np.array(list(np.arange(12))+self.result).reshape(1,-1)).reshape(-1)
        print('Результат:')
        for i in range(6):
            print(title[i],': ', round(inv[12+i],3))
        
        
        