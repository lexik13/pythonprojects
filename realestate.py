"""
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
import pandas as pd

Displays data types of each column:
df = pd.read_csv('kc house sales.csv')
print(df.dtypes)

Drops column then prints statistical summary:
df = pd.read_csv('kc house sales.csv')
df_drop = df.drop(['Unnamed: 0', 'id'], axis=1)
df.describe()
print(df.describe())

Counts unique column values then coverts it to a data frame:
count = df['floors'].value_counts()
count_df = count.to_frame()
print(count_df)


Produces a box plot w/ two attributes for outlier comparison:
df['waterfront'] = df['waterfront'].map({0: 'Non-Waterfront', 1: 'Waterfront'})
sns.boxplot(x='waterfront', y='price', data=df)
plt.ylim(1, 2500000)
plt.xlabel('Waterfront View')
plt.ylabel('Price')
plt.show()

Fitting a linear regression model & calculate r^2
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

X = df[['sqft_living']]
y = df['price']
lm = LinearRegression()
lm.fit(X, y)
y_pred = lm.predict(X)

r2 = r2_score(y, y_pred)
print(r2)

Creates a pipeline object for prediction, fits the object using 'features' then calculates r^2:

df = pd.read_csv('kc house sales.csv')
features =["floors", "waterfront","lat" ,"bedrooms" ,"sqft_basement" ,"view" ,"bathrooms","sqft_living15","sqft_above","grade","sqft_living"]
Input=[('scale',StandardScaler()),('polynomial', PolynomialFeatures(include_bias=False)),('model',LinearRegression())]
pipe = Pipeline(Input)

x = df[features]
y = df['price']
x = x.dropna()
y = y[x.index]
pipe.fit(x,y)
ypipe = pipe.predict(x)
lm = LinearRegression()
lm.fit(x, y)
y_pred = lm.predict(x)
r2 = r2_score(y, y_pred)
print(r2)

Fits a Ridge regression object using the training data, setting the regularization parameter to 0.1, and calculates the R^2 using the test data:

features =["floors", "waterfront","lat" ,"bedrooms" ,"sqft_basement" ,"view" ,"bathrooms","sqft_living15","sqft_above","grade","sqft_living"]
X = df[features]
Y = df['price']

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.15, random_state=1)

pr= PolynomialFeatures(degree=2)
ridge = Ridge(alpha=0.1)

x_train_poly = pr.fit_transform(x_train)
x_test_poly = pr.transform(x_test)

ridge.fit(x_train_poly, y_train)

y_pred = ridge.predict(x_test_poly)
r2 = r2_score(y_test, y_pred)

df = pd.read_csv('kc house sales.csv')
df = df.dropna()

features = ["floors", "waterfront", "lat", "bedrooms", "sqft_basement", "view", "bathrooms", "sqft_living15", "sqft_above", "grade", "sqft_living"]
X = df[features]
Y = df['price']

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.15, random_state=1)

pr = PolynomialFeatures(degree=2)

x_train_poly = pr.fit_transform(x_train)
x_test_poly = pr.transform(x_test)

ridge = Ridge(alpha=0.1)
ridge.fit(x_train_poly, y_train)

y_pred = ridge.predict(x_test_poly)

r2 = r2_score(y_test, y_pred)
print(r2)


"""












