from sklearn.preprocessing import StandardScaler
X= [[0, 15],
    [1, -10]]

a = StandardScaler().fit(X).transform(X)
print(a)