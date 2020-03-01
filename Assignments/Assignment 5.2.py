largest = None
smallest = None
while True:
    	num = input("Enter a number: ")
    	if num == "done" : 
    		break
    	n = int(num)
    	elif largest < n :
        	largest = n
    	elif smallest == None or smallest > n :
    		smallest = n 
    	else:
    		print("Invalid input")
    
print("Maximum is",largest)
print ("Minimum is",smallest)
