# Code you have previously used to load data
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# Path of the file to read
iowa_file_path = '../home_data_train.csv'

home_data = pd.read_csv(iowa_file_path)
y = home_data.SalePrice
feature_columns = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = home_data[feature_columns]

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 1)

# define the model
iowa_model = DecisionTreeRegressor(random_state=1)

# Fit iowa_model with the training data.
iowa_model.fit(train_X, train_y)

# Predict with all validation observations
val_predictions = iowa_model.predict(val_X)

# print the top few validation predictions
print(iowa_model.predict(val_X.head()))

# print the top few actual prices from validation data
print(val_y.head())


predict_y = iowa_model.predict(val_X)
val_mae = mean_absolute_error(val_y,predict_y) 


print(val_mae)