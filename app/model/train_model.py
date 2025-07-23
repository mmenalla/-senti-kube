from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

texts = ["I love this", "Horrible", "Amazing experience", "Not good"]
labels = [1, 0, 1, 0]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = LogisticRegression()
model.fit(X, labels)

with open("app/model/model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("app/model/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)
