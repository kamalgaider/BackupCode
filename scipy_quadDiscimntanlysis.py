from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
#train data on dimensions of TV or mobile, & then predict result of a provided dimensions
o = [[3,4],[4,5],[3,7],[2,5],[14,22],[15,18],[17,30],[16,25]]
i = ['mob','mob','mob','mob','TV','TV','TV','TV']

cfx = QuadraticDiscriminantAnalysis()
cfx= cfx.fit(o,i)
print(cfx.predict([[4,6]]))
