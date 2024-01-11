# 𝓢𝓮𝓪𝓻𝓬𝓱 𝓐𝓵𝓰𝓸𝓻𝓲𝓽𝓱𝓶 𝓥𝓲𝓼𝓾𝓪𝓵𝓲𝔃𝓪𝓽𝓲𝓸𝓷

This repository includes a visualization of different search algorithms. It consists of two main classes: the 𝓮𝓷𝓿𝓲𝓻𝓸𝓷𝓶𝓮𝓷𝓽 class and the 𝓪𝓰𝓮𝓷𝓽 class. The 𝓮𝓷𝓿𝓲𝓻𝓸𝓷𝓶𝓮𝓷𝓽 class creates a setup with a target (red) and walls (black), and the agent's task is to interact with the environment to search for the target. Each agent has its own implemented search method. The 𝓮𝓷𝓿𝓲𝓻𝓸𝓷𝓶𝓮𝓷𝓽 class is built using the pygame module.

The user can instantiate an environment instance by specifying the percentage of tiles that will be covered with walls. The user is also able to input the agent's starting position and the target position. After the agent completes searching, the agent outputs the searched path in blue if possible.

From the visualization, we see that depth-first search expands the most nodes, which demonstrates its inefficiency in such tasks. On the other hand, informed search algorithms such as greedy search and A* search with Manhattan heuristic performed the best on average.

## 1. Depth first search

<p align="center">
  <img src="Graphics/DFS.gif" width="30%">
</p>
    
<p align="center">
  Depth-First Search Visualization
</p>

## 2. Breadth first search

<p align="center">
  <img src="Graphics/BFS.gif" width="30%">
</p>
    
<p align="center">
  Breadth-First Search Visualization
</p>

## 3. Greedy search

<p align="center">
  <img src="Graphics/Greedy.gif" width="30%">
</p>
    
<p align="center">
  Greedy Search Visualization
</p>

## 4. A* search

<p align="center">
  <img src="Graphics/Astar.gif" width="30%">
</p>
    
<p align="center">
  A* Search Visualization
</p>


