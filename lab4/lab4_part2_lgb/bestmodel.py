import os
import lightgbm as lgb

def get_bestmodelpath(k):
	log_path = './log/result_3.txt'
	with open(log_path, 'r') as f:
		lines = f.readlines()

	mse_list = []
	for i in range(len(lines)):
		mse = float(lines[i][45:-1])
		mse_list.append(mse)
	mse_list.sort()

	model_file = []
	for i in range(len(lines)):
		for j in range(len(lines)):
			cur = lines[j]
			if mse_list[i] == float(cur[45:-1]):
				model_file.append('./lgbmodels/' + cur[9:20])
     
	return model_file[:k]

def get_bestmodel(model_path):
	models = []
	for i in range(len(model_path)):
		tmp_path = model_path[i]
		model = lgb.Booster(model_file=tmp_path)
		models.append(model)
	return models

