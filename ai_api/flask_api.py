from flask import Flask, request, jsonify
# -*- coding: utf-8 -*-

import warnings
warnings.filterwarnings('ignore')

# Setting Library
import torch
from torch import nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import gluonnlp as nlp
import numpy as np
from tqdm import tqdm, tqdm_notebook
import pandas as pd
from sklearn.model_selection import train_test_split
from hanspell import spell_checker
from soynlp.normalizer import emoticon_normalize
from bert_utils import BERTClassifier, BERTDataset
import bert_utils

# koBERT
from kobert.utils import get_tokenizer
from kobert.pytorch_kobert import get_pytorch_kobert_model

# Transformers
from transformers import AdamW
from transformers.optimization import get_cosine_schedule_with_warmup
import evaluate

app = Flask(__name__)

# # 모델 경로 지정
# model_path = 'model.pth'
# model = torch.load(model_path)
# device = torch.device('cuda') # GPU 사용

@app.route('/predict', methods=['POST'])
def predict_route():
    if request.method == 'POST':
        data = request.get_json()  # JSON 데이터 받기
        text = data['text']  # 텍스트 추출
        prediction = evaluate.predict(text)  # 모델을 이용해 예측하기
        return jsonify({'emotion': prediction})  # 결과 반환

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
