import pandas as pd 
from sklearn.linear_model import LinearRegression
import pickle

df = pd.read_csv("FuelConsumption.csv")

stuff = df.describe()
print(stuff)
#use required features
cdf = df[['ENGINESIZE', 'CYLINDERS', "FUELCONSUMPTION_COMB", "CO2EMISSIONS"]]

#Training data and predictor variable
#Use all data for training (train-test-split not used)
x = cdf.iloc[:, :3]
y = cdf.iloc[:, -1]
regressor = LinearRegression()

regressor.fit(x, y)

#Saving model to current directory
#Pickle serializes objects so they can be saved to file, and loaded into prgram again
# pickle.dump(regressor, open('model.pkl', 'wb'))

model = pickle.load(open('model.pkl', 'rb'))
print(model.predict([[2.6, 8, 10.1]]))
