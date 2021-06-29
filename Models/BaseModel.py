from sklearn.base import BaseEstimator
from numpy import ndarray


class BaseModel(BaseEstimator):
    def __init__(self):
        pass

    def set_params(self, **params):
        for param, value in params:
            setattr(self, param, value)

    def get_params(self, deep: bool = True):
        return {}

    def clone(self):
        instance = self.__class__()
        instance.set_params(**self.get_params())
        return instance

    def fit(self, x, y=None):
        pass

    def predict(self, x: ndarray) -> ndarray:
        pass
