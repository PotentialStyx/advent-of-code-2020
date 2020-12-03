def part1(data):
	data = data.split("\n")
	return slope(data, 3, 1) # 223
	
def slope(data, x, y):
	index = [0,0]
	count = 0
	while 1:
		index[0] += x
		index[1] += y
		if(index[1] >= 323): break
		if(index[0] >= len(data[0])): index[0] -= len(data[0])
		try:
			if(data[index[1]][index[0]]=="#"):count += 1
		except: print(index[0], index[1]); exit(1)
	return count

def part2(data):
	data = data.split("\n")
	
	slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
	
	solution = 1
	for i in slopes:
		solution *= slope(data, i[0], i[1])
		
	return solution
