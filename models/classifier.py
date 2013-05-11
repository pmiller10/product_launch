# sklearn
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, ExtraTreesRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR

from net import Net
from lin_reg import MyLinearRegression

class Classifier(object):

    @classmethod
    def preds(self, data, targets, cv, stores):
        #model = LinearRegression()
        model = MyLinearRegression()
        #model = SVR()
        #model = KNeighborsRegressor(weights='distance', n_neighbors=5, p=1, leaf_size=30) # score 0.75
        #model = RandomForestRegressor() # score 0.390
        #model = ExtraTreesRegressor(compute_importances=True, n_estimators=40) # score 0.37 #TODO best without scaling
        #model = GradientBoostingRegressor() # 0.628
        #model = Net(data, targets, epochs=100)
        
        print model
        model.fit(data, targets)

        #preds = [model.predict(c) for c in cv]
        #models, weights = self.train(data, targets, cv)
        #preds = self.vote(models, cv, weights)
        preds = []
        for i,c in enumerate(cv):
            s = stores[i]
            p = model.predict(c, s)
            preds.append(p)
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
