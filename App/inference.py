import joblib
import preprocessing as p


def make_prediction(test):
    test = p.fill_missing(test)
    test = p.model_preprocessing(test)
    model = joblib.load("../models/model")
    Final_prediction = model.predict(test)
    return Final_prediction
