answer=[]
def 약수구하기(n):
	n=int(n)
	for i in range(0, n+1):
		for f in range(0,n+1):
			if i*f ==n:
				answer.append(i)
				answer.append(f)
입력값=input()

약수구하기(입력값)
answer1 = set(answer)
answer = list(answer1)
print(answer)
answer.sort()
for s in answer:
	print(s, end = ' ')
#https://level.goorm.io/exam/43255/%EC%95%BD%EC%88%98-%EA%B5%AC%ED%95%98%EA%B8%B0/quiz/1

