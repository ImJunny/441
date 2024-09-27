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
    pass



    
def breadth_first_search(problem):
    # Initialization for breadth first search
    node = Node(problem.init_state)
    frontier = deque([node])         # queue: append/popleft
    explored = [problem.init_state]  # used as "visited"
    # implement the rest of generic search algorithm
    # for breadth-first search
    pass




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
        return [coin for coin in self.coins<=state]
    
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
                if row==-1 or col==-1 or row==self.n or col==self.n:break

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
                tempState = self.result((tempState),state[i])
                availableSpots = self.actions(tempState)
            else: return False
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
        pass

    
    def actions(self, state):
        pass

    
    def result(self, state, action):
        pass

    
    def goal_test(self, state):
        pass


if __name__ == "__main__":
    eight_queens = NQueensProblem(8)
    # print(eight_queens.actions((7,2,6,3,1,5,-1,-1)))
    # print(eight_queens.result((7,2,-1,-1,-1,-1,-1,-1),6))
    print(eight_queens.goal_test((7,3,0,2,5,1,6,4)))

    pass
