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
            stores = line[3]
            total_sold = line[4]
            distinct = line[5]
            distinct_repeat = line[6]
            product.append(stores) # we know this for all weeks

            if (i+1) % 26 == 0:
                total_sold = line[4]
                targets.append(float(total_sold))

                p = [float(x) for x in product]
                products.append(p)
                product = []

            if (i+1) % 26 != 0:
                product.append(total_sold)
                product.append(distinct)
                product.append(distinct_repeat)

        return products, targets

    @classmethod
    def data_like_test(self, data_file=train_file, ids=False):
        f = file(data_file, 'r')
        lines = f.readlines()[1:] # remove header
        lines = [re.sub("\r\n", '', line).split(',') for line in lines]
        targets = []
        products = []
        product = []
        product_ids = []
        test_weeks = range(14,27)
        week = 0
        for i,line in enumerate(lines):
            week += 1

            stores = line[3]
            product.append(stores) # we know this for all weeks

            if week not in test_weeks:
                total_sold = line[4]
                distinct = line[5]
                distinct_repeat = line[6]
                units_per_store = float(total_sold)/float(stores)
                percent_repeat = float(distinct_repeat)/float(distinct)

                product.append(total_sold)
                product.append(distinct)
                product.append(distinct_repeat)
                product.append(units_per_store)
                product.append(percent_repeat) # this only gives a small boost in ExtraTrees
            elif week == 26:
                if ids:
                    product_id = line[0]
                    product_ids.append(product_id)
                targets.append(float(total_sold))
                p = [float(x) for x in product]
                products.append(p)
                product = []
                week = 0

        if ids:
            return products, targets, product_ids
        else:
            return products, targets

    @classmethod
    def data_for_units_per_store(self, data_file=train_file, ids=False):
        f = file(data_file, 'r')
        lines = f.readlines()[1:] # remove header
        lines = [re.sub("\r\n", '', line).split(',') for line in lines]
        targets = []
        products = []
        product = []
        product_ids = []
        stores = []
        test_weeks = range(14,27)
        week = 0
        wk1_stores = 0
        wk6_stores = 0
        wk13_stores = 0
        wk26_stores = 0
        us1 = 0
        us6 = 0
        us13 = 0
        for i,line in enumerate(lines):
            week += 1

            if week == 1:
                wk1_stores = float(line[3])
                total_sold = float(line[4])
                us1 = total_sold/wk1_stores
            elif week == 6:
                wk6_stores = float(line[3])
                total_sold = float(line[4])
                us6 = total_sold/wk6_stores
            elif week == 13:
                wk13_stores = float(line[3])
                total_sold = float(line[4])
                us13 = total_sold/wk13_stores
            elif week == 26:
                wk26_stores = float(line[3])
                
                if not ids:
                    total_sold = float(line[4])
                    us26 = total_sold/wk26_stores
                    targets.append(us26)

                delta_stores = wk26_stores/wk13_stores
                delta_us_1_13 = us1/us13
                delta_us_6_13 = us6/us13
                product = [delta_us_1_13, delta_us_6_13, us13, delta_stores] 
                products.append(product)
                stores.append(wk26_stores)

                #distinct = line[5]
                #distinct_repeat = line[6]
                #percent_repeat = float(distinct_repeat)/float(distinct)

                if ids:
                    product_id = line[0]
                    product_ids.append(product_id)
                week = 0
        if ids:
            return products, targets, stores, product_ids
        else:
            return products, targets, stores
