# conda install pandas
import pandas as  pd


from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

# Obtenemos el dataset a entrenar
df = pd.read_csv('https://raw.githubusercontent.com/jsulopz/data/main/uso_internet_espana.csv')
df = df.drop(columns=['Unnamed: 0']) 

# Imprimimos 5 filas aleatorias
print("5 EJEMPLOS DE LOS DATOS....................................................")
print(df.sample(5))
print("INFORMACIÓN DEL DATASET....................................................")
print(df.info())

# convertimos las variables categóricas en one-hot encoding
df = pd.get_dummies(data=df, drop_first=True)

# Imprimimos 5 filas aleatorias
print("5 EJEMPLOS CON FORMATO ONE-HOT....................................................")
print(df.sample(5))

# Separamos las features y el target
x = df.drop(columns='uso_internet')     # features
y = df['uso_internet']                  #target

print("DATASET DE LOS FEATURES....................................................")
print(x.info())

# Creamos el modelo
model = DecisionTreeClassifier(max_depth=3)
# Entrenamos el modelo
model.fit(x,y)

# pasamos las features y el target para que nos diga que tan bien predice
print("ACCURACY DEL MODELO....................................................")
print(model.score(x, y))




## PARA PODER VISUALIZAR EL ARBOL

# conda install python-graphviz
import graphviz 

dot_data = tree.export_graphviz(model,out_file=None, 
                      feature_names=x.columns.tolist(),  
                      class_names=df['uso_internet'].astype(str).unique().tolist(),  
                      filled=True, rounded=True,  
                      special_characters=True) 
graph = graphviz.Source(dot_data) 

# nombre del pdf a guardar
graph.render("arbolPreview") 


## Usando el Modelo para predecir

# Obtenemos que ingresará el usuario
anios = 16
sexo = "MuJer"
estudios = "Sin"

# Verificamos que se entendieron correctamente
if(anios == None):
    print("No entiendo el año") 
if(sexo == None):
    print("No entiendo el sexo")
if(estudios == None):
    print("No entiendo los estudios")

anios = str(anios)
sexo = sexo.lower()
estudios = estudios.lower()

sexo_mujer = "0" if sexo == "mujer" else "1"
estudios_sin = "1" if estudios == "sin" else "0"
estudios_primarios = "1" if estudios == "primario" else "0"
estudios_secundarios = "1" if estudios == "secundario" else "0"
estudios_superiores = "1" if estudios == "superior" else "0"
estudios_universitarios = "1" if estudios == "universitario" else "0"

print(anios)
print(sexo)
print(estudios)

# generamos un dataframe con los datos que nos pasaron para predecir el uso de internet
user_data = pd.DataFrame({
    'edad': [anios],
    'sexo_Mujer': [sexo_mujer],  
    'estudios_Medios universitarios': [estudios_universitarios],  
    'estudios_Primaria': [estudios_primarios],  
    'estudios_Secundaria': [estudios_secundarios],  
    'estudios_Sin estudios': [estudios_sin],
    'estudios_Superiores': [estudios_superiores],  
})

print(user_data.head())

y_pred = model.predict(user_data)
print(y_pred)