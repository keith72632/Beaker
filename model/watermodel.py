import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle

df = pd.read_csv("WaterData.csv")

#how to get row with columns of certain values: f.loc[df['column_name'] == some_value]
#use required features
cdf = df[['Type', 'AirTemp', 'WaterTemp', 'RawPh', 'SettledPh', 'RawTurb', 'MixerSpeed', 'DetentionTimeGPM', 'SolidsRemoved', 'Dosage']]
   
# #Training data and predictor variable
# #Use all data for training (train-test-split not used)
X = cdf.iloc[:, :9].values
y = cdf.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

regressor = LinearRegression()

regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

d = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})

   
# #Saving model to current directory
# #Pickle serializes objects so they can be saved to file, and loaded into prgram again
pickle.dump(regressor, open('watermodel.pkl', 'wb'))
print('Water mode loaded into watermodel.pkl')
            
# model = pickle.load(open('watermodel.pkl', 'rb'))
# print(model.predict([[1, 66, 60, 7.84, 7.66, 0.66, 30, 555, 0.90]]))

