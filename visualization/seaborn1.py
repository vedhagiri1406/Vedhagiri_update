import seaborn as sns
import matplotlib.pyplot as plt

# dataset load
df = sns.load_dataset("iris")
print(df)
# scatterplot
sns.scatterplot(x="sepal_width", y="petal_width", data=df, hue="species")
plt.show()
