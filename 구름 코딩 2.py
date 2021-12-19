answer=[]
user_input = input()
user_input_int=int(user_input)
for i in range(0, user_input_int+1):
	for f in range(0,user_input_int+1):
		if i*f ==user_input_int:
			answer.append(i)
			answer.append(f)
answer1 = set(answer)
answer = list(answer1)
answer.sort()

for z in range(len(answer)):
	print(	answer[z] , end=' ')


