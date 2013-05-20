from dal.product import Product
from product_preprocess import ProductPreprocess
from models.classifier import Classifier
from postprocess import ProductPostprocess
import score
import time

start = time.time()
# preprocessing
_, total_sold = Product.data_like_test()
train_data, us26, _ = Product.data_for_units_per_store()
test_data, _, week26_stores, product_ids = Product.data_for_units_per_store(data_file="/home/ubuntu/product_launch/data/test.csv", ids=True)

matrix = ProductPreprocess.to_matrix(train_data)
matrix = ProductPreprocess.scale(matrix)
matrix = ProductPreprocess.polynomial(matrix, 2)
data = matrix.tolist()



# split cv and training data
train_total_sold, cv_total_sold = total_sold[:1500], total_sold[1500:]
train_week26_stores, cv_week26_stores = week26_stores[:1500], week26_stores[1500:]
train_us26 = us26[:1500]
print us26[0:10]
print data[0]
#print len(train[0])
#print len(train[10])
#print len(train[100])
#print len(us26)
#print total_sold[0]



# classify
start = time.time()
preds = Classifier.preds(train_data, us26, test_data, week26_stores)
preds = ProductPostprocess.nonnegatives(preds)
ProductPostprocess.submit(preds, product_ids)
print "duration: ", time.time() - start
