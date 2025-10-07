import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn import preprocessing


weather = ["Sunny","Sunny","Overcast","Rainy","Rainy","Rainy","Overcast",
           "Sunny","Sunny","Rainy","Sunny","Overcast","Overcast","Rainy"]

temp = ["Hot","Hot","Hot","Mild","Cool","Cool","Cool","Mild","Cool",
        "Mild","Mild","Hot","Mild","Cool"]

play = ["No","No","Yes","Yes","Yes","No","Yes","No","Yes",
        "Yes","Yes","Yes","Yes","No"]


le = preprocessing.LabelEncoder()
weather_encoded = le.fit_transform(weather)
temp_encoded = le.fit_transform(temp)
label = le.fit_transform(play)

print("Weather:", weather_encoded)
print("Temp:", temp_encoded)
print("Play:", label)

 
features = np.array(list(zip(weather_encoded, temp_encoded)))

print("Features:\n", features)


model = GaussianNB()
model.fit(features, label)


predicted = model.predict([[0, 2]])  
print("Predicted:", predicted)