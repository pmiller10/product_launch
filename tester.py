from dal.product import Product
from product_preprocess import ProductPreprocess
from models.classifier import Classifier
from postprocess import ProductPostprocess
import score
import time

start = time.time()
# preprocessing
data, targets = Product.data()
matrix = ProductPreprocess.to_matrix(data)
matrix = ProductPreprocess.scale(matrix)
data = matrix.tolist()



# split cv and training data
train, cv = data[:1500], data[1500:]
train_targets, cv_targets = targets[:1500], targets[1500:]
print len(train)
print len(train_targets)
print len(cv)



# classify
preds = Classifier.preds(train, train_targets, cv)
preds = ProductPostprocess.nonnegatives(preds)
print preds[:10]
print cv_targets[:10]



# score
print score.rmsle(preds, cv_targets)

print "duration: ", time.time() - start