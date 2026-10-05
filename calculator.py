while True:
	print("Choose Your Desired Function")	
	print("1.Addition")
	print("2.Subtraction")
	print("3.Multiplication")
	print("4.Division")
	print("5.Exit")

	choice=int(input())

	if choice ==1:
		print("Give Two numbers For Addition")
		a = int(input())
		b =int(input())
		add= a+b
		print("The Addition is: " + str(add))


	elif choice ==2:
		print("Provide Two Integers For Subtraction")
		a =int(input())
		b=int(input())
		sub = a-b
		print("The Subtraction is: "+ str(sub))

	elif choice ==3:
		print("Give Two Numbers For Multiplication")
		a =int(input())
		b=int(input())
		mul = a*b
		print("The Multiplication is: "+ str(mul))

	elif choice ==4:
		print("Give Two Numbers For Division")
		a =int(input())
		b=int(input())
		div=a/b
		print("The Division is: "+ str(div))

	elif choice ==5:
		print("Thank You For Calculating With Us")
		break

	else :
		print("Please Select A Valid Function (1-5)")					