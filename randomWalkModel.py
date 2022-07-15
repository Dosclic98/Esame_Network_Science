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

def buildRandomWalkModel(N, mMin, mMax, p):
    nStart = 4
    G = nx.complete_graph(nStart)
    for i in range(nStart, N):
        newM = round(np.random.uniform(mMin, mMax))
        firstAttach = np.random.choice(G.nodes)
        neighIter = nx.neighbors(G, firstAttach)
        
        # Get the list of possible neighbors of "firstAttach"
        possibleNeigh = []
        for neigh in neighIter:
            possibleNeigh.append(neigh)
        # Attach the new added node to the selected node
        G.add_edge(i, firstAttach)
        
        if np.random.uniform() < p:
            # Connect i to one of the neighbor of "firstAttach"
            G.add_edge(i, np.random.choice(possibleNeigh))
        else:
            # Connect i to one of the other nodes    
            nodes = set(G.nodes())
            otherNodes = nodes.difference(set(possibleNeigh))
            otherNodes = otherNodes.difference({i, firstAttach})
            if(len(otherNodes) > 0) :
                G.add_edge(i, np.random.choice(list(otherNodes)))
    
    print("Degree assortativity: " + nx.degree_assortativity_coefficient(G).__str__())
    print("Clustering coefficient: " + nx.average_clustering(G).__str__())
    nx.draw(G, with_labels=True)
    pylab.show()
    
N = 10
mMin = 2
mMax = 6
# Probability of triadic closure
p = 0.8

buildRandomWalkModel(N, mMin, mMax, p)