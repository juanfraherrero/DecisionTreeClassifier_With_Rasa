from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_opcion"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Obtenemos las entidades
        anios = next(tracker.get_latest_entity_values('anios'), None)
        sexo = next(tracker.get_latest_entity_values('sexo'), None)
        estudios = next(tracker.get_latest_entity_values('estudios'), None)

        # Verificamos que se entendieron correctamente
        if(anios == None):
            dispatcher.utter_message(text="No entiendo el año")
            return 
        if(sexo == None):
            dispatcher.utter_message(text="No entiendo el sexo")
            return
        if(estudios == None):
            dispatcher.utter_message(text="No entiendo los estudios")
            return
        
        # convertimos a string y a minúsculas
        anios = str(anios)
        sexo = sexo.lower()
        estudios = estudios.lower()

        # convertimos a one-hot encoding
        sexo_mujer = "1" if sexo == "mujer" else "0"
        estudios_sin = "1" if estudios == "sin" else "0"
        estudios_primarios = "1" if estudios == "primario" else "0"
        estudios_secundarios = "1" if estudios == "secundario" else "0"
        estudios_superiores = "1" if estudios == "superior" else "0"
        estudios_universitarios = "1" if estudios == "universitario" else "0"


        # generamos un dataframe con los datos que nos pasaron para 
        #   predecir el uso de internet
        user_data = pd.DataFrame({
            'edad': [anios],
            'sexo_Mujer': [sexo_mujer],  
            'estudios_Medios universitarios': [estudios_universitarios],  
            'estudios_Primaria': [estudios_primarios],  
            'estudios_Secundaria': [estudios_secundarios],  
            'estudios_Sin estudios': [estudios_sin],
            'estudios_Superiores': [estudios_superiores],  
        })

        # # print(user_data.head())
        
        # predecimos y respondemos al usuario
        y_pred = model.predict(user_data)

        if(y_pred[0] == 1):
            dispatcher.utter_message(text="Te recomiendo buscar en Google informaión, la wikipedia es un buen lugar para empezar")
        else:
            dispatcher.utter_message(text="Te recomiendo ir a una biblioteca y leer libros, seguramente haya alguna cerca en tu zona")

        return []
    



# conda install pandas
import pandas as  pd

# conda install -c anaconda scikit-learn
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

# Obtenemos el dataset a entrenar
df = pd.read_csv('https://raw.githubusercontent.com/jsulopz/data/main/uso_internet_espana.csv')
print(df.info())
df = df.drop(columns=['Unnamed: 0']) 
print(df.info())
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