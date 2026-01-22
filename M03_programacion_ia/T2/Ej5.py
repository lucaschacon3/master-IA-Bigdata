import pandas as pd

data={
    'Nombre': ['Ana', 'Luis', 'Carlos', 'Marta'],
    'Edad': [23, 35, 45, 29],
    'Nota': [3, 9, 5, 8]
}

df=pd.DataFrame(data)

print("DataFrame original:")
print(df)

print("-------------------------")

df['Aprobado'] = df['Nota'] >= 5

print("DataFrame con columna 'Aprobado':")
print(df)
print("-------------------------")

estudiantes_aprobados = df[df['Aprobado']]

print("Estudiantes aprobados:")
print(estudiantes_aprobados)
print("-------------------------")

promedio_notas = df['Nota'].mean()

print("Promedio de notas de los estudiantes:", promedio_notas)