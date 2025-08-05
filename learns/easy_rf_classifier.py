# simplest random-forest classifier
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(random_state=0)
X = [[1, 2, 3],
     [11, 12, 13]]
y = [0, 1]
clf.fit(X, y)

# a = clf.predict(X)
# print(a)
# b = clf.predict([[4, 5, 6], [14, 15, 16]])
# print(b)
# c = clf.predict([[17, 18, 19], [2, 3, 4]])
# print(c)
d = clf.predict([[9, 31, 1], [11, 21, 13]])
print(d)