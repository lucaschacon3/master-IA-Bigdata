import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import confusion_matrix

# 1. Carga del dataset (sin etiquetas para el entrenamiento)
iris = load_iris()
X = iris.data
y_real = iris.target  # Solo para comparación posterior

# 2. Estandarización de variables
# Crucial para K-Means ya que se basa en distancias euclidianas: d(p,q) = \sqrt{\sum (p_i - q_i)^2}
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. Entrenamiento del modelo K-Means (K=3)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
clusters = kmeans.fit_predict(X_scaled)

# 4. Representación gráfica (Proyección 2D usando PCA)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

plt.figure(figsize=(12, 5))

# Gráfico de Clusters obtenidos
plt.subplot(1, 2, 1)
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=clusters, cmap='viridis', edgecolors='k')
plt.title('Clusters obtenidos por K-Means')
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')

# Gráfico de Clases reales
plt.subplot(1, 2, 2)
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y_real, cmap='plasma', edgecolors='k')
plt.title('Clases Reales (Dataset Iris)')
plt.xlabel('Componente Principal 1')
plt.ylabel('Componente Principal 2')

plt.tight_layout()
plt.savefig('kmeans_clustering.png')

# 5. Análisis descriptivo y comparación
# Nota: Los IDs de cluster pueden no coincidir con los IDs de target (0,1,2)
print("Matriz de contingencia (Clusters vs Real):")
print(confusion_matrix(y_real, clusters))

