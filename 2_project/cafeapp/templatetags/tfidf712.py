# -*- coding: utf-8 -*-

#{% load 712_tfidf %}


import numpy as np
import pandas as pd
from math import log
#
#from google.colab import drive
#drive.mount('/content/drive')
#path2='/content/drive/Shareddrives/스마트 캠퍼스 데이터톤/data/명사추출_combined.xlsx'
#data=pd.read_excel(path2)
#data.info()
#
    #from google.colab import drive
    #drive.mount('/content/drive')
    #path2='/content/drive/Shareddrives/스마트 캠퍼스 데이터톤/data/명사추출_delete1.xlsx'
    #data2=pd.read_excel(path2)
    #data2.info()
    #
    
    
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

def keywordimportance(data2):    
  A=data2["words"].values.astype('U')
  
  vector=CountVectorizer()
  print(vector.fit_transform(A).toarray())
  print(vector.vocabulary_)
  
  tfidfv=TfidfVectorizer().fit(A)
  print(tfidfv.transform(A).toarray())
  print(tfidfv.vocabulary_)
  
  B=tfidfv.transform(A).toarray()
  
  lst=sorted(vector.vocabulary_.items())
  llst=[]
  for i in range(len(lst)):
    llst.append(lst[i][0])
  
  d0=pd.DataFrame(B,columns=llst)
  
  imp=[]
  for i in range(len(data2)):
    k1=pd.DataFrame(d0.loc[i]).sort_values(by=[i],ascending=False) #tf-idf 값이 큰 순서대로 출력함, 클수록 중요한거 맞나?, 기준점 정할 필요?
    k1=k1[k1[i]!=0]
    k1=k1.T
    kk1=k1.columns.tolist()
    str = '' 
    separtor = ',' 
    for idx, val in enumerate(kk1): 
      str += val + ('' if idx == len(kk1) -1 else separtor)
    imp.append(str)
  
  data2['tf-idf']=imp
  data2.head()
  
  """TextRank는 바로 이 PageRank 에 파생된 알고리즘으로, PageRank에 적용된 웹 사이트 방문자 수를 '연관된 단어의 수'로 바꿔 연관된 단어의 수가 많은 단어를 중요한 단어라고 판단한다."""
  
  sentence=data2.loc[1,'tf-idf']
  A=np.dot(sentence,sentence)
  
  class GraphMatrix(object):
    def __init__(self):
      self.tfidf = TfidfVectorizer()
      self.cnt_vec = CountVectorizer()
      self.graph_sentence = []
    def build_sent_graph(self, sentence):
      tfidf_mat = self.tfidf.fit_transform(sentence).toarray()
      self.graph_sentence = np.dot(tfidf_mat, tfidf_mat.T)
      return self.graph_sentence
    def build_words_graph(self, sentence):
      cnt_vec_mat = normalize(self.cnt_vec.fit_transform(sentence).toarray().astype(float), axis=0)
      vocab = self.cnt_vec.vocabulary_
      return np.dot(cnt_vec_mat.T, cnt_vec_mat), {vocab[word] : word for word in vocab}
  
  return np.dot(B,B.T)
  
from django import template

register = template.Library()
register.filter('keywordimportance',keywordimportance)
#