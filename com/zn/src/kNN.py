from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt


def create_data_set():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels


def classify0(in_x, data_set, lables, k):
    data_set_size = data_set.shape[0]
    diff_mat = tile(in_x, (data_set_size, 1)) - data_set
    square_diff_mat = diff_mat ** 2
    square_dis = square_diff_mat.sum(axis=1)
    distances = square_dis ** 0.5
    sorted_dis_indicies = distances.argsort()
    lable_count = {}
    for i in range(k):
        lable = lables[sorted_dis_indicies[i]]
        lable_count[lable] = lable_count.get(lable, 0) + 1
    sorted_lable_count = sorted(lable_count.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sorted_lable_count[0][0]


def file2matrix(filename):
    handle = open(filename)
    line_num = len(handle.readlines())
    return_matrix = zeros((line_num, 3))
    label_vector = []
    index = 0
    handle = open(filename)
    for line in handle.readlines():
        line = line.strip()
        line_data = line.split('\t')
        return_matrix[index, :] = line_data[0:3]
        label_vector.append(int(line_data[-1]))
        index += 1
    return return_matrix, label_vector

def plot(data):
    fig = plt.figure()
    ax = fig.add_subplot(111)

