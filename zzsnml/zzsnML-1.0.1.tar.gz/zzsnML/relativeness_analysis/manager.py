# -*- coding: utf-8 -*-
from relativeness_analysis.vocabulary import Vocabulary
from relativeness_analysis.classifier2 import xgboost
from relativeness_analysis.utils import data_processor
import time, os
import numpy as np 
# import pandas as pd
import cx_Oracle
import pickle


os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'


class TrainManager(object):
	def __init__(self):
		self.signature = int(time.time())

	def read_sql(self, sql, con):
		# print('Fetching data from remote sql...')
		# raw_data = pd.read_sql_query(sql, con)
		# with open('data.pd', 'wb') as f:
		# 	pickle.dump(raw_data, f)
		# raw_data.to_excel('raw_data.xlsx')
		# data = {}
		# for record in raw_data.iterrows:
		# 	company = record['tid'].strip()
		# 	article = record['content_no_tag'].strip()
		# 	title = record['title'].strip()
		# 	relevant = record['relevance'].strip()
		# 	emotion = '非负' # record['emotion'].strip()
		# 	data[company] = data.get(company, []) + [(title+'。'+article, relevant, emotion)]
		# conn.close()
		# return data
		cursor = con.cursor()
		cursor.execute(sql)
		data = {}

		def convert(col):
			if isinstance(col, cx_Oracle.LOB):
				return col.read().decode('utf-8')
			else:
				return col

		for record in cursor:
			company = convert(record[2])
			title = convert(record[0])
			article = convert(record[1])
			relevant = convert(record[3])
			if article is None:
				continue
			else:
				if relevant is None:
					relevant = 1
				if title is not None:
					title = title.strip()
				else:
					title = ''
				article = article.strip()
			relevant = '保留' if relevant == 0 else '删除'
			emotion = '非负'
			
			data[company] = data.get(company, []) + [(title+'。'+article, relevant, emotion)]
		con.close()
		return data

	def make_dirs(self, path):
		dir_path = os.path.join(os.getcwd(), path)
		if not os.path.isdir(dir_path):
			os.makedirs(dir_path)
	def train(self, sql, con, _all=False, _emotion=False, config=None, transformer='tf', transformer_norm='l2', save_to_folder=None, \
			lr=0.1, reg_alpha=0, reg_lambda=1, objective='binary:logitraw', with_sample_weight=True, subsample=1, \
			min_child_weight=1, scale_pos_weight=1, thres=0.5, train_ratio=0.8):
		print('Fetching data from remote SQL...')
		data = self.read_sql(sql, con)
		print('Done!')

		dp = data_processor(data, transformer=transformer, transformer_norm=transformer_norm)
		processed_data, processed_label, processed_label_dict = dp.preprocess(_all=_all, _emotion=_emotion)
		# print(processed_label)

		for company in processed_data:
			if len(processed_label[company]) == 0:
				print('%s 没有数据！跳过该类！' % company)
				continue
			try:
				dp.reset()
				vocab = Vocabulary(signature=self.signature, name='vocab-%s'%company, min_word_len=2)
				dp.update_vocab(vocab, processed_data[company])
				print('%s, after updating, %s' % (company, vocab.get_size()))
				transformed_data = dp.transform(vocab, processed_data[company], processed_label[company])
				self.make_dirs(save_to_folder)
				vocab_save_to = os.path.join(save_to_folder, 'vocab-%s' % company)
				vocab.save(vocab_save_to)  # vocab-all-1491195238.voc

				
				xgb = xgboost(processed_label_dict[company], self.signature, lr=lr, reg_alpha=reg_alpha, reg_lambda=reg_lambda, \
							objective=objective, with_sample_weight=with_sample_weight, subsample=subsample, thres=thres,\
							min_child_weight=min_child_weight, scale_pos_weight=scale_pos_weight)
				(X_train, Y_train), (X_test, Y_test) = xgb.train_test_split(transformed_data, processed_label[company], train_ratio=train_ratio)

				print('Training on %s' % company)
				if reg_alpha > 0 and reg_lambda > 0:
					penalty = 'l1+l2'
				elif reg_alpha > 0:
					penalty = 'l1'
				elif reg_lambda > 0:
					penalty = 'l2'
				else:
					penalty = 'None'

				# xgboost-all-tf-l1+l2-l2-0.5-1496718804.xgb
				clf_save_to = os.path.join(save_to_folder, 'xgboost-%s-%s-%s-%s-%s' % (company, transformer, penalty, transformer_norm, thres))
				xgb.train(X_train, Y_train, save_to=clf_save_to)

				print('On training dataset:')
				xgb.report(X_train, Y_train, verbose=False)

				print('On test dataset:')
				xgb.report(X_test, Y_test, verbose=False)

			except Exception as e:
				print(e)
				# raise e


def test(connection_string = 'cis/cis_zzsn9988@118.190.174.96:1521/orcl', begin_date = '2017-03-01', end_date = '2017-07-13'):
	'''
	begin_date:开始日期
	end_date:结束日期
	'''
	# company list
	# company_list = ['3745', '3089', '3748', '2783', '3440']
	company_list = ['3745,3089,3748,2783,3440', '3741,3420,3319']
	# 模型参数
	save_to_folder = './tmp'  # 存放训练结果(分类器和词典)的目录
	_all = False  # 是否区分企业进行训练，True表示不区分
	_emotion = False  # 是否区分情感正负面进行训练，True表示区分
	thres = 0.5
	lr = 0.1
	reg_alpha = 0
	reg_lambda = 1
	objective = 'binary:logitraw'
	with_sample_weight = True
	subsample = 1
	min_child_weight = 1
	scale_pos_weight = 1
	for company in company_list:
		ora_conn = cx_Oracle.connect(connection_string)
		sql_query = '''select b.title,b.content_no_tag,'P'||t.tid as tid,t.delflag as relevance from cis_ans_basedata b inner join cis_ans_basedata_type t on  (b.id=t.bid and t.delflag is not null) 
					where (b.orientation !=2 or b.orientation is null) 
					and t.tid in (%s)
					and B.Publish_Date > '%s' and B.Publish_Date < '%s' ''' % (company, begin_date, end_date)
		# print(sql_query)
		tm = TrainManager()
		tm.train(sql_query, ora_conn, _all=_all, _emotion=_emotion, save_to_folder=save_to_folder, lr=lr, reg_alpha=reg_alpha, \
				reg_lambda=reg_lambda, objective=objective, with_sample_weight=with_sample_weight, subsample=subsample, \
				thres=thres, min_child_weight=min_child_weight, scale_pos_weight=scale_pos_weight)

if __name__ == '__main__':
	test()
