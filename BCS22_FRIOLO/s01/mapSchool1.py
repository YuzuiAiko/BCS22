def algo(graph, start, end):
    #if there is unknown value, assign it to inf
    distances = {location: float('inf') for location in graph}


    #assigns none to all previous location slots
    previous_loc = {node: None for node in graph}


    #print(distances)
    distances[start] = 0


    #makes library for visited locations
    visited = set()

    #make storage for the shortest graph
    shortpath_graph = []

    #condition where loop continues when all places are not yet visited
    while visited != set(graph):
        #this line of code identifies the current location and its weight using the lambda
        #it also checks whether the node has been visited already or not
        current_loc = min((node for node in graph if node not in visited), key=lambda node: distances[node])

        #appends current location to visited library
        visited.add(current_loc)

        for next_loc, weight in graph[current_loc].items():
            #adds current value to the next locations value
            newval = distances[current_loc] + weight


            #checks if newval is lower than next locations value
            if newval < distances[next_loc]:

                #This code replaces the inf value of the next location to the sum of the weight of current location
                # and weight of next location(eg. store_a = 0(home) + 7(store_a's value from graph)
                distances[next_loc] = distances[current_loc] + weight

                # assigns all of the current node's neigbors previous node as the current node
                # (eg. current node: Home, neighbor node: store_a(previous node:Home)
                previous_loc[next_loc] = current_loc

    while end != start:

        # backtracking with the use of graphing the previous location of each location
        shortpath_graph.append(end)

        #assign end to the previous location of the current end value (eg. School(store_b), store_b(store_a)
        end = previous_loc[end]

        #if end is start, add start value which is home.
        if start == end:
            shortpath_graph.append(end)

    #reverses list to from home to destination
    shortpath_graph.reverse()
    print("The shortest path from home to school (L to R):",shortpath_graph)


graph = {
    'home': {'store_a': 7, 'store_b': 14, 'intersection':25},
    'store_a': {'home': 7, 'store_b': 5},
    'store_b': {'school': 7},
    'intersection': {'school': 7},
    'school': {'store_b': 7, 'intersection':7}

}

start = "home"
end = "school"
algo(graph, start, end)