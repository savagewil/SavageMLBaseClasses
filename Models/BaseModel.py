from sklearn.base import BaseEstimator


class BaseModel(BaseEstimator):
    def __init__(self):
        pass

    def set_params(self, **params):
        pass

    def get_params(self, deep=True):
        pass

    def clone(self):
        pass

    def fit(self, x, y=None):
        pass

    def predict(self, x):
        pass