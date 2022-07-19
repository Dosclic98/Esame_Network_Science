import math
import pylab
import itertools
import random

import random as rand
import numpy as np
import networkx as nx
from networkx.utils import powerlaw_sequence
import scipy.stats as stats

def buildConfigModelNetwork(degreeSequence):
    MG = nx.MultiGraph()
    
    iter = (sum(degreeSequence)/2)
    print("Degree Sequence: " + degreeSequence.__str__())
    originalDegrees = degreeSequence.copy()
    while sum(degreeSequence) > 0:
        #print("Degree Sequence: " + degreeSequence.__str__())
        first, second = np.random.randint(0,len(degreeSequence)), np.random.randint(0,len(degreeSequence))
        while (first != second and (degreeSequence[first] < 1 or degreeSequence[second] < 1)) or (first == second and (degreeSequence[first] < 2)):
            first, second = np.random.randint(0,len(degreeSequence)), np.random.randint(0,len(degreeSequence)) 
        
        degreeSequence[first] = degreeSequence[first] - 1
        degreeSequence[second] = degreeSequence[second] - 1
            
        MG.add_edge(first, second)
    
    for n in MG.nodes:
        assert(MG.degree(n) == originalDegrees[n])
    
    # Remove multiedges creating a normal graph
    G = nx.Graph(MG)
    # Remove self loops
    G.remove_edges_from(nx.selfloop_edges(G))
    print("Degree assortativity:", nx.degree_assortativity_coefficient(G))
    print("Clustering coefficient:", nx.average_clustering(G))
    nx.draw(G, with_labels=True)
    pylab.show()
    
    return G
        
        

N = 1000
degreesUniform = [0] * N
degreesNormal = [0] * N
degreesPower = [0] * N

mu, sigma = 3, 1
alpha = 1.5
a, b = 3, 7

degreesNormal = np.round(np.random.normal(mu, sigma, N)).astype(int)
while sum(degreesNormal) % 2 != 0 and sum(degreesNormal)/2 > len(degreesNormal):
    degreesNormal = np.round(np.random.normal(mu, sigma, N)).astype(int)
    
degreesUniform = np.round(np.random.uniform(a,b, size=N)).astype(int)    
while sum(degreesUniform) % 2 != 0 and sum(degreesUniform)/2 > len(degreesUniform):
    degreesUniform = np.round(np.random.uniform(a,b, size=N)).astype(int)    


degreesPower = nx.random_powerlaw_tree_sequence(N, tries=50000)

buildConfigModelNetwork(degreeSequence=degreesNormal)
buildConfigModelNetwork(degreeSequence=degreesUniform)
buildConfigModelNetwork(degreeSequence=degreesPower)