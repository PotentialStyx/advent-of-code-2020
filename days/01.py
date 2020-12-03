def part1(data):
	data = list(map(lambda x: int(x), data.split()))
	
	x = 0
	
	for i in data:
		for j in data:
			if(i+j == 2020):
				return i*j

def part2(data):
	data = set(map(lambda x: int(x), data.split()))
		
	x = 0
	
	for i in data:
		for j in data:
			if(i+j > 2019):
				continue
			for k in data:
				if(i+j+k == 2020):
					return i*j*k
