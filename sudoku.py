#code to find the next empty grid

def nextCell(grid):
	for x in range(9):
		for y in range(9):
			if grid[x][y] == 0:
				return x, y
	return -1, -1


#code to check if row is possible

def row_check(grid, row, num):
	for x in range(9):
		if grid[row][x] == num:
			return False
	return True


#code to check if column is possible

def col_check(grid, col, num):
	for x in range(9):
		if grid[x][col] == num:
			return False
	return True


#code to check if grid is possible

def grid_check(grid, row, col, num):
	for i in range(row, row + 3):
		for j in range(col, col + 3):
			if grid[i][j] == num:
				return False
	return True


#to print

def print_grid(grid):
	for i in range(9):
		for j in range(9):
			print(grid[i][j], end = " ")
		print("")


#solving function

def solve_sudoku(grid):
	
	i, j = nextCell(grid)

	if i == -1:
		return True

	for num in range(1, 10):
		if row_check(grid, i, num) and col_check(grid, j, num) and grid_check(grid, i - i%3, j - j%3, num):
			grid[i][j] = num

			if solve_sudoku(grid):
				return True

			grid[i][j] = 0
	return False


#code to test, grid is hard coded
grid=[[3,0,5,4,2,0,8,1,0], [4,8,7,9,0,1,5,0,6], [0,2,9,0,5,6,3,7,4], [8,5,0,7,9,3,0,4,1], [6,1,3,2,0,8,9,5,7], [0,7,4,0,6,5,2,8,0], [0,0,0,0,0,0,0,0,0], [5,0,8,6,7,0,1,9,2], [0,9,6,5,1,2,4,0,8]]  
if(solve_sudoku(grid)):
	print_grid(grid) 
else: 
        print("No grid found")
