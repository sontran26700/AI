from collections import defaultdict 
import re
from collections import defaultdict,deque
import sys
from sys import argv
from collections import Counter

data = open(argv[2],"r") 

  
from collections import defaultdict 
  

class Gra: 
  
    def __init__(self,vertices): 
        self.V= vertices 
        self.graph = [] 
                                
          
   
    
    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w]) 
  
    
     
    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 
  
    
    
    def union(self, parent, rank, x, y): 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y) 
  
         
        
        if rank[xroot] < rank[yroot]: 
            parent[xroot] = yroot 
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot 
  
         
        
        else : 
            parent[yroot] = xroot 
            rank[xroot] += 1
  
      
        
    def KruskalMST(self): 
  
        result =[] 
  
        i = 0 
        e = 0 
  
            
                
                
                
        self.graph =  sorted(self.graph,key=lambda item: item[2]) 
  
        parent = [] ; rank = [] 
  
        
        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 
      
         
        while e < self.V -1 : 

            u,v,w =  self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent ,v) 
  
             
                         
                        
            if x != y: 
                e = e + 1     
                result.append([u,v,w]) 
                self.union(parent, rank, x, y)             
            
        temp = 0
        for u,v,weight in result:
            temp = temp + weight
        return temp

if __name__=="__main__": 
    
    from sys import argv
    from collections import Counter
    if argv[1] == 'kruskal':
        file = open(argv[2],'r')
        lines = file.readlines()
        arr = []
        for x in lines:
            arr.append(x.split())
        arr2 = []
        for i in range(len(arr)):
            arr2.append(int(arr[i][0]))
            arr2.append(int(arr[i][1]))
        ad = Counter(arr2)
        g = Gra(len(ad))
        for i in range(len(arr)):
            g.addEdge(int(arr[i][0]),int(arr[i][1]),int(arr[i][2]))
        rcv = g.KruskalMST()
        file2 = open(argv[3],'w+')
        # file2.write(str(co))
        file2.write(str(rcv))
        file2.close()
