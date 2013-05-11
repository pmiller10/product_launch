from dal.product import Product
from product_preprocess import ProductPreprocess
from models.classifier import Classifier
from postprocess import ProductPostprocess
import score
import time

start = time.time()
# preprocessing
train, targets = Product.data_like_test()
test_data, x, product_ids = Product.data_like_test(data_file="/home/ubuntu/product_launch/data/test.csv", ids=True)
#x = Product.data_like_test(data_file="/home/ubuntu/product_launch/data/test.csv", ids=True)


#print train[0]
#print len(train[0])
#print len(train[10])
#print len(train[100])
#print targets[0]
#print len(train)
#print len(train_targets)
#print len(cv)



# classify
preds = Classifier.preds(train, targets, test_data)
preds = ProductPostprocess.nonnegatives(preds)
ProductPostprocess.submit(preds, product_ids)



print "duration: ", time.time() - start
