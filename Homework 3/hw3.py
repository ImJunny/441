########################################################
#
# CMPSC 441: Homework 3
#
########################################################


student_name = 'John Nguyen'
student_email = 'jnn5163@psu.edu'



########################################################
# Import
########################################################

from hw3_utils import *
from collections import deque
import math

# Add your imports here if used






##########################################################
# 1. Best-First, Uniform-Cost, A-Star Search Algorithms
##########################################################


def best_first_search(problem):
    node = Node(problem.init_state, heuristic=problem.h(problem.init_state))
    frontier = deque([node])         # queue: popleft/append-sorted
    explored = [problem.init_state]  # used as "visited"

    while frontier:
        # if state is goal state, return node
        if problem.goal_test(node.state):
            return node
        
        # pick best node from frontier
        frontier = deque(sorted(frontier, key=lambda node: node.heuristic))
        lowestHNode = frontier.popleft()
        
        # create all one-step extentions of node to each child
        childrenNodes = lowestHNode.expand(problem)

        for child in childrenNodes:
            if problem.goal_test(child.state):
                return child
            if child.state not in explored:
                frontier.append(child)
                explored.append(child.state)
    
    return Node(None, None, None, None, None)



def uniform_cost_search(problem):
    node = Node(problem.init_state, heuristic=problem.h(problem.init_state))
    frontier = deque([node])         # queue: popleft/append-sorted
    explored = [problem.init_state]  # used as "visited"

    while frontier:
        # pick best node from frontier
        frontier = deque(sorted(frontier, key=lambda node: node.path_cost))
        lowestCNode = frontier.popleft()

        # if state is goal state, return node
        if problem.goal_test(lowestCNode.state):
            return lowestCNode
        
        # if state in explored, continue
        if lowestCNode in explored:
            continue

        # create all one-step extentions of node to each child
        explored.append(lowestCNode.state)
        childrenNodes = lowestCNode.expand(problem)
        
        for child in childrenNodes:
            if child.state not in explored:
                if child.state not in frontier:
                    frontier.append(child)
                for existing in frontier:
                    if existing.state == child.state and child.path_cost < existing.path_cost:
                        frontier.remove(existing)
                        frontier.append(child)
                        break
    
    return Node(None, None, None, None, None) 


    
def a_star_search(problem):
    node = Node(problem.init_state, heuristic=problem.h(problem.init_state))
    frontier = deque([node])         # queue: popleft/append-sorted
    explored = []                    # used as "expanded" (not "visited")
    
    while frontier:
        # pick best node from frontier
        frontier = deque(sorted(frontier, key=lambda node: node.path_cost+node.heuristic))
        lowestCNode = frontier.popleft()

        # if state is goal state, return node
        if problem.goal_test(lowestCNode.state):
            return lowestCNode
        
        # if state in explored, continue
        if lowestCNode in explored:
            continue
        
        # create all one-step extentions of node to each child
        explored.append(lowestCNode.state)
        childrenNodes = lowestCNode.expand(problem)
        
        for child in childrenNodes:
            if child.state not in explored:
                if child.state not in frontier:
                    frontier.append(child)
                for existing in frontier:
                    if existing.state == child.state and child.path_cost < existing.path_cost:
                        frontier.remove(existing)
                        frontier.append(child)
                        break
        
    
    return Node(None, None, None, None, None) 




##########################################################
# 2. N-Queens Problem
##########################################################


class NQueensProblem(Problem):
    """
    The implementation of the class NQueensProblem related
    to Homework 2 is given for those students who were not
    able to complete it in Homework 2.
    
    Note that you do not have to use this implementation.
    Instead, you can use your own implementation from
    Homework 2.

    >>>> USE THIS IMPLEMENTATION AT YOUR OWN RISK <<<<
    >>>> USE THIS IMPLEMENTATION AT YOUR OWN RISK <<<<
    >>>> USE THIS IMPLEMENTATION AT YOUR OWN RISK <<<<
    """
    
    def __init__(self, n):
        super().__init__(tuple([-1] * n))
        self.n = n
        

    def actions(self, state):
        if state[-1] != -1:   # if all columns are filled
            return []         # then no valid actions exist
        
        valid_actions = list(range(self.n))
        col = state.index(-1) # index of leftmost unfilled column
        for row in range(self.n):
            for c, r in enumerate(state[:col]):
                if self.conflict(row, col, r, c) and row in valid_actions:
                    valid_actions.remove(row)
                    
        return valid_actions

        
    def result(self, state, action):
        col = state.index(-1) # leftmost empty column
        new = list(state[:])  
        new[col] = action     # queen's location on that column
        return tuple(new)

    
    def goal_test(self, state):
        if state[-1] == -1:   # if there is an empty column
            return False;     # then, state is not a goal state

        for c1, r1 in enumerate(state):
            for c2, r2 in enumerate(state):
                if (r1, c1) != (r2, c2) and self.conflict(r1, c1, r2, c2):
                    return False
        return True

    
    def conflict(self, row1, col1, row2, col2):
        return row1 == row2 or col1 == col2 or abs(row1-row2) == abs(col1-col2)

    
    def g(self, cost, from_state, action, to_state):
        """
        Return path cost from start state to to_state via from_state.
        The path from start_state to from_state costs the given cost
        and the action that leads from from_state to to_state
        costs 1.
        """
        return cost+1


    def h(self, state):
        """
        Returns the heuristic value for the given state.
        Use the total number of conflicts in the given
        state as a heuristic value for the state.
        """
        conflictCount = 0
        for c1, r1 in enumerate(state):
            for c2, r2 in enumerate(state):
                if (r1, c1) != (r2, c2) and self.conflict(r1, c1, r2, c2):
                    conflictCount+=1

        return conflictCount



