def addition(a, b):                                       #Addition Function
	result = a + b
	return result

def substraction(a, b):                                   #Substraction Function
	result = a - b
	return result

def multiplication(a, b):                                 #Multiplication Function
	result = a * b
	return result

def division(a, b):                                       #Division Function
	result = a / b
	return result

try:
	
	while True:                                              #Loop
		print("Choose Your Desired Function")	
		print("1.Addition")
		print("2.Subtraction")
		print("3.Multiplication")
		print("4.Division")
		print("5.Exit")

		choice=int(input())                                #Input   

		if choice == 1:
			print ("Give Two numbers For Addition")
			a = int(input())
			b = int(input())
			add = addition(a, b)							#Addition Called
			print ("The Addition is : " + str(add))			#Addition Print


		elif choice == 2:
			print("Provide Two Integers For Subtraction")
			a = int(input())
			b = int(input())
			sub = substraction(a, b)						#Substraction Called
			print("The Substraction is : " + str(sub)) 		#Substraction Print
 
		elif choice == 3:
			print("Give Two Numbers For Multiplication")
			a = int(input())
			b = int(input())
			mul = multiplication(a, b)						#Multiplication Called
			print("The Multiplication is: "+ str(mul))		#Multiplication Print

		elif choice == 4:
			print("Give Two Numbers For Division")
			a = int(input())
			b = int(input())
			div= division(a, b)								#Division Called
			print("The Division is: "+ str(div))			#Divison Print

		elif choice == 5:
			print("Thank You For Calculating With Us")
			break

		else :
			print("Please Select A Valid Function (1-5)")					
except:
	print("Please Provide A Number")			
	


