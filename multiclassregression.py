import numpy as np


# x = [[7.0, 0.27, 0.36, 20.7, 0.045, 45.0, 170.0, 1.001, 3.0, 0.45, 8.8],
#      [6.3, 0.3, 0.34, 1.6, 0.049, 14.0, 132.0, 0.994, 3.3, 0.49, 9.5],
#      [8.1, 0.28, 0.4, 6.9, 0.05, 30.0, 97.0, 0.9951, 3.26, 0.44, 10.1],
#      [7.2, 0.23, 0.32, 8.5, 0.058, 47.0, 186.0, 0.9956, 3.19, 0.4, 9.9],
#      [6.6, 0.16, 0.4, 1.5, 0.044, 48, 143, 0.9912, 3.54, 0.52, 12.4],
#      [8.1, 0.28, 0.4, 6.9, 0.05, 30, 97, 0.9951, 3.26, 0.44, 10.1],
#      [6.2, 0.32, 0.16, 7, 0.045, 30, 136, 0.9949, 3.18, 0.47, 9.6],
#      [7, 0.27, 0.36, 20.7, 0.045, 45, 170, 1.001, 3, 0.45, 8.8],
#      [6.3, 0.3, 0.34, 1.6, 0.049, 14, 132, 0.994, 3.3, 0.49, 9.5],
#      [8.1, 0.22, 0.43, 1.5, 0.044, 28, 129, 0.9938, 3.22, 0.45, 11]]
# y = [6, 6, 6, 6, 7, 6, 6, 6, s6, 6]




# print(len(x))

data = open("E:\winequality-white.csv", "r")
x = []
y = []
for count in data:
    u = count.split(';')[:11]
    v = count.split(';')[11]
    y.append(float(v))
    temp = []
    for count1 in range(0, len(u)):
        u[count1] = float(u[count1])
        temp.append(u[count1])
    x.append(temp)


def loss(x, y, w):
    s = 0
    for i in range(len(x)):
        s += (y[i] - fx(x[i], w)) ** 2
    return s / (2 * len(x))


def fx(x, w):
    return (w[0] * x[0]) + (w[1] * x[1]) + (w[2] * x[2]) + (w[3] * x[3]) + (w[4] * x[4]) + (w[5] * x[5]) + (w[6] * x[6]) + (w[7] * x[7]) + (w[8] * x[8]) + (w[9] * x[9]) + (w[10] * x[10]) + w[11]


def sigmoid(x):
    return 1 / (1 + (1 / np.exp(x)))


def derivative(x, y, w):
    s1 = 0
    s2 = 0
    s3 = 0
    s4 = 0
    s5 = 0
    s6 = 0
    s7 = 0
    s8 = 0
    s9 = 0
    s10 = 0
    s11 = 0
    s12 = 0
    for i in range(len(x)):
        s1 += (fx(x[i], w) - y[i]) * x[i][0]
        s2 += (fx(x[i], w) - y[i]) * x[i][1]
        s3 += (fx(x[i], w) - y[i]) * x[i][2]
        s4 += (fx(x[i], w) - y[i]) * x[i][3]
        s5 += (fx(x[i], w) - y[i]) * x[i][4]
        s6 += (fx(x[i], w) - y[i]) * x[i][5]
        s7 += (fx(x[i], w) - y[i]) * x[i][6]
        s8 += (fx(x[i], w) - y[i]) * x[i][7]
        s9 += (fx(x[i], w) - y[i]) * x[i][8]
        s10 += (fx(x[i], w) - y[i]) * x[i][9]
        s11 += (fx(x[i], w) - y[i]) * x[i][10]
        s12 += (fx(x[i], w) - y[i])
    return (s1 * w[0]) / len(x), (s2 * w[1]) / len(x), (s3 * w[2]) / len(x), (s4 * w[3]) / len(x), (s5 * w[4]) / len(x), (s6 * w[5]) / len(x), (s7 * w[6]) / len(x), (s8 * w[7]) / len(x), (s9 * w[8]) / len(x), (s10 * w[9]) / len(x), (s11 * w[10]) / len(x), s12 / len(x)


epoch = 780
learning_rate = 0.00003
w = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
los_old = 0
for i in range(epoch):
    los = loss(x, y, w)
    # print('#', i, 'loss = ', los)
    if los > (los_old + 0.0001) and i > 0:
        break
    los_old = los
    a, b, c, d, e, f, g, h, j, k, l, m = derivative(x, y, w)
    w[0] = w[0] - a * learning_rate
    w[1] = w[1] - b * learning_rate
    w[2] = w[2] - c * learning_rate
    w[3] = w[3] - d * learning_rate
    w[4] = w[4] - e * learning_rate
    w[5] = w[5] - f * learning_rate
    w[6] = w[6] - g * learning_rate
    w[7] = w[7] - h * learning_rate
    w[8] = w[8] - j * learning_rate
    w[9] = w[9] - k * learning_rate
    w[10] = w[10] - l * learning_rate
    w[11] = w[11] - m * learning_rate

predict_y = fx([7.6,0.67,0.14,1.5,0.074,25,168,0.9937,3.05,0.51,9.3], w)
probability = sigmoid(predict_y)
print('x = [7.6,0.67,0.14,1.5,0.074,25,168,0.9937,3.05,0.51,9.3] <=> y =',
      predict_y, '|Probability =',  probability)
# expect 5
