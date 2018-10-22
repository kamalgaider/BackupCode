import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVR

dates =[]
prices=[]

def get_data(filename):
	with open(filename, 'r') as csvfile:
		ireader = csv.reader(csvfile)
		next(csvfile)# to remove headers from CSV file

		#append dates & prices from csv to lists
		for row in ireader:
			dates.append(int(row[0].split('-')[0]))
			prices.append(float(row[1]))

def predict_prices(dates, prices, dtp) :
	
	# convert list to 1-D array ( list, (rows, column))
	dates = np.reshape(dates, (len(dates), 1))
	
	#Create 3 different Support Vector Regression models
	svr_lin = SVR(kernel ='linear', C =1e3)# 1e3 = 1000
	svr_poly = SVR(kernel ='poly', C =1e3, degree =2)
	svr_rbf = SVR(kernel ='rbf', C =1e3, gamma =0.1)

	#Train models
	svr_lin.fit(dates,prices)
	svr_poly.fit(dates,prices)
	svr_rbf.fit(dates,prices)

	#Plot graph for the training data
	plt.scatter(dates,prices, color ='black', label = 'Data')
	
	plt.plot(dates, svr_lin.predict(dates), color='green', label = 'Linear model')
	plt.plot(dates, svr_poly.predict(dates), color='blue', label = 'Polynomial model')
	plt.plot(dates, svr_rbf.predict(dates), color='red', label = 'RBF model')

	plt.xlabel('Date')
	plt.ylabel('Price')
	plt.title('Support Vector Regression')
	plt.legend()
	plt.show()

	#Print predicted prices
	for i in range(len(dtp)):
		print("Price predictions on {}: ".format(dtp[i]),svr_rbf.predict(dtp)[i], 
			svr_lin.predict(dtp)[i], svr_poly.predict(dtp)[i])

get_data('AAPL.csv')
dates_to_predict = np.reshape([23,24,25,26,27], (5, 1))#dates to predict prices for
predicted_price= predict_prices(dates,prices, dates_to_predict)
