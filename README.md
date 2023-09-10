# Using Decision Tree Classifier with Rasa

This repository is a example for the subject "Programación Exploratoria" about how to run a DecisionTreeClassifier model in Rasa.

The model is train with the [dataset](https://raw.githubusercontent.com/jsulopz/data/main/uso_internet_espana.csv). It predict whether is better for te user search information in google or got to a library based on the features age, sex, and highest degree of study achieved.

## Installation
Use a virtual enviroment as [Anaconda](https://www.anaconda.com/products/distribution), download and install it.
Then you need [Python](https://www.python.org/), currently using version 3.9.12

Once you have both of them, get inside the terminal and create a virtual enviroment and excute, (without the ").
```bash
create --name "NameOfYourEnviroment" python="YourPythonVersion"
```
This command create the virtual enviroment, and everytime you want to get in the enviroment you must run the next command.
```bash
conda activate "NameOfYourEnviroment"
```
Once we are in the enviroment, we install the next dependencies, one at time.
```bash
conda install ujson
conda install tensorflow
pip install rasa
conda install pandas
conda install python-graphviz
```
Now you are ready to pull the repository and in the terminal inside the virtual enviroment you can train it, and run it

## Usage

Once you clone or pull the repository to your local, then you have to train it, so inside your terminal and inside the conda enviroment with rasa you run the next command
```bash
rasa train
```
when the train is finished, run the next commands for testing both in separate terminals.
```bash
rasa shell
```
and 
```bash
rasa run actions
```
After both command finish, in the terminal where you run the *rasa shell* should appear a "type:" or something where you can talk to the agent. Chat with the agent:
```text
{your input} -> Buenas, donde me recomendarías buscar información?
{agent} -> claro! dime edad, sexo y estudios
{your input} -> tengo 11 soy hombre y tengo estudios superiores
```
Luego de indicarle la información al agente rasa usará el modelo de árbol de decisión para predecir si debe buscar en google o ir a una biblioteca.

