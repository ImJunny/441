from hw3_utils import * 
from hw3 import *
import unittest

class TestSearches(unittest.TestCase):
    def testSearch(self):
        q = NQueensProblem(8)
        self.assertEqual(best_first_search(q).solution(), [7, 1, 3, 0, 6, 4 , 2, 5])
        self.assertEqual(uniform_cost_search(q).solution(), [0, 4, 7, 5, 2, 6, 1, 3])
        self.assertEqual(a_star_search(q).solution(), [7, 1 , 3, 0, 6, 4, 2, 5])

        romania_map = Graph(romania_roads, False)
        romania_map.locations = romania_city_positions
        g = GraphProblem('Arad', 'Bucharest', romania_map)
        self.assertEqual(best_first_search(g).solution(), ['Sibiu', 'Fagaras', 'Bucharest'])
        self.assertEqual(uniform_cost_search(g).solution(), ['Sibiu', 'Rimnicu', 'Pitesti', 'Bucharest'])
        self.assertEqual(a_star_search(g).solution(), ['Sibiu', 'Rimnicu', 'Pitesti', 'Bucharest'])

        map = Graph(best_graph_edges, True)
        map.heuristics = best_graph_h
        g = GraphProblem('S', 'G', map)
        self.assertEqual(best_first_search(g).solution(), ['B', 'G'])

        map = Graph(uniform_graph_edges, True)
        g = GraphProblem('S', 'G', map)
        self.assertEqual(uniform_cost_search(g).solution(), ['A', 'D', 'G'])

        map = Graph(a_star_graph_edges, True)
        map.heuristics = a_star_graph_admissible_h
        g = GraphProblem('S', 'G', map)
        self.assertEqual(a_star_search(g).solution(), ['B', 'C', 'G'])
        map.heuristics = a_star_graph_consistent_h
        g = GraphProblem('S', 'G', map)
        self.assertEqual(a_star_search(g).solution(), ['A', 'C', 'G'])

        e = EightPuzzle((3, 4, 1, 7, 6, 0, 2, 8, 5))
        self.assertEqual(best_first_search(e).solution(), ['LEFT', 'UP', 'RIGHT', 'DOWN', 'DOWN', 'LEFT', 'LEFT',
                                                           'UP', 'RIGHT', 'RIGHT', 'UP', 'LEFT', 'DOWN', 'DOWN',
                                                           'RIGHT', 'UP', 'LEFT', 'UP', 'RIGHT', 'DOWN', 'LEFT',
                                                           'UP', 'LEFT', 'DOWN', 'RIGHT', 'RIGHT', 'UP', 'LEFT',
                                                           'LEFT', 'DOWN', 'RIGHT', 'UP', 'LEFT', 'DOWN', 'RIGHT',
                                                           'RIGHT', 'DOWN', 'LEFT', 'LEFT', 'UP', 'UP', 'RIGHT',
                                                           'DOWN', 'LEFT', 'DOWN', 'RIGHT', 'RIGHT'])
        self.assertEqual(a_star_search(e).solution(), ['DOWN', 'LEFT', 'LEFT', 'UP', 'UP', 'RIGHT', 'RIGHT',
                                                         'DOWN', 'LEFT', 'LEFT', 'UP', 'RIGHT', 'DOWN', 'DOWN',
                                                         'RIGHT', 'UP', 'UP', 'LEFT', 'DOWN', 'RIGHT', 'DOWN'])
        
