import math
import pylab
import itertools
import random

import random as rand
import numpy as np
import networkx as nx
from networkx.utils import powerlaw_sequence
import scipy.stats as stats

def buildFitnessModel(N, m, dist):
    # Create a clique of m nodes
    G = nx.complete_graph(m)
    print("Distribution: " + dist.__str__())
    for i in range(G.number_of_nodes(), N):
        # Select m different nodes at random, weighted by their degree.
        newNeighbors = []
        possibleNeighbors = list(G.nodes)
        for _ in range(m):
            degrees = [dist[n] * G.degree(n) for n in possibleNeighbors]
            j = random.choices(possibleNeighbors, degrees)[0]
            newNeighbors.append(j)
            possibleNeighbors.remove(j)
        
        # 3. Add a new node i and link it with the m nodes from the previous step.
        for j in newNeighbors:
            G.add_edge(i, j)

    print("Degree assortativity:", nx.degree_assortativity_coefficient(G))
    print("Clustering coefficient:", nx.average_clustering(G))
    nx.draw(G, with_labels=True)
    pylab.show()
    
    return G


N = 50
m = 8
degreesUniform = [0] * N
degreesNormal = [0] * N
degreesPower = [0] * N

mu, sigma = 3, 1
alpha = 1.5

distNormal = np.random.normal(mu, sigma, N)
distUniform = np.random.uniform(3,7, size=N)
distPower = nx.random_powerlaw_tree_sequence(N, tries=5000)

buildFitnessModel(N, m, distNormal)
buildFitnessModel(N, m, distUniform)
buildFitnessModel(N, m, distPower)

