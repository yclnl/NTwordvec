import fasttext
import numpy as np
import json
from sklearn.tree import ExtraTreeClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn.model_selection import train_test_split
model = fasttext.cbow('rawData.txt', 'model')
ngrams = 3
id_map = json.load(open('label_id.json'))
count = 0
feature = []
target = []
for line in open('data_seg.txt'):
    lineList = line.split(' ')
    label = lineList[len(lineList)-1].split('\n')[0]
    label_id = id_map[label][0]
    target.append([label_id])
    wordList = lineList[:len(lineList)-1]
    wordvec = np.zeros(100*ngram)
    for ngram in range(1,ngrams+1):
        if len(wordList)>=ngram:
            for i in range(0,len(wordList)-ngram):
                word=''
                for idx in range(i,i+ngram):
                    word+=wordList[idx]
                wordvec[100*(ngram-1):100*(ngram)] += np.array(model[word])

            wordvec /= (len(wordList)-ngram+1)
        else:
            word = ''
            for subword in wordList:
                word+=subword
            wordvec[100*(ngram-1):100*ngram] = np.array(model[word])
    feature.append(wordvec.tolist())
feature =np.array(feature)
print(feature.shape)
np.save('feature.npy',feature)
np.save('target.npy',target)

