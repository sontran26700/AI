import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.preprocessing import LabelEncoder
from collections import defaultdict
from nltk.corpus import wordnet as wn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import model_selection, naive_bayes, svm
from sklearn.metrics import accuracy_score

np.random.seed(500)

Corpus = pd.read_csv(r"E:\projecttrithuenhantao\parin.csv",encoding='latin-1') #encoding latin1 : các kí tự đặc biệt
dataset = pd.read_csv(r"E:\projecttrithuenhantao\parin.csv",header=None)

#step1 : chuyen doi cac tu ve dang chu thuong
Corpus['text'] = [entry.lower() for entry in Corpus['text']]

# Step2: words tokens. mỗi từ trong 1 câu là 1 mảng và tách thành từng từ .
Corpus['text']= [word_tokenize(entry) for entry in Corpus['text']]
# Step3 : xóa các stopwords
# WordNetLemmatizer requires Pos tags to understand if the word is noun or verb or adjective etc. By default it is set to Noun
tag_map = defaultdict(lambda : wn.NOUN)
tag_map['J'] = wn.ADJ
tag_map['V'] = wn.VERB
tag_map['R'] = wn.ADV


for index,entry in enumerate(Corpus['text']):#index là số rows trong data, entry từng row, mỗi row là 1 câu)
    # tạo ra 1 cái mảng trống lên lưu lại từ theo qtac.
    Final_words = []
    #
    word_Lemmatized = WordNetLemmatizer()
    # pos_tag function below will provide the 'tag' i.e if the word is Noun(N) or Verb(V) or something else.
    for word, tag in pos_tag(entry): # cho chạy trong từng câu , xđ từng , kiểu thẻ tag
        # kiểm tra các stopwords và trong bản chữ cái alphabet
        if word not in stopwords.words('english') and word.isalpha():
            word_Final = word_Lemmatized.lemmatize(word,tag_map[tag[0]])
            Final_words.append(word_Final) # thỏa mãn thì append các word vô final_Words

    # Tập mà các từ xử lí cuối cùng cho mỗi lần lặp,
    Corpus.loc[index,'text_final'] = str(Final_words)
    #print(Corpus)
Train_X, Test_X, Train_Y, Test_Y = model_selection.train_test_split(Corpus['text_final'],Corpus['label'],test_size=0.3)

Encoder = LabelEncoder() # hỗ trợ đưa về mang vector
Train_Y = Encoder.fit_transform(Train_Y)
Test_Y = Encoder.fit_transform(Test_Y)
Tfidf_vect = TfidfVectorizer(max_features=5000)
Tfidf_vect.fit(Corpus['text_final'])
Train_X_Tfidf = Tfidf_vect.transform(Train_X)
Test_X_Tfidf = Tfidf_vect.transform(Test_X)
#print('trainx',Train_X_Tfidf)
#print('testx',Test_X_Tfidf)
#print("vectorVC",Tfidf_vect.vocabulary_)
#print("len",len(Tfidf_vect.vocabulary_))

# phân loại NB trên tập data
Naive = naive_bayes.MultinomialNB()
Naive.fit(Train_X_Tfidf,Train_Y)
# predict the labels on validation dataset
predictions_NB = Naive.predict(Test_X_Tfidf)
# dùng accuracy_score để tính accuracy
print("Naive Bayes Accuracy: ",accuracy_score(predictions_NB, Test_Y)*100)
# dùng SVM
# training data vs SVM
SVM = svm.SVC(C=1.0, kernel='linear', degree=3, gamma='auto')
SVM.fit(Train_X_Tfidf,Train_Y)
# predict the labels on validation dataset
predictions_SVM = SVM.predict(Test_X_Tfidf)
# Use accuracy_score function to get the accuracy
print("SVM Accuracy:",accuracy_score(predictions_SVM, Test_Y)*100)


dataset.rename(columns={0: 'text', 1: 'label'}, inplace=True)
dataset['output'] = np.where(dataset['label'] == 'emotion', 1, 0)
Num_Words = dataset.shape[0]
print(dataset.head(778))


count=0
for i in dataset['output']:
    if i ==1:
        count= count+1
print('count',count)



#print("\nSize of input file is ", dataset.shape)




