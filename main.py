import random

graph ={
    "a": {
        "a": 0.2,
        "b": 0.3,
        "c": 0,
        "d": 0.2,
        "e": 0.2,
        "f": 0.1
    },

    "b": {
        "a": 0.5,
        "b": 0.3,
        "c": 0,
        "d": 0.1,
        "e": 0,
        "f": 0.1
    },

    "c": {
        "a": 0,
        "b": 0,
        "c": 0.7,
        "d": 0,
        "e": 0.2,
        "f": 0.1
    },

    "d": {
        "a": 0,
        "b": 0.2,
        "c": 0,
        "d": 0.2,
        "e": 0.5,
        "f": 0.1
    },

    "e": {
        "a": 0.1,
        "b": 0,
        "c": 0,
        "d": 0.3,
        "e": 0.3,
        "f": 0.3
    },

    "f": {
        "a": 0.1,
        "b": 0.05,
        "c": 0.05,
        "d": 0.6,
        "e": 0.1,
        "f": 0.1
    },
}

#this function allows us to randomly select the next vertex to travel to. Make sure to check the documentation for random.choices!
def checkTraversal(vertex):
    return random.choices(list(vertex.keys()), weights=list(vertex.values()))[0]

#empty list to hold the number of steps in each run of traversing from city A to city C
iteration_list = []


#randomly walk over the graph from city A to city C, tracking the number of steps taken
for x in range(500):
    steps = 0
    current_vertex = "a"

    while current_vertex != "c":
        current_vertex = checkTraversal(graph[current_vertex])
        steps +=1
    
    iteration_list.append(steps)

# print(iteration_list)

# plot historgram of results in iteration_list
import pandas as pd
import matplotlib.pyplot as plt

iteration_df = pd.DataFrame(iteration_list)

iteration_df.hist(bins=100)
plt.show()