
# coding: utf-8

# In[11]:


import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


# In[12]:


N  = 100
k = 7
#setting graph (x, y) coordinates 
G = nx.empty_graph(N)
coordinates = nx.random_layout(G) 
x, y = zip(*coordinates.values())

#creating links between nodes
for node in G.nodes():
    distances = np.sqrt(np.power(x[node]-x, 2) + np.power(y[node]-y, 2))
    probabilities = distances/distances.sum()
    connect_to = np.random.choice(G.nodes(), size=k, p=probabilities, replace=False)
    edges = [(node, adj_node) for adj_node in connect_to]
    G.add_edges_from(edges)


# In[13]:


#Function for visualizing the graph node degree distribution 
#If normalize=True - show the probability of degrees, otherwise - their frequency
#log_y - whether to show y-axis in logarithmic scale
def plot_degree_distribution(degrees, frequency, normalize=True, log_y=False):
    if normalize == True:
        y = frequency/frequency.sum()
        ylab = 'probability'
    else:
        y = frequency
        ylab = 'frequency'           
    if log_y == True:
        y = np.log(y)
        ylab = 'ln({})'.format(ylab)    
    plt.plot(degrees, y, 'ro')
    plt.xlabel('degree')
    plt.ylabel(ylab)
    plt.title('Degree distribution')


# In[14]:


#Graph visualization
nx.draw_networkx(G, pos=coordinates, with_labels=False, node_size=[deg for deg in dict(nx.degree(G)).values()])
plt.show()


# In[15]:


#Visualization of the gaph node degree distribution
degrees_list = sorted(list(set(dict(nx.degree(G)).values())))
degrees_count = [list(dict(nx.degree(G)).values()).count(deg) for deg in degrees_list]
plot_degree_distribution(np.array(degrees_list), np.array(degrees_count), True, False)
plt.show()

