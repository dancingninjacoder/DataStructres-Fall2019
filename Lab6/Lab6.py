#Kimberly Arenas

#Imports the kruskal and the top sort programs needed to implement the graphs
import Kruskal as K
import Topological as topSort

#NOTE: The graphs created in the main file are based on the ones from the previous homework given to us in class
  
#Method to create a hard-coded graph so it can be sent to the kruskal.py file
def Kruskal_Algorithm():
    #Sets the number of vertices in the graph
    n = 10
    #Creates the maximum number of vertices for this graph
    g = K.Kruskal(n) 
    print("Applying a graph of ",n," vertices.")
    print("")
    #Sets the edges that are present in the graph, reading from, to, and its weight value
    g.addEdge(0, 1, 4) 
    g.addEdge(0, 4, 3) 
    g.addEdge(1, 4, 2) 
    g.addEdge(1, 5, 5) 
    g.addEdge(1, 2, 4) 
    g.addEdge(2, 5, 6)
    g.addEdge(2, 6, 9)
    g.addEdge(3, 6, 13)
    g.addEdge(4, 7, 1)
    g.addEdge(4, 5, 12)
    g.addEdge(5, 7, 21)
    g.addEdge(7, 8, 14)
    g.addEdge(5, 8, 11)
    g.addEdge(5, 6, 17)
    g.addEdge(6, 8, 10)
    g.addEdge(8, 9, 16)
    g.addEdge(3, 9, 20)
    print("")
    print("Creating the new graph using Kruskal's Algorithm...")
    #Sends the new formed graph to be sorted using kruskal's algorithm. The next class will print its result
    g.Kruskal_al()
    
def Topological_sort():
    #Sets the number of vertices in the graph
    n = 9
    #Creates the maximum number of vertices for this graph
    g2 = topSort.Topological(n)
    print("Applying a graph of ",n," vertices.")
    print("")
    #Sets the edges that are present in the graph, reading from, and to values
    g2.add_edge(0, 1) 
    g2.add_edge(4, 0) 
    g2.add_edge(4, 1) 
    g2.add_edge(7, 4) 
    g2.add_edge(5, 4) 
    g2.add_edge(5, 7) 
    g2.add_edge(8, 7) 
    g2.add_edge(8, 5) 
    g2.add_edge(5, 1) 
    g2.add_edge(2, 1) 
    g2.add_edge(2, 3) 
    g2.add_edge(5, 2) 
    g2.add_edge(6, 2) 
    g2.add_edge(6, 3) 
    g2.add_edge(6, 5) 
    g2.add_edge(6, 8) 
    g2.add_edge(3, 1) 
    print("")
    print("Creating the new graph for Topological Sort...")
    print("")
    #Sends the new formed graph to be sorted using kruskal's algorithm. The next class will print its result
    g2.topological_sort()

def main():
    print("Kruskal and Topological Sort program!") 
    print("")
    print("Choose the graph implementation would you test out today:")
    print("")
    print("A. Kruskal's Algorithm")
    print("B. Topological Sort")
    user_selection = input()
    count = 0
    if (user_selection == "A" or user_selection == "a"):
        print("Applying Kruskal's Algorithm...")
        print("")
        Kruskal_Algorithm()
    elif (user_selection == "B" or user_selection == "b"):
        print("Applying Topological Sort...")
        print("")       
        Topological_sort()
    elif count == 3:
        print("ERROR: Too many incorrect statements!")
        print("Farewell.")
    else: 
        print("ERROR: Input not valid!") 
        count+=1
        main()
        
main()