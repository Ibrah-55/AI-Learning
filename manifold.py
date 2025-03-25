from sklearn.manifold import Isomap
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
digits = load_digits()
iso = Isomap(n_components=2)

iso.fit(digits.data)
data_projected = iso.transform(digits.data)
plt.scatter(data_projected[:, 0], data_projected[:, 1], c=digits.target,
            edgecolor='none', alpha=0.5,
            cmap=plt.cm.get_cmap('Purples', 10))
plt.colorbar(label='digit label', ticks=range(10))
plt.clim(-0.5, 9.5)
plt.show()