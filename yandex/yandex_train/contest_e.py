import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression


with open('input.txt') as f:
    train_data = [list(map(float, f.readline().split())) for i in range(1000)]
    train_df = pd.DataFrame(train_data, columns=[
        'x1', 'x2', 'x3', 'x4', 'x5', 'y'])

    test_data = [list(map(float, f.readline().split())) for i in range(1000)]
    test_df = pd.DataFrame(test_data, columns=['x1', 'x2', 'x3', 'x4', 'x5'])

X, y = train_df[['x1', 'x2', 'x3', 'x4', 'x5']], train_df['y']

poly = PolynomialFeatures(degree=2, include_bias=False)
poly_features = poly.fit_transform(X)

poly_reg_model = LinearRegression()
poly_reg_model.fit(X, y)

poly_reg_y_predicted = poly_reg_model.predict(test_df)

for val in poly_reg_y_predicted:
    print(val)
