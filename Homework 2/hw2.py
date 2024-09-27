########################################################
#
# CMPSC 441: Homework 2
#
########################################################


student_name = 'Type your full name here'
student_email = 'Type your email address here'


########################################################
# Import
########################################################


from hw2_utils import *
from collections import deque


##########################################################
# 1. Uninformed Any-Path Search Algorithms
##########################################################
def depth_first_search(problem):
    # Initialization for depth first search
    node = Node(problem.init_state)
    frontier = deque([node])         # stack: append/pop
    explored = [problem.init_state]  # used as "visited"
    # implement the rest of generic search algorithm
    # for depth-first search

    # find solution while states exist in frontier
    while frontier:
        # base case; return node that contains solution path
        if problem.goal_test(node.state):
            return node
        node = frontier.pop()
        
        # get children from current node
        childrenNodes = node.expand(problem)
        
        # add more nodes to frontier if not explored
        for child in childrenNodes:
            if problem.goal_test(child.state):
                return child
            if child.state not in explored:
                frontier.append(child)
                explored.append(child.state)

    return Node(None, None, None)


def breadth_first_search(problem):
    # Initialization for breadth first search
    node = Node(problem.init_state)
    frontier = deque([node])         # queue: append/popleft
    explored = [problem.init_state]  # used as "visited"
    # implement the rest of generic search algorithm
    # for breadth-first search
    
    while frontier:
        # pop first node from frontier
        node = frontier.popleft()
        
        # base case; return node that contains solution path
        if problem.goal_test(node.state):
            return node

        # get children from current node
        childrenNodes = node.expand(problem)

        # add more nodes to frontier if not explored
        for child in childrenNodes:
            if problem.goal_test(child.state):
                return child
            if child.state not in explored:
                frontier.append(child)
                explored.append(child.state)

    return Node(None, None, None)


##########################################################
# 2. Coin Problem
##########################################################
class CoinPuzzle(Problem):
    # This is a subclass of the class Problem.
    #   See hw2_utils.py for what each method does.
    # You need to orverride the following methods
    #   so that it works for CoinPuzzle

    def __init__(self, init_state, goal_state, coins):
        super().__init__(init_state, goal_state)
        self.coins = coins

    def actions(self, state):
        return [coin for coin in self.coins if coin<=state]
    
    def result(self, state, action):
        return state-action
    
    def goal_test(self, state):
        if state==self.goal_state: return True
        return False


##########################################################
# 3. N-Queens Problem
##########################################################
class NQueensProblem(Problem):
    # This is a subclass of the class Problem.
    #   See hw2_utils.py for what each method does.
    # You need to orverride the following methods
    #   so that it works for NQueenProblem
    
    def __init__(self, n):
        super().__init__(tuple([-1] * n))
        self.n = n
    
    def actions(self, state):
        # board is 2D array
        board = [['.']*self.n for i in range(self.n)]
        # queens is array of (row,col) for queen positions
        queens = []
        # lastCol to determine last column to look at empty rows
        lastCol=-1
         
        # method to mark diagonals of each queen
        def fillDiagonals(tup,rowAdd,colAdd):
            row = tup[0]
            col = tup[1]
            while True:
                board[row][col]="x"
                row+=rowAdd
                col+=colAdd
                if row==-1 or col==-1 or row==self.n or col==self.n: break

        # mark all queens diagonals, verticals, and horizontals
        for i, num in enumerate(state):
            if num!=-1:
                tup=(num,i)
                queens.append(tup)
                fillDiagonals(tup,1,1)
                fillDiagonals(tup,1,-1)
                fillDiagonals(tup,-1,1)
                fillDiagonals(tup,-1,-1)
                for j in range(self.n):
                    board[tup[0]][j]="x"
                    board[j][tup[1]]="x"
            else:
                lastCol=i
                break

        # get all empty rows
        result=[]
        for row in range(self.n):
            if board[row][lastCol]!="x":
                result.append(row)

        return result


    def result(self, state, action):
        # temp array to store states
        temp = []
        # fill next -1 with value of action
        for num in state:
            if num!=-1:
                temp.append(num)
            else:
                temp.append(action)
                break
        # turn temp array into tuple
        temp+=[-1]*(self.n-len(temp))
        return tuple(temp)
    
                        
    def goal_test(self, state):
        # tempState to keep track of current state
        tempState = tuple([-1]*self.n)
        availableSpots = self.actions(tempState)

        # check if the next value in state is in self.action 
        # array, updating tempState every time
        for i in range(len(state)):
            if state[i] in availableSpots:
                tempState = self.result((tempState), state[i])
                availableSpots = self.actions(tempState)
            else: 
                return False
        return True


