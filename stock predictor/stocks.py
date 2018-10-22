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

def predict_prices(dates, prices, x) :
	
	# make array using (dates list, (length, its order))
	dates = np.reshape(dates, (len(dates), 1))
	
	#Create models
	svr_lin = SVR(kernel ='linear', C =1e3)
	svr_poly = SVR(kernel ='poly', C =1e3, degree =2)
	svr_rbf = SVR(kernel ='rbf', C =1e3, gamma =0.1)

	#Train models
	svr_lin.fit(dates,prices)
	svr_poly.fit(dates,prices)
	svr_rbf.fit(dates,prices)

	plt.scatter(dates,prices, color ='black', label = 'Data')
	
	plt.plot(dates, svr_lin.predict(dates), color='green', label = 'Linear model')
	plt.plot(dates, svr_poly.predict(dates), color='blue', label = 'Polynomial model')
	plt.plot(dates, svr_rbf.predict(dates), color='red', label = 'RBF model')

	plt.xlabel('Date')
	plt.ylabel('Price')
	plt.title('Support Vector Regression')
	plt.legend()
	plt.show()

	return svr_rbf.predict(x)[0], svr_lin.predict(x)[0], svr_poly.predict(x)[0]

get_data('AAPL.csv')
predicted_price= predict_prices(dates,prices,29)
print(predict_prices)
