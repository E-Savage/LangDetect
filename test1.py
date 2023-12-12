import pandas as pd
import numpy as np
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/dataset.csv")

# language detection model
x = np.array(data["Text"])
y = np.array(data["language"])

cv = CountVectorizer()
x = cv.fit_transform(x)
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

# this problem uses multiclassification so.... Naive Bayes algo is the way to go

model = MultinomialNB()
model = model.fit(X_train,y_train)
model.score(X_test,y_test)

# saving model to a file, save vectorizer to a file
joblib.dump(model, 'langModel.joblib')
joblib.dump(cv,'vectorizer.joblib')

sentence = input("Enter a Text: ")
data = cv.transform([sentence]).toarray()
detected_sentence = model.predict(data)
print(detected_sentence)