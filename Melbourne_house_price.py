import pandas as pd
file_path = 'C:/Users/Soudabeh/Documents/Job Hunting 2021/learning/KaggleCourseML/melbourne_house_price_data.csv'
home_data = pd.read_csv(file_path)
home_data.describe()