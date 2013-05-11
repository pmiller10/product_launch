import re

class Product(object):

    train_file = "/home/ubuntu/product_launch/data/train.csv"
    test_file = "/home/ubuntu/product_launch/data/test.csv"

    @classmethod
    def data(self, data_file=train_file):
        f = file(data_file, 'r')
        lines = f.readlines()[1:] # remove header
        lines = [re.sub("\r\n", '', line).split(',') for line in lines]
        targets = []
        products = []
        product = []
        for i,line in enumerate(lines):
            if (i+1) % 26 == 0:
                targets.append(float(line[4]))
                p = [float(x) for x in product]
                products.append(p)
                product = []

            if (i+1) % 26 != 0:
                stores = line[3]
                total_sold = line[4]
                distinct = line[5]
                distinct_repeat = line[6]

                product.append(stores)
                product.append(total_sold)
                product.append(distinct)
                product.append(distinct_repeat)

        return products, targets
