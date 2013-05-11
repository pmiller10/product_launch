import numpy as np

# sklearn
from sklearn.linear_model import LinearRegression, SGDClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, ExtraTreesClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

class Classifier(object):

    @classmethod
    def preds(self, data, targets, cv):
        model = LinearRegression()
        model.fit(data, targets)
        preds = [model.predict(c) for c in cv]
        #models, weights = self.train(data, targets, cv)
        #preds = self.vote(models, cv, weights)
        return preds

    @classmethod
    def train(self, data, targets, cv):
        models = []
        weights = []

        models.append(LinearRegression())
        weights.append(1.)

        for m in models:
            m.fit(data, targets)
        return models, weights
