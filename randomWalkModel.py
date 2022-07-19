import math
from platform import node
import pylab
import itertools
import random

import random as rand
import numpy as np
import networkx as nx
from networkx.utils import powerlaw_sequence
import scipy.stats as stats

def buildRandomWalkModel(N, m, p):
    # Create a clique of m nodes
    G = nx.complete_graph(int(math.sqrt(m)))
    for i in range(G.number_of_nodes(), N):
        firstAttach = np.random.choice(G.nodes)
        neighIter = nx.neighbors(G, firstAttach)
        
        # Get the list of possible neighbors of "firstAttach"
        originalNeigh = []
        for neigh in neighIter:
            originalNeigh.append(neigh)
        # Attach the new added node to the selected node
        G.add_edge(i, firstAttach)
        
        possibleNeigh = originalNeigh
        for _ in range(m - 1):    
            if np.random.uniform() < p:
                # Connect i to one of the neighbor of "firstAttach"
                if(len(possibleNeigh) > 0):
                    choiceNeigh = np.random.choice(possibleNeigh)
                    G.add_edge(i, choiceNeigh)
                    possibleNeigh = list(set(possibleNeigh).difference({choiceNeigh}))
            else: 
                # Fine the neighors of i to exclude them
                newNeigh = []
                for neigh in nx.neighbors(G, i):
                    newNeigh.append(neigh)

                # Connect i to one of the other nodes
                nodes = set(G.nodes())
                otherNodes = nodes.difference(set(originalNeigh))
                otherNodes = otherNodes.difference({i, firstAttach})
                otherNodes = otherNodes.difference(set(newNeigh))
                if(len(otherNodes) > 0) :
                    G.add_edge(i, np.random.choice(list(otherNodes)))
        
    print("Degree assortativity of RW model:", nx.degree_assortativity_coefficient(G))
    print("Clustering coefficient of RW model:", nx.average_clustering(G))
    nx.draw(G, with_labels=True)
    pylab.show()
    
    return G
    
N = 50
m = 8
# Probability of triadic closure
p = 0

buildRandomWalkModel(N, m, p)

G = nx.barabasi_albert_graph(N,m)
print("Degree assortativity of BA graph:", nx.degree_assortativity_coefficient(G))
print("Clustering coefficient of BA graph:", nx.average_clustering(G))
nx.draw(G, with_labels=True)
pylab.show()
    