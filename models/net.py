from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure import SigmoidLayer, SoftmaxLayer, TanhLayer, LinearLayer

class Net():

    def __init__(self, data, targets, epochs):
        ds = SupervisedDataSet(len(data[0]), 1)
        for i,d in enumerate(data):
            t = float(targets[i])
            ds.addSample(d, t)
        
        net = buildNetwork(len(data[0]), 10, 5, 1, hiddenclass=TanhLayer, outclass=LinearLayer)
        print net
        trainer = BackpropTrainer(net, ds, momentum=0.4)
        trainer.trainUntilConvergence(maxEpochs=epochs, verbose=True)
        #for i in range(epochs):
            #print trainer.train()
        self.model = net

    def predict(self, data):
        pred = self.model.activate(data)
        return pred

    def fit(self, data, targets):
        pass
