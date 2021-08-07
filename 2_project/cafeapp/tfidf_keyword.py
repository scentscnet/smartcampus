
from re import search
import numpy as np
import pandas as pd
from math import log
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
def sortingimportance(data1,q):
    ##object_list=Subject.objects.all().values('words')
    #data = pd.DataFrame.from_records(request)
    print('raw:',data1)
    data=pd.DataFrame(data1)
    print('after pd : ',data)
    return data, data1
    #A=data['words'].astype('U')
    ##vector=CountVectorizer()
    #tfidfv=TfidfVectorizer().fit(A)
    #if q in tfidfv.vocabulary_.keys():
    #    wordnumber=tfidfv.vocabulary_[q]
    #    B=tfidfv.transform(A).toarray()
    #    df=pd.DataFrame(B)
    #    df.sort_values(by=[wordnumber], axis=0, ascending=[False])
    #    return df
    #else:
    #    return '입력하신 단어의 과목이 없습니다.'
