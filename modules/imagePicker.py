import pandas as pd
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
from sklearn.externals import joblib

pt_data = pd.read_csv(r'C:\Users\ajwal\OneDrive\IT\Projekty\Zew Cthulhu\support\ml\data.csv')
X = pt_data.drop(columns=['portret'])
y = pt_data['portret']

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
#
# model = DecisionTreeClassifier()
# # model.fit(X_train, y_train)
# model.fit(X, y)
# joblib.dump(model, 'data.joblib')
model = joblib.load('data.joblib')


def pick_image(lista):
    predictions = model.predict([lista])
    return predictions[0]


# predictions = model.predict(X_test)
# score = accuracy_score(y_test, predictions)
# score
