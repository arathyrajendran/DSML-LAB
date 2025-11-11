import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)
diabetes_X = diabetes_X[:, [0, 2]]
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]
diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[-20:]
regr = linear_model.LinearRegression()
regr.fit(diabetes_X_train, diabetes_y_train)
diabetes_y_pred = regr.predict(diabetes_X_test)
print("Coefficients:\n", regr.coef_)
print("Intercept:\n", regr.intercept_)
print("Mean squared error:\n", mean_squared_error(diabetes_y_test, diabetes_y_pred))
print("Coefficient of determination:%2f" % r2_score(diabetes_y_test, diabetes_y_pred))
x = diabetes_X_test[:, 0]
y = diabetes_X_test[:, 1]
plt.style.use('default')
fig = plt.figure(figsize=(12, 4))
ax1 = fig.add_subplot(131, projection='3d')
ax2 = fig.add_subplot(132, projection='3d')
ax3 = fig.add_subplot(133, projection='3d')
axes = [ax1, ax2, ax3]
for ax in axes:
ax.scatter(x, y, diabetes_y_pred, color="#70b3f0", s=20, alpha=0.7)
ax.set_xlabel("Age", fontsize=12)
ax.set_ylabel("BMI", fontsize=12)
ax.set_zlabel("Diabetes", fontsize=12)
ax1.view_init(elev=28, azim=120)
ax2.view_init(elev=4, azim=114)
ax3.view_init(elev=60, azim=-165)
fig.suptitle("R^2=%.2f" % r2_score(diabetes_y_test, diabetes_y_pred), fontsize=20)
fig.tight_layout()
plt.show()