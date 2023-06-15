""" print("zia") """
import seaborn as sns
import matplotlib.pyplot as plt
""" kashti=sns.load_dataset('titanic')
print(kashti.head(3)) """
sns.set_theme(style="ticks", color_codes=True)
titanic=sns.load_dataset("titanic")
print(titanic)
#sns.catplot(x="sex", y="survived", hue="class", kind="bar", data=titanic)
g= sns.FacetGrid (titanic, row="sex", hue="alone")
g=(g.map(plt.scatter, "age", "fare").add_legend())
plt.show()
