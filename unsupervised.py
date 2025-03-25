from sklearn.decomposition import PCA
model  = PCA(n_components=2)
model.fit(X_iris)
X_2D = model.transform(X_iris)
iris['PCA1'] = X_2D[:, 0]   
iris['PCA2'] = X_2D[:, 1]   
sns.lmplot("PCA1", "PCA2", hue='species', data=iris, fit_reg=False)
plt.show()