class TestNQueens(unittest.TestCase):
    def testNQueensG(self):
        eight_queens = NQueensProblem(8)
        self.assertEqual(eight_queens.g(0, (-1, -1, -1, -1, -1, -1, -1, -1), 7, (7, -1, -1, -1, -1, -1, -1, -1)), 1)
        self.assertEqual(eight_queens.g(1, (7, -1, -1, -1, -1, -1, -1, -1), 1, (7, 1, -1, -1, -1, -1, -1, -1)), 2)   
        self.assertEqual(eight_queens.g(2, (7, 1, -1, -1, -1, -1, -1, -1), 3, (7, 1, 3, -1, -1, -1, -1, -1)), 3)
        self.assertEqual(eight_queens.g(3, (7, 1, 3, -1, -1, -1, -1, -1), 0, (7, 1, 3, 0, -1, -1, -1, -1)), 4)
        self.assertEqual(eight_queens.g(4, (7, 1, 3, 0, -1, -1, -1, -1), 6, (7, 1, 3, 0, 6, -1, -1, -1)), 5)
        self.assertEqual(eight_queens.g(5, (7, 1, 3, 0, 6, -1, -1, -1), 4, (7, 1, 3, 0, 6, 4, -1, -1)), 6)
        self.assertEqual(eight_queens.g(6, (7, 1, 3, 0, 6, 4, -1, -1), 2, (7, 1, 3, 0, 6, 4, 2, -1)), 7)
        self.assertEqual(eight_queens.g(7, (7, 1, 3, 0, 6, 4, 2, -1), 5, (7, 1, 3, 0, 6, 4, 2, 5)), 8)

    def testNQueensH(self):
        eight_queens = NQueensProblem(8)
        self.assertEqual(eight_queens.h((-1, -1, -1, -1, -1, -1, -1, -1)), 56)
        self.assertEqual(eight_queens.h((7, -1, -1, -1, -1, -1, -1, -1)), 42)
        self.assertEqual(eight_queens.h((7, 1, -1, -1, -1, -1, -1, -1)), 32)
        self.assertEqual(eight_queens.h((7, 1, 3, -1, -1, -1, -1, -1)), 24)
        self.assertEqual(eight_queens.h((7, 1, 3, 0, -1, -1, -1, -1)), 16)
        self.assertEqual(eight_queens.h((7, 1, 3, 0, 6, -1, -1, -1)), 8)
        self.assertEqual(eight_queens.h((7, 1, 3, 0, 6, 4, -1, -1)), 4)
        self.assertEqual(eight_queens.h((7, 1, 3, 0, 6, 4, 2, -1)), 0)
        self.assertEqual(eight_queens.h((7, 1, 3, 0, 6, 4, 2, 5)), 0)

class TestGraph(unittest.TestCase):
    def testGraphG(self):
        romania_map = Graph(romania_roads, False)
        romania = GraphProblem('Arad', 'Bucharest', romania_map)
        self.assertEqual(romania.g(0, 'Arad', 'Zerind', 'Zerind'), 75)
        self.assertEqual(romania.g(0, 'Arad', 'Sibiu', 'Sibiu'), 140)
        self.assertEqual(romania.g(140, 'Sibiu', 'Rimnicu', 'Rimnicu'), 220)
        self.assertEqual(romania.g(220, 'Rimnicu', 'Pitesti', 'Pitesti'), 317)
        self.assertEqual(romania.g(317, 'Pitesti', 'Bucharest', 'Bucharest'), 418)

    def testGraphH(self):
        romania_map = Graph(romania_roads, False)
        romania = GraphProblem('Arad', 'Bucharest', romania_map)
        self.assertEqual(romania.h('Arad'), "inf")
        self.assertEqual(romania.h('Sibiu'), "inf")
        self.assertEqual(romania.h('Fagaras'), "inf")
        self.assertEqual(romania.h('Pitesti'), "inf")
        self.assertEqual(romania.h('Rimnicu'), "inf")
        self.assertEqual(romania.h('Bucharest'), "inf")

        romania_map = Graph(romania_roads, False)
        romania_map.locations = romania_city_positions
        
        romania = GraphProblem('Arad', 'Bucharest', romania_map)
        self.assertEqual(romania.h('Arad'), 350.2941620980858)
        self.assertEqual(romania.h('Sibiu'), 232.69937687926884)
        self.assertEqual(romania.h('Fagaras'), 154.62535367784935)
        self.assertEqual(romania.h('Pitesti'), 89.89438247187641)
        self.assertEqual(romania.h('Rimnicu'), 186.48860555004424) #wrong?
        self.assertEqual(romania.h('Bucharest'), 0.0)

        roads = dict(S = dict(A=1, B=2), A= dict(C=1),
                     B = dict(C=2), C = dict(G=100))
        roads_h = dict(S=90, A=100, B=88, C=100, G=0)
        roads_map = Graph(roads, True)
        roads_map.heuristics = roads_h
        
        problem = GraphProblem('S', 'G', roads_map)
        self.assertEqual(problem.h('S'), 90)
        self.assertEqual(problem.h('A'), 100)
        self.assertEqual(problem.h('B'), 88)
        self.assertEqual(problem.h('C'), 100)
        self.assertEqual(problem.h('G'), 0)


