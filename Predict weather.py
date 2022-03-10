Outlook =["sunny","sunny","overcast","rain","rain","rain","overcast","sunny","sunny","rain","sunny","overcast","overcast","rain"]
Temp=["hot","hot","hot","mild","cool","cool","cool","mild","cool","mild","mild","mild","hot","mild"]
Hump=["high","high","high","high","normal","normal","normal","high","normal","normal","normal","high","normal","high"]
Windy=["false","true","false","false","false","true","true","false","false","false","true","true","false","true"]
Class=["N","N","P","P","P","N","P","N","P","P","P","P","P","N"]

from sklearn import preprocessing
#creating label encoder

le=preprocessing.LabelEncoder()
#convert string labels into number

Outlook_encoded=le.fit_transform(Outlook)
Temp_encoded=le.fit_transform(Temp)
Hump_encoded=le.fit_transform(Hump)
Windy_encoded=le.fit_transform(Windy)
Class_encoded=le.fit_transform(Class)

print(Outlook_encoded)
print(Temp_encoded)
print(Hump_encoded)
print(Windy_encoded)
print(Class_encoded)


features=zip(Outlook_encoded,Temp_encoded,Hump_encoded,Windy_encoded)
resultFeatures=list(features)
print(resultFeatures)



from sklearn.naive_bayes import GaussianNB

model = GaussianNB()
model.fit(resultFeatures,Class)
predicted =model.predict([[2,2,0,1]])
print("predict:",predicted)


