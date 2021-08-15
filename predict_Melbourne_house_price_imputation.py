import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.impute import SimpleImputer


# Read the data
X_full = pd.read_csv('../data/train.csv', index_col='Id')
X_test_full = pd.read_csv('../data/test.csv', index_col='Id')

# Remove rows with missing target, separate target from predictors
X_full.dropna(axis=0, subset=['SalePrice'], inplace=True)
y = X_full.SalePrice
X_full.drop(['SalePrice'], axis=1, inplace=True)

# To keep things simple, just use numerical predictors
X = X_full.select_dtypes(exclude=['object'])
X_test = X_test_full.select_dtypes(exclude=['object'])

# Break off validation set from training data
X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2,
                                                      random_state=0)
													  
# Shape of training data (num_rows, num_columns)
print(X_train.shape)

# Number of missing values in each column of training data
missing_val_count_by_column = (X_train.isnull().sum())
print(missing_val_count_by_column[missing_val_count_by_column > 0])

# How many rows are in the training data?
num_rows = X_train.shape[0]
print(num_rows)

# How many columns in the training data have missing values?
num_cols_with_missing = (missing_val_count_by_column[missing_val_count_by_column > 0].shape[0])
print(num_cols_with_missing)

# How many missing entries are contained in all of the training data?
tot_missing = ((missing_val_count_by_column[missing_val_count_by_column > 0]).sum())
print(tot_missing)

#=================== Imputation =================
# Preprocessed training and validation features
final_imputer = SimpleImputer()
final_X_train = pd.DataFrame(final_imputer.fit_transform(X_train))
final_X_valid = pd.DataFrame(final_imputer.transform(X_valid))

# Fill in the line below: preprocess test data
final_X_test = pd.DataFrame(final_imputer.transform(X_test))


# imputation removed column names; put them back
final_X_train.columns = X_train.columns
final_X_valid.columns = X_valid.columns
final_X_test.columns = X_test.columns

# Define and fit model
model = RandomForestRegressor(n_estimators=100, random_state=0)
model.fit(final_X_train, y_train)

#===================== Calculate MAE

# Get validation predictions and MAE
preds_valid = model.predict(final_X_valid)
print("MAE (Your approach):")
print(mean_absolute_error(y_valid, preds_valid))

# get test predictions
preds_test = model.predict(final_X_test)
print("MAE (Your approach):")
print(mean_absolute_error(y_valid, preds_test))

#=================== save test predictions to file
output = pd.DataFrame({'Id': X_test.index,
                       'SalePrice': preds_test})
output.to_csv('submission.csv', index=False)
