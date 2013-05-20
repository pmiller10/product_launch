import math


# root mean square logarithmic error
def rmsle(preds, targets):
    if len(preds) != len(targets):
        raise Exception("The number of prediction and targets must be the same")
    total = 0.
    for i,p in enumerate(preds):
        t = targets[i]
        total += (math.log(p[0] + 1) - math.log(t + 1)) ** 2
    avg = total/len(preds)
    return math.sqrt(avg)
