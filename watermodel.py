import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle

def main():
    df = pd.read_csv("WaterData.csv")

    #use required features
    cdf = df[['Type', 'AirTemp', 'WaterTemp', 'RawPh', 'SettledPh', 'RawTurb', 'DetentionTimeGPM', 'SolidsRemoved', 'Dosage']]
    # print(cdf.describe())
    # #Training data and predictor variable
    # #Use all data for training (train-test-split not used)
    X = cdf.iloc[:, :8].values
    y = cdf.iloc[:, -1].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    regressor = LinearRegression()

    regressor.fit(X_train, y_train)

    # print(regressor.intercept_)

    y_pred = regressor.predict(X_test)

    d = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
    print(d)

    res = input("Load or Dump?")
    if res == 'Load' or 'load':
        # #Saving model to current directory
        # #Pickle serializes objects so they can be saved to file, and loaded into prgram again
        pickle.dump(regressor, open('watermodel.pkl', 'wb'))
        print('Water mode loaded into watermodel.pkl')
        res2 = input("Dump?")
        if res2 == 'yes' or 'y' or 'Yes' or 'dump' or 'Dump':
            model = pickle.load(open('watermodel.pkl', 'rb'))
            print(model.predict([[1, 66, 60, 7.84, 7.66, 0.66, 555, 0.90]]))
    elif res == 'Dump' or 'dump':
        model = pickle.load(open('watermodel.pkl', 'rb'))
        print(model.predict([[1, 75, 66, 7.5, 7.2, 1.0, 555, 0.90]]))
    else:
        print('Learn to fucking spell')

if __name__ == '__main__':
    main()