#solution to part 1 and 2
with open('PYTHONNUM.txt','r') as f: #just create a text file with the input and save it as .txt from here: https://adventofcode.com/2021/day/1/input
    inp = [int(line.strip()) for line in f]
a = sum([1 for i,x in enumerate(inp[1:], start=1) if x > inp[i-1]]) #this is to find if the successive reading increased and then count how many of them increased
b = sum([1 for i,x in enumerate(inp[1:-2], start=1) if sum(inp[i:i+3]) > sum(inp[i-1:i+2])]) #this to add the three consecutive readings and then compare them with the succesive summation of three readings
print(f'A: {a}\nB: {b}') #result
