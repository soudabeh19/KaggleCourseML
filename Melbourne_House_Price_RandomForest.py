import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


# File Path to read
iowa_file_path = '../home_data_train.csv'
home_data = pd.read_csv(iowa_file_path)


y = home_data.SalePrice

features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = home_data[features]

# Split into test and training Sets
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

# Specify Model
rf_model = RandomForestRegressor(random_state=1)

# Fit model
rf_model.fit(train_X, train_y)

# Calculate the mean absolute error of the Random Forest model on the test set
val_predictions = rf_model.predict(val_X)
rf_val_mae = mean_absolute_error(val_y,val_predictions)

print("Validation MAE for Random Forest Model: {}".format(rf_val_mae))