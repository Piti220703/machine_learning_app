import sys
import json
import ast
import pandas as pd
import joblib

features, target = joblib.load("./saved_models/infor.pkl")

print(json.dumps(features))

sys.stdout.flush()