class TestEightPuzzle(unittest.TestCase):
    def testPuzzleInit(self):
        puzzle = EightPuzzle((1,0,6,8,7,5,4,2,3), (0,1,2,3,4,5,6,7,8))
        self.assertEqual(puzzle.init_state, (1, 0, 6, 8, 7, 5, 4, 2, 3))
        self.assertEqual(puzzle.goal_state, (0, 1, 2, 3, 4, 5, 6, 7, 8))

        puzzle = EightPuzzle((1,0,3,4,2,5,7,8,6))
        self.assertEqual(puzzle.init_state, (1, 0, 3, 4, 2, 5, 7, 8, 6))
        self.assertEqual(puzzle.goal_state, (1, 2, 3, 4, 5, 6, 7, 8, 0))

    def testPuzzleActions(self):
        puzzle = EightPuzzle((1,0,3,4,2,5,7,8,6))
        self.assertEqual(puzzle.actions((0,1,2,3,4,5,6,7,8)), ['DOWN', 'RIGHT'])
        self.assertEqual(puzzle.actions((6,3,5,1,8,4,2,0,7)), ['UP', 'LEFT', 'RIGHT'])
        self.assertEqual(puzzle.actions((4, 8, 1, 6, 0, 2, 3, 5, 7)), ['UP', 'DOWN', 'LEFT', 'RIGHT'])
        self.assertEqual(puzzle.actions((1,0,6,8,7,5,4,2,3)), ['DOWN', 'LEFT', 'RIGHT'])
        self.assertEqual(puzzle.actions((1,2,3,4,5,6,7,8,0)), ['UP', 'LEFT'])
    
    def testPuzzleResult(self):
        puzzle = EightPuzzle((1,0,3,4,2,5,7,8,6))
        self.assertEqual((3,1,2,0,4,5,6,7,8), puzzle.result((0,1,2,3,4,5,6,7,8), 'DOWN'))
        self.assertEqual((6, 3, 5, 1, 8, 4, 0, 2, 7), puzzle.result((6,3,5,1,8,4,2,0,7), 'LEFT'))
        self.assertEqual((3,4,0,7,6,1,2,8,5), puzzle.result((3,4,1,7,6,0,2,8,5), 'UP'))
        self.assertEqual((1,8,4,7,2,6,3,5,0), puzzle.result((1,8,4,7,2,6,3,0,5), 'RIGHT'))

    def testPuzzleGoal(self):
        puzzle = EightPuzzle((1,0,6,8,7,5,4,2,3), (0,1,2,3,4,5,6,7,8))
        self.assertFalse(puzzle.goal_test((6,3,5,1,8,4,2,0,7)))
        self.assertFalse(puzzle.goal_test((1,2,3,4,5,6,7,8,0)))
        self.assertTrue(puzzle.goal_test((0,1,2,3,4,5,6,7,8)))

        puzzle = EightPuzzle((1,0,3,4,2,5,7,8,6))
        self.assertFalse(puzzle.goal_test((6,3,5,1,8,4,2,0,7)))
        self.assertFalse(puzzle.goal_test((0,1,2,3,4,5,6,7,8)))
        self.assertTrue(puzzle.goal_test((1,2,3,4,5,6,7,8,0)))

    def testPuzzleG(self):
        puzzle = EightPuzzle((1,0,3,4,2,5,7,8,6))
        self.assertEqual(puzzle.g(0, (4,8,1,6,0,2,3,5,7), 'UP', (4,0,1,6,8,2,3,5,7)), 1)
        self.assertEqual(puzzle.g(3, (8,0,1,4,6,2,3,5,7), 'DOWN', (8,6,1,4,0,2,3,5,7)), 4)
        self.assertEqual(puzzle.g(8, (8,1,2,4,5,6,3,7,0), 'UP', (8,1,2,4,5,0,3,7,6)), 9)
        self.assertEqual(puzzle.g(11, (1,2,8,4,5,6,3,0,7), 'RIGHT', (1,2,8,4,5,6,3,7,0)), 12)
    
    def testPuzzleH(self):
        puzzle = EightPuzzle((1,0,3,4,2,5,7,8,6))
        self.assertEqual(puzzle.goal_state, (1, 2, 3, 4, 5, 6, 7, 8, 0))
        self.assertEqual(puzzle.h((1,2,3,4,5,0,7,8,6)), 1)
        self.assertEqual(puzzle.h((1,2,0,4,5,3,7,8,6)), 2)
        self.assertEqual(puzzle.h((1,0,2,4,5,3,7,8,6)), 3)
        self.assertEqual(puzzle.h((4,1,2,0,5,3,7,8,6)), 5)
        self.assertEqual(puzzle.h((4,1,2,6,8,0,3,5,7)), 13)

if __name__ == "__main__":
    unittest.main()