##########################################################
# 3. Graph Problem
##########################################################



class GraphProblem(Problem):
    """
    The implementation of the class GraphProblem related
    to Homework 2 is given for those students who were
    not able to complete it in Homework 2.
    
    Note that you do not have to use this implementation.
    Instead, you can use your own implementation from
    Homework 2.

    >>>> USE THIS IMPLEMENTATION AT YOUR OWN RISK <<<<
    >>>> USE THIS IMPLEMENTATION AT YOUR OWN RISK <<<<
    >>>> USE THIS IMPLEMENTATION AT YOUR OWN RISK <<<<
    """
    
    
    def __init__(self, init_state, goal_state, graph):
        super().__init__(init_state, goal_state)
        self.graph = graph

        
    def actions(self, state):
        """Returns the list of adjacent states from the given state."""
        return list(self.graph.get(state).keys())

    
    def result(self, state, action):
        """Returns the resulting state by taking the given action.
            (action is the adjacent state to move to from the given state)"""
        return action

    
    def goal_test(self, state):
        return state == self.goal_state

    
    def g(self, cost, from_state, action, to_state):
        """
        Returns the path cost from root to to_state.
        Note that the path cost from the root to from_state
        is the give cost and the given action taken at from_state
        will lead you to to_state with the cost associated with
        the action.
        """
        return cost + self.graph.get(from_state)[to_state]
    

    def h(self, state):
        """
        Returns the heuristic value for the given state. Heuristic
        value of the state is calculated as follows:
        1. if an attribute called 'heuristics' exists:
           - heuristics must be a dictionary of states as keys
             and corresponding heuristic values as values
           - so, return the heuristic value for the given state
        2. else if an attribute called 'locations' exists:
           - locations must be a dictionary of states as keys
             and corresponding GPS coordinates (x, y) as values
           - so, calculate and return the straight-line distance
             (or Euclidean norm) from the given state to the goal
             state
        3. else
           - cannot find nor calculate heuristic value for given state
           - so, just return a large value (i.e., infinity)
        """
        try:        
            return self.graph.heuristics[state]
        except:
            try:
                xState = self.graph.locations[state][0]
                yState = self.graph.locations[state][1]
                xGoalState = self.graph.locations[self.goal_state][0]
                yGoalState = self.graph.locations[self.goal_state][1]
                return math.sqrt((xGoalState-xState)**2+(yGoalState-yState)**2)
            except:
                return "inf"





##########################################################
# 4. Eight Puzzle
##########################################################


class EightPuzzle(Problem):
    def __init__(self, init_state, goal_state=(1,2,3,4,5,6,7,8,0)):
        super().__init__(init_state, goal_state)


    def actions(self, state):
        actions = []

        # store position of blank tile as tuple
        indexBlank = state.index(0)
        posBlank = (math.floor(indexBlank/3),indexBlank%3)
        # get valid actions relative to blank tile      
        if posBlank[0]-1 >=0 and posBlank[0]-1 <=2: 
            actions.append("UP")
        if posBlank[0]+1 >=0 and posBlank[0]+1 <=2: 
            actions.append("DOWN")        
        if posBlank[1]-1 >=0 and posBlank[1]-1 <=2: 
            actions.append("LEFT")
        if posBlank[1]+1 >=0 and posBlank[1]+1 <=2: 
            actions.append("RIGHT")

        # return list of valid actions
        return actions
    

    def result(self, state, action):
        # store position of blank tile as tuple
        indexBlank = state.index(0)
        posBlank = (math.floor(indexBlank/3), indexBlank%3)
        
        # initialize variables to store value and position of tile to move
        valueAction = -1
        posAction = tuple()
        
        # determine position of tile to move
        if action == "UP":
            posAction = (posBlank[0]-1, posBlank[1])
        elif action == "DOWN":
            posAction = (posBlank[0]+1, posBlank[1])
        elif action == "LEFT":
            posAction = (posBlank[0], posBlank[1]-1)
        else:
            posAction = (posBlank[0], posBlank[1]+1)
        
        # get value and index of tile to move
        indexAction = posAction[0]*3+posAction[1]
        valueAction = state[indexAction]
        
        # return resultant state
        newState = list(state)
        newState[indexBlank] = valueAction
        newState[indexAction] = 0
        return tuple(newState)

    
    def goal_test(self, state):
        return state==self.goal_state
    

    def g(self, cost, from_state, action, to_state):
        """
        Return path cost from root to to_state via from_state.
        The path from root to from_state costs the given cost
        and the action that leads from from_state to to_state
        costs 1.
        """
        return cost+1
    

    def h(self, state):
        """
        Returns the heuristic value for the given state.
        Use the sum of the Manhattan distances of misplaced
        tiles to their final positions.
        """
        # initialize variable to keep track of distances
        sum=0
        for i in range(len(state)):
            # do not account for distance of blank tile
            if state[i]==0: continue
            posTile = (math.floor(i/3), i%3)
            indexTileGoal = self.goal_state.index(state[i])
            # indexTileGoal = state[i]-1
            posTileGoal = (math.floor(indexTileGoal/3), indexTileGoal%3)
            distance = abs(posTile[0]-posTileGoal[0]) + abs(posTile[1]-posTileGoal[1])
            sum+=distance

        return sum
