import seaborn as sns; sns.set()
iris = sns = sns.load_dataset('iris')   

sns.pairplot(iris, hue='species', size=1.5)