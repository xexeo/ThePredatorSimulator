# ThePredatorSimulator
It works by using Case-based reasoning to determine the best way  of approaching prey, then using the A* pathfinding algorithm to find the quickest route to the nearest prey. 
## Case-based Reasoning
This works by comparing previous cases to match the one most similar to the current case (e.g. 3 prey, 1 predator). These cases are stored as objects and are ordered to find the highest matching one (Based on the users chosen percentage).
## A* Pathfinding
This works by finding the best nodes towards a certain location, scoring them on distance and how many nodes have been used. The node with the best score is then added to the route of nodes. 