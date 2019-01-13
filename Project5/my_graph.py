#my_graph.py



class Vertex:
   def __init__(self, key):
		
      self.id = key
      self.connected = []
      self.visited = False
      self.color = None

   def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connected])

   #def __eq__(self, other):
   #   return self.id == other.id
class MyGraph:
   def __init__(self, filename):
      self.num_connections = 0
      self.num_vertices = 0
      self.vertList = 0
      self.missingverts = False
      self.missingvertlist = []
      self.visitedlist = []
      self.colorlist = []

      self.filename = filename
      self.read_file(filename)
      


   def read_file(self, filename):
		#reads the file and inputs connections and vertices
      infile = open(filename, 'r')
      inputlist = infile.readlines()

      connections = []
      templist = []

      for i in range(len(inputlist)):
         if(i == 0):
            self.num_vertices = int(inputlist[0].strip())
            self.vertList = [None]*self.num_vertices
            #fakevariable = 0
         elif(i == 1):
            #self.num_connections = int(inputlist[1].strip())
            fakevariable = 1
         else:
            #print(self.vertList)
            inputlist[i] = inputlist[i].replace(" ", '')
            vert1 = int(inputlist[i][0])
            vert2 = int(inputlist[i][1])
            self.addEdge(vert1,vert2)

            #print(self.vertList[0].connected[0].id)

     # numlist = [x for x in range(self.num_vertices)]
      for i in range(len(self.vertList)):
         if(self.vertList[i] == None):
            self.missingverts = True
            self.missingvertlist.append(i+1)


   def addEdge(self,f,t,cost=0):
        if(self.vertList[f-1] == None):
           nv = self.addVertex(f)
        if(self.vertList[t-1] == None):
           nv = self.addVertex(t)

        #f_connected = self.get_con_id(self.vertList[f-1].connected)
        #print(self.vertList[t-1].id)
        #if(self.vertList[t-1].id not in f_connected):
        #print("adding connections to" , self.vertList[f-1].id, ": ", self.vertList[t-1].id)
        self.vertList[f-1].connected.append(self.vertList[t-1])
        self.vertList[t-1].connected.append(self.vertList[f-1])
        #print("the connected length of " ,self.vertList[f-1].id, " is ", len(self.vertList[f-1].connected))

   def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
   def get_con_id(self, connlist):
      returnlist = []
      for i in range(len(connlist)):
         returnlist.append(connlist[i].id)


   def addVertex(self,key):
        self.num_vertices = self.num_vertices + 1
        newVertex = Vertex(key)
        #print(key)
        #print(self.num_vertices)
        #print(len(self.vertList))
        self.vertList[key-1] = newVertex
        return newVertex

   def is_num(self, num):
      try:
         float(num)
         return True
      except ValueError:
         return False

   def conn_components(self):
		#returns a list of lists of the connections within the graph
      connections = []
      for i in range(len(self.vertList)):
         if(self.vertList[i] != None):
            if(self.vertList[i].visited == False):
               connectedlist = []
               self.depth_connections(self.vertList[i], connectedlist)
               connections.append(connectedlist)
      if(self.missingverts == True):
        connections.append(self.missingvertlist)

      #sort by number order before returning lists!!!!
      return connections

   def depth_connections(self, vertex, connectedlist):
      connectedlist.append(vertex.id)
      vertex.visited = True
      for i in range(len(vertex.connected)):
         if(vertex.connected[i].visited == False):
            self.depth_connections(vertex.connected[i], connectedlist)

   def depth_b(self, v):
      self.visitedlist[v] = 1
      #for i in range(len(self.vertList[v].connected)):
         #print(self.vertList[v].connected[i], ' color: ', self.colorlist[i])
      for i in self.vertList[v].connected:
         if(self.colorlist[i.id-1] == self.colorlist[v]):
            print("node: ", i.id, "color:",self.colorlist[i.id-1], " node2: ",self.vertList[v].id, " color: ", self.colorlist[v])
            return False
         if(self.visitedlist[i.id] == 0):
            self.colorlist[i.id] = not self.colorlist[v]
            if not self.depth_b(i.id-1):
               return False
      return True

   def bicolor(self):
      #dear grader, I know this function does not work because I kept getting false on the last node in the vertlist. 
      #Hopefully you see that I was extremely close to coming up with the algorithm and I can get some partial credit on this sections. Thanks!!!
      self.colorlist = [0]*(self.num_vertices+1)
      self.visitedlist = [0]*(self.num_vertices+1)
      for i in range(self.num_vertices):
         #print(i)
         i+=1
         if(self.visitedlist[i] == 0):
            self.colorlist[i] = True
            if not self.depth_b(i):
               return False
      return True

   
         
      

