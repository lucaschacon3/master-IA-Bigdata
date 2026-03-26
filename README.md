# Máster en Inteligencia Artificial y Big Data

Repositorio general con el contenido, prácticas y proyectos desarrollados durante el Máster en IA & Big Data.  
El objetivo es centralizar todo el trabajo de las distintas asignaturas en una única estructura organizada y reutilizable. 

---

## ⚙️ Instalación

```bash
git clone https://github.com/lucaschacon3/master-IA-Bigdata.git
cd master-ia-bigdata
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt


# Fundamentos de IA

## Contenidos

- **Introducción a la Inteligencia artificial.**
    - Recorrido histórico de la IA.
    - Potencial y desafíos de la Inteligencia artificial.
    - Tipos de IA (Débil, fuerte, general)
    - Subcampos de la Inteligencia artificial
        - IA.
        - ML.
        - DL - Redes neuronales.
        - GenAI.
        - IA Agéntica
        - NLP.
        - CV (Computer Visión).
        - Sistemas expertos.
        - Robótica - IoT.
- **Herramientas para el desarrollo de IA.**
    - Lenguajes de programación para la IA.
        - Python.
        - Java.
        - R.
        - C++.
        - JavaScript - TypeScript.
    - Bibliotecas y frameworks para la IA.
        - Matemáticas: numpy
        - Manipulación y validación de datos: pydantic, pandas, polars, SQLAlquemy
        - Visualización: matplotlib, seaborn, plotly
        - ML: scikit-learn, XGBoost
        - DL: Tensorflow, keras, pytorch, Huggingface transformers
        - NLP: spacy, nltk
    - IDES y editores de código con IA.
        - Vscode + Github copilot
        - Cursor
        - Antigravity
        - Windsurf
    - Agentes para el desarrollo.
        - Claude Code.
        - Open Code.
        - OpenClaw
    - IA local
        - Ollama
        - vLLM
    - Cloud Computing para la IA (Iaas, Paas, Saas).
        - AWS
        - Azure
        - GCP
- **ML y DL.**
    - Problemas de entrenamiento.
        - Overfitting
        - Underfitting
        - Outliers.
        - Regularización L1, L2
    - Paradigmas del ML
        - Supervisado.
        - No supervisado.
        - Aprendizaje por refuerzo.
        - Autosupervisado.
    - Modelos de ML.
        - Regresión (supervisado): regresion lineal, regresión logística, knn, svm, arbol de decision, randon forest, gradient boosting.
        - Clasificación (supervisado): Naive bayes, knn, svm, arbol de decision, randon forest, gradient boosting.
        - Segmentación (Clústering - no supervisado): Kmeans, dbsca.
    - Modelos DL - Redes neuronales.
        - MLP: supevisado (regresión y clasificacion).
        - RNN: supevisado (regresión y clasificacion).
        - CNN: supevisado (clasificacion) .
        - Transformers (GPT, BERT): supervisado y autosupervisado.
        - Autoencoders: no supervisado (segmentacion - clustering)
    - Tests de Modelos.
        - Regresion: MAE, MSE, RMSE, R2
        - Clasificación: Accuracy, precisión, recall, F1-Score, Matriz de confusión, ROC/AUC.
        - Segmentación (clustering): inercia, silhouette score, visualización
        - Métricas de Negocio (ROI, latencia de inferencia, costo por token).
- **IA generativa.**
    - NLP.
    - LLM y Transformers.
    - Agentes (Langchain, LLamaindex)
    - Orquestacion de agentes (LangGraph, CrewAI)
    - Tokenización.
    - Pompting.
    - RAG - BBDD vectoriales.
    - Transfer Learning - Finetunning (LoRa, QLoRa).
    - IA multimodal
- **Ética y legalidad.**
    - Privacy by desing.
    - Peligros y casos reales.
    - EU AI Act - AESIA
    - Shadow AI
    - Gobernanza y compliance.