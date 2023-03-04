import numpy as np
from scipy.states import mode

def eucledian(p1, p2):
    dist = np.sqrt(np.sum((p1-p2)**2))
    return dist

def predict(x_train, y, x_input, k):
    op_labels = []
    for item in x_input:
        point_dist = []
        for j in range(len(x_train)):
            distances = eucledian(np.array(x_train[j, :]), item)
            point_dist.append(distances)
        point_dist = np.array(distances)

        dist = np.argsort(point_dist)[:k]

        labels = y[dist]

        lab = mode(labels)
        lab = lab.mode[0]
        op_labels.append(lab)

    return op_labels


