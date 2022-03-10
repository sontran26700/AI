import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("E:\portland_price.txt", dtype=np.float64, delimiter=",")

X = data[::,0:2]
y = data[::,-1:]
#print(X)
# #Plot Size and Price
# plt.figure(figsize = (15,4), dpi = 100)
# plt.subplot(121)
# plt.scatter(X[::,0],y)
# plt.xlabel("Size of house (X1)")
# plt.ylabel("Price of house (Y)")

# #Plot no.bed and price
# plt.subplot(122)
# plt.scatter(X[::,1],y)
# plt.xlabel("Number of bedroom (X2)")
# plt.ylabel("Price of house (Y)")
# plt.show()

#Add bias into X
m,n = X.shape
X_bias = np.ones((m,n+1))
X_bias[::,1:] = X
# #print(X_bias[0:5,::])

# introduce weights of hypothesis (randomly initialize)
theta = np.random.rand(1,3)
#print(X_bias[::,1:2])

#feature scaling
mean_size = np.mean(X_bias[::,1:2])
mean_bedroom = np.mean(X_bias[::,2:])
size_std = np.std(X_bias[::,1:2])
bedroom_std = np.std(X_bias[::,2:])
X_bias[::,1:2] = (X_bias[::,1:2] - mean_size)/ (size_std) 
X_bias[::,2:] = (X_bias[::,2:] - mean_bedroom)/ (bedroom_std)
X_bias[0:5,::]
#print(X_bias[::,2:])

def cal_cost(X_bias, y, theta):
	m, n = X.shape
	hypothesis = X_bias.dot(theta.transpose())
	cost = (1/(2*m)) * np.sum(np.square(hypothesis - y), axis=0)
	return cost
	
	
def gradientDescent(X_bias,y,theta,iterations,alpha):

	cost_log = np.array([])
	for i in range(0,iterations):
		hypothesis = X_bias.dot(theta.transpose())
		temp0 = theta[0,0] - alpha*(1.0/m)*((hypothesis-y)*(X_bias[::,0:1])).sum(axis=0)
		temp1 = theta[0,1] - alpha*(1.0/m)*((hypothesis-y)*(X_bias[::,1:2])).sum(axis=0)
		temp2 = theta[0,2] - alpha*(1.0/m)*((hypothesis-y)*(X_bias[::,-1:])).sum(axis=0)
		theta[0,0] = temp0
		theta[0,1] = temp1
		theta[0,2] = temp2
		cost_log = np.append(cost_log,cal_cost(X_bias,y,theta))

	plt.plot(np.linspace(1,iterations,iterations,endpoint=True),cost_log)
	plt.title("Iteration vs Cost graph ")
	plt.xlabel("Number of iteration")
	plt.ylabel("Cost of Theta")
	plt.show()
	return theta
	
alpha = 0.3
iterations = 100
theta = gradientDescent(X_bias,y,theta,iterations,alpha)
print(theta)

# predict the price of a house with 1650 square feet and 3 bedrooms
# add bias unit 1.0
X_predict = np.array([1.0,1650.0,3]) 
#feature scaling the data first
X_predict[1] = (X_predict[1] - mean_size)/ (size_std) 
X_predict[2] = (X_predict[2]- mean_bedroom)/ (bedroom_std)
hypothesis = X_predict.dot(theta.transpose())
print("Cost of house with 1650 sq ft and 3 bedroom is ",hypothesis)