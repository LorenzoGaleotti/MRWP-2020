
import networkx as nx
import matplotlib.pyplot as plt
import math as mt



#Warm-up

def evenOddS(s):
    if mt.remainder(len(s),2)==0: 
        return "yes"
    else:
        print("no")
        return "no"
    
evenOddS("test")

def prefix(s,s1):
    if s1.startswith(s):
        return "yes"
    else:
        return "no"

def prefix1(s,s1):
    i=0
    while i<len(s) and s[i]==s1[i]:
        i+=1
    if i==len(s):
        return "yes"
    else:
        return "no"

print(prefix1("io","it"))

def extension(s):
    l=s.split(".")
    if len(l)==1:
        return "NONE"
    else:
        return l[len(l)-1]

def extension1(s):
    i=0
    j=-1
    while i<len(s):
          if s[i]==".":
              j=i
          i+=1
    if j==-1:
        return "NONE"
    else:
        return s[j+1:]

 
print(extension1("pippo.1"))

def listtodic(l,l1):
    d={}
    if len(l)!=len(l1):
        return d
    for i in range(len(l)):
        d[l[i]]=l1[i]
    return d

print(listtodic([1,2],["a","b"]))

def dicttolist(d):
    return (list(d.keys()),list(d.values()))

print(dicttolist({1:"a"}))

#Graph

G=nx.Graph()

print(G.edges())
print(G.nodes())


for n in range(100):
    G.add_node(n)
    if mt.remainder(n,2)==0 and n+2<100:
        G.add_edge(n,n+2)
    if mt.remainder(n,3)==0:
        for i in range(n):
            G.add_edge(n,i)
            
print(G.adj)

def deg(G,n):
    if n in G:
        return len(G[n]) 
    
print(deg(G,1), G[1])


nx.write_gexf(G,"prova.gexf")
#nx.draw_kamada_kawai(G,with_labels=True)
#
#plt.show()

pos=nx.kamada_kawai_layout(G)
lab={}
for n in G:
    lab[n]=n
    
nx.draw_networkx_nodes(G,pos, node_color='r',node_size=500,alpha=0.8)
nx.draw_networkx_labels(G,pos,lab,font_size=16)
nx.draw_networkx_edges(G,pos)

plt.show()

def spanning(G,n):
    todo={n}
    T=nx.Graph()
    while todo!=set():
        m=todo.pop()
        T.add_node(m)
        for o in G[m]:
            if o not in T:
                T.add_edge(m,o)
                if o not in todo:
                    todo.add(o)
    return T

def connected_component(G,n):
    return G.subgraph(spanning(G,n).nodes())

def maximalCC(G):
    todo=list(G.nodes())
    size=-1
    while todo!=[]:
        n=todo.pop()
        pc=connected_component(G,n)
        if size<pc.size():
            size=pc.size()
            cc=pc
    return cc



#G1=nx.Graph()
#G1.add_edge(1,2)
#G1.add_edge(3,4)
#G1.add_edge(3,5)
#
#nx.draw(maximalCC(G1))
#plt.show()
#
#nx.draw(connected_component(G1,2),with_labels=True)
#print(len(G.nodes()))
