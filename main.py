import pandas as pd
from graph import Graph

dataset = pd.read_csv('train.csv')
graph = Graph()

for index, row in dataset.iterrows():
    graph.insert_node()
print("1233")