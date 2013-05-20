from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, ExtraTreesRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from net import Net

class BaseRegression():

    def fit(self, data, targets):
        self.model.fit(data, targets)

    def predict(self, data, stores):
        pred = self.model.predict(data)
        #print pred, ' for ', data
        return pred * stores

class MyLinearRegression(BaseRegression):

    def __init__(self):
        self.model = LinearRegression()

    def predict(self, data, stores):
        pred = self.model.predict(data)
        #print pred, ' for ', data
        return [pred * stores]

class MyNet(BaseRegression):

    #def __init__(self):
        #self.model = RandomForestRegressor(n_estimators=20)

    def fit(self, data, targets, epochs=2):
        self.model = Net(data, targets, epochs=2)

class MyExtra(BaseRegression):
    def __init__(self):
        self.model = ExtraTreesRegressor(compute_importances=True, n_estimators=20) # score 0.37 #TODO best without scaling

class MySVR(BaseRegression):
    def __init__(self):
        self.model = SVR()

class MyNeigh(BaseRegression):
    def __init__(self):
        self.model = KNeighborsRegressor()