##########################################################
# 4. Graph Problem
##########################################################
class GraphProblem(Problem):
    # This is a subclass of the class Problem.
    #   See hw2_utils.py for what each method does.
    # You need to orverride the following methods
    #   so that it works for GraphProblem

    def __init__(self, init_state, goal_state, graph):
        super().__init__(init_state, goal_state)
        self.graph=graph
    
    def actions(self, state):
        return [city for city in self.graph.edges[state].keys()]
    
    def result(self, state, action):
        return action
    
    def goal_test(self, state):
        return self.goal_state==state


if __name__ == "__main__":

    old_british_coins_1 = [120,30,24,12,6,3,1]
    old_british_coins_2 = [1,3,6,12,24,30,120]
    us_coins_1 = [100,50,25,10,5,1]
    us_coins_2 = [1,5,10,25,50,100]

    p = CoinPuzzle(48, 0, old_british_coins_1)
    d = depth_first_search(p); print(d.solution())
    # [1, 1, 3, 6, 12, 24, 1]
    b = breadth_first_search(p); print(b.solution())
    # [24, 24]

    p = CoinPuzzle(48, 0, old_british_coins_2)
    print(depth_first_search(p).solution())
    # [30, 12, 6]
    (breadth_first_search(p).solution())
    # [24, 24]

    p = CoinPuzzle(48, 0, us_coins_1)
    d = depth_first_search(p); print(d.solution())
    # [1, 1, 1, 1, 5, 10, 1, 1, 1, 1, 25]
    b=breadth_first_search(p); print(b.solution())
    # [25, 10, 10, 1, 1, 1]

    p = CoinPuzzle(48, 0, us_coins_2)
    print(depth_first_search(p).solution())
    # [25, 10, 10, 1, 1, 1]
    print(breadth_first_search(p).solution())
    [1, 1, 1, 10, 10, 25]

    #You can also test...

    q = NQueensProblem(1)
    d = depth_first_search(q); print(d.solution())
    # [0]
    b = breadth_first_search(q); print(b.solution())
    # [0]

    d = depth_first_search(NQueensProblem(2)); print(d.solution())
    # None
    b = breadth_first_search(NQueensProblem(2)); print(b.solution())
    # None

    print(depth_first_search(NQueensProblem(4)).solution())
    # [2, 0, 3, 1]
    print(breadth_first_search(NQueensProblem(4)).solution())
    # [1, 3, 0, 2]

    print(depth_first_search(NQueensProblem(8)).solution())
    # [7, 3, 0, 2, 5, 1, 6, 4]
    print(breadth_first_search(NQueensProblem(8)).solution())
    # [0, 4, 7, 5, 2, 6, 1, 3]
    
    romania_map = Graph(romania_roads, False)

    g = GraphProblem('Arad', 'Bucharest', romania_map)
    d = depth_first_search(g); print(d.solution())
    # ['Timisoara', 'Lugoj', 'Mehadia', 'Drobeta', 'Craiova', 'Pitesti', 'Bucharest']
    b = breadth_first_search(g); print(b.solution())
    # ['Sibiu', 'Fagaras', 'Bucharest']
    g = GraphProblem('Urziceni', 'Arad', romania_map)
    print(depth_first_search(g).solution())
    # ['Bucharest', 'Fagaras', 'Sibiu', 'Arad']
    print(breadth_first_search(g).solution())
    #['Bucharest', 'Fagaras', 'Sibiu', 'Arad']
    
    g = GraphProblem('Urziceni', 'NoName', romania_map)
    depth_first_search(g).solution() #fix
    sol = depth_first_search(g).solution()
    print(sol)
    # None

    pass