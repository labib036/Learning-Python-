print("Enter A Magic Number")
user_num =int(input())

def collatz(number):
	if number%2 ==0:
		result = number //2
	else :
		result = 3*number+1
	print(result)
	return result
while user_num !=1:
	user_num=collatz(user_num)							