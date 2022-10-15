from time import perf_counter
from collections import deque
from state import State
from solver import Solver

goalTest = [[0,1,2],[3,4,5],[6,7,8]]

class BFS(Solver):
  
  def solve(self):
    self.expandedNodes += 1
    before = perf_counter()
    frontier = deque([self.initialState])
    self.explored.add(self.initialState.id)
    
    while frontier:
      state = frontier.popleft()
      state.getFManhattan()
      if (state.board == goalTest):
        self.finalState = state
        self.runningTime = perf_counter() - before
        return True
      if state.depth+1 > self.depth:
        self.depth = state.depth+1
      for neighbor in state.neighbors():
        if not ((neighbor.id in self.explored)):
          self.explored.add(neighbor.id)
          frontier.append(neighbor)
    
    self.runningTime = perf_counter() - before
    return False