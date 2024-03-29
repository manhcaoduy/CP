import unittest
from typing import List


class Solution:
    def __init__(self):
        pass

    def solveSudoku(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for k in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                        if self.is_valid(board, i, j, k):
                            board[i][j] = k
                            if self.solveSudoku(board):
                                return True
                            else:
                                board[i][j] = '.'
                    return False
        return True

    def is_valid(self, board, x, y, c):
        a, b = (x // 3) * 3, (y // 3) * 3
        for i in range(9):
            if board[x][i] == c:
                return False
            if board[i][y] == c:
                return False
            if board[a + (i // 3)][b + (i % 3)] == c:
                return False
        return True


class Testing(unittest.TestCase):
    def test_all(self):
        tests = [
            {
                "input": [
                    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                    [".", "9", "8", ".", ".", ".", ".", "6", "."],
                    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                    [".", "6", ".", ".", ".", ".", "2", "8", "."],
                    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
                ],
                "answer": [
                    ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
                    ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
                    ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
                    ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
                    ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
                    ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
                    ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
                    ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
                    ["3", "4", "5", "2", "8", "6", "1", "7", "9"]
                ],
            },
        ]

        solution = Solution()

        for test in tests:
            inp, answer = test["input"], test["answer"]
            output = inp
            status = solution.solveSudoku(output)
            self.assertTrue(status, f"test fail with input {inp}")
            self.assertEqual(output, answer, f"test fail with input {inp}")


if __name__ == "__main__":
    unittest.main()
