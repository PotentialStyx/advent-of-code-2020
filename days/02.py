from collections import Counter
def part1(data):
	data = data.split("\n")
	def map_it(data):
		final = []
		data = data.split(":")
		final.append(data[0].split(" ")[0])
		final.append(data[0].split(" ")[1])
		final.append(data[1][1:])
		return tuple(final)
	data = list(map(map_it,data))
	
	total = 0 
	
	for i in data:
		needed = i[0].split("-")
		
		char = i[1]
		
		password = i[2]
		
		new = Counter(password)
		
		chars = new.get(char, 0)
		
		if(chars >= int(needed[0]) and chars <= int(needed[1])):
			total += 1
		
	return total
    
def part2(data):
	
	data = data.split("\n")
	def map_it(data):
		final = [None, None, None]
		data = data.split(":")
		final[0] = data[0].split(" ")[0]
		final[1] = data[0].split(" ")[1]
		final[2] = data[1][1:]
		return tuple(final)
	data = list(map(map_it,data))
	
	total = 0
	
	for i in data:
		needed = i[0].split("-")
		
		char = i[1]
		
		password = " " + i[2]
		
		if((password[int(needed[0])] == char) ^ (password[int(needed[1])]==char)):
			total +=1
			
	return total
