print("ALLAH, Muhammad SAW")
# import seaborn as sns
# import matplotlib.pyplot as plt
# sns.set_theme(style="ticks", color_codes=True)
# titanic=sns.load_dataset("titanic")
# print(titanic)
# sns.catplot(x="sex", y="survived", hue="class", kind="bar", data=titanic)
# plt.show()
#!!!!!
# Step involved in data visualization
# Step-1 import liberaries
import seaborn as sns 
import matplotlib.pyplot as plt   
# step-2 set a theme
sns.set_theme(style="ticks", color_codes=True)
# step-3 import data set
kashti= sns.load_dataset("titanic")
#print(kashti)
#step-4 plot basic graph with 1 variable
p= sns.countplot(x="sex", data=kashti)
plt.show()
# step-5 plot basic graph with 2 variable with titles
p= sns.countplot(x="sex", data=kashti, hue="class")
p.set_title("basic count plot for kashthi")
plt.show()

