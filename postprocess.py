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
