class ProductPostprocess():

    @classmethod
    def nonnegatives(self, data):
        positives = []
        for d in data:
            if d >= 0:
                positives.append(d)
            else:
                positives.append(0)
        return positives

    @classmethod
    def submit(self, preds, ids):
        f = file("data/submission3.csv", 'w+')
        header = "Product_Launch_Id,Weeks_Since_Launch,Units_that_sold_that_week\n"
        f.write(header)

        for i,p in enumerate(preds):
            product_id = ids[i]
            f.write(str(product_id) + ',' + '26' + ',' + str(p[0]) + "\n")
        f.close()
