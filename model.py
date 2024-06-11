from sklearn.ensemble import StackingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
import sys
import json

class Ensemble():
  def __init__(self, base_models={"SVC": SVC(), "KNN": KNeighborsClassifier(), "DecisionTree": DecisionTreeClassifier()}, meta_model=LogisticRegression(), dataset=pd.notnull):
    self.meta_model=meta_model
    self.ds = dataset
    self.X = dataset.drop(columns="credit_risk", axis = 1)
    self.y = dataset['credit_risk']
    self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)
    self.models = list()
    for name, model in base_models.items():
      self.models.append((name, model))

  def fit(self):
    self.stack_model = StackingClassifier(estimators=self.models, final_estimator=self.meta_model, cv=5)
    self.stack_model.fit(self.X_train, self.y_train)

  def predict(self, X_pred):
    return self.stack_model.predict(X_pred)

input = pd.read_json(sys.argv[1], orient='index').T
model, features, target = joblib.load("./saved_models/predict.pkl")


prediction = model.predict(input).tolist()

print(json.dumps(prediction))
sys.stdout.flush()