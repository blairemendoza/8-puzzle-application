from time import perf_counter
from state import State
from solver import Solver
import heapq

goalTest = [[0,1,2],[3,4,5],[6,7,8]]

class aStar(Solver):

  # solve method
  def solve(self):
    before = perf_counter()
    frontier = [self.initialState]
    self.initialState.getFEuclidean()
    self.explored.add(self.initialState.id)
    
    while frontier:
      self.expandedNodes += 1
      state = heapq.heappop(frontier)
      if (state.board == goalTest):
        self.finalState = state
        self.runningTime = perf_counter() - before
        return True
      if state.depth+1 > self.depth:
        self.depth = state.depth+1
      for neighbor in state.neighbors():
        if not ((neighbor.id in self.explored)):
          self.explored.add(neighbor.id)
          neighbor.getFEuclidean()
          heapq.heappush(frontier,neighbor)
    
    self.runningTime = perf_counter() - before
    return False