from sklearn.linear_model import LinearRegression

class MyLinearRegression():

    def __init__(self):
        self.model = LinearRegression()

    def fit(self, data, targets):
        self.model.fit(data, targets)

    def predict(self, data, stores):
        pred = self.model.predict(data)
        #print pred, ' for ', data
        return [pred * stores]
