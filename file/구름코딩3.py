user_input = input()
user_input_int=int(user_input)
answer=[]
#print(user_input_int)
i=1
while i*5 <= user_input_int:
	answer.append(i*5)
	i=i+1
	if i*5> user_input_int:
		break
s=1
while s*3 <= user_input_int:
	answer.append(s*3)
	s=s+1
	if s*3> user_input_int:
		break
#print(answer)
answer1 = set(answer) 
answer = list(answer1)
#print(answer)
result=sum(answer)
print(result)
#print(answer)