#Exercise 3.1
import networkx as nx

k = 5
m = 4
n = 400

g = nx.star_graph(k)
print(g)

for i in range(k+1, n+1):
    degrees = dict(g.degree()) # in dict key is node and value is degree
    