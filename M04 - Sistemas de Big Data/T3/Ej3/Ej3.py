import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Cargar dataset
df = pd.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv")

# 2. Histogramas multivariable por especie
plt.figure(figsize=(12,8))
df.hist(column=['sepal_length','sepal_width','petal_length','petal_width'], 
        by=df['species'], figsize=(12,8), layout=(3,4), edgecolor='black')
plt.tight_layout()
plt.savefig("grafico_1.png")
plt.close()


# 3. Pairplot
sns.pairplot(df, hue="species")
plt.savefig("grafico_2.png")
plt.close()


# 4. Heatmap de correlación
plt.figure(figsize=(7,5))
sns.heatmap(df.drop(columns=['species']).corr(), annot=True, cmap="Blues")
plt.savefig("grafico_3.png")
plt.close()


# 5. Gráficos de violín
plt.figure(figsize=(12,6))
for i, col in enumerate(['sepal_length','sepal_width','petal_length','petal_width']):
    plt.subplot(2,2,i+1)
    sns.violinplot(data=df, x='species', y=col)
plt.tight_layout()
plt.savefig("grafico_4.png")
plt.close()

