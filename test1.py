import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/dataset.csv")
print(data.head())

print(data.isnull().sum())

print(data['language'].value_counts())

# language detection model
x = np.array(data["Text"])
y = np.array(data["language"])

cv = CountVectorizer()
x = cv.fit_transform(x)
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

# this problem uses multiclassification so.... Naive Bayes algo is the way to go

model = MultinomialNB()
model.fit(X_train,y_train)
model.score(X_test,y_test)


user = input("Enter a Text: ")
data = cv.transform([user]).toarray()
output = model.predict(data)
print(output)