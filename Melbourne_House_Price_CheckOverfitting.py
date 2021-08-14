
import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor


# Function to find the optimal tree-size to avoid over/under fitting
def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return(mae)
	
	


# Path of the file to read
iowa_file_path = '../home_data_train.csv'
home_data = pd.read_csv(iowa_file_path)

# Trget object 
y = home_data.SalePrice

# Define Features
features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = home_data[features]

# Split into test and training Sets
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)


candidate_max_leaf_nodes = [5, 25, 50, 100, 250, 500]

mae_dict={}

for leaf_node in candidate_max_leaf_nodes:
    mae_dict[leaf_node] = get_mae(leaf_node,train_X, val_X, train_y, val_y)
    

best_tree = [key for key in mae_dict if mae_dict[key] == min(mae_dict.values())]
best_tree_size = best_tree[0]

#-----------------start: Suggested Solution-------------------
# scores = {leaf_size: get_mae(leaf_size, train_X, val_X, train_y, val_y) for leaf_size in candidate_max_leaf_nodes}
# best_tree_size = min(scores, key=scores.get)
#-----------------end: Suggested Solution-------------------

# Define model with optimal size 
final_model = DecisionTreeRegressor(max_leaf_nodes=best_tree_size,random_state=0)

# Fit Model
final_model.fit(train_X, train_y)

# Make validation predictions and calculate mean absolute error
val_predictions = final_model.predict(val_X)
val_mae = mean_absolute_error(val_predictions, val_y)
print("Validation MAE: {:,.0f}".format(val_mae))


