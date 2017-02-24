# this definition SHOULD take a user input in and check to see if it has exclamations
# and then return the user input to the program WITHOUT the exclamations. 
#not currently working.

def exclamation_check(user_str):
	new_str = ""
	print "in the body of the definition."
	if user_str[-3:] == "!!!":
    		print "in the three tree"
		new_str = user_str[:-3]
    		print new_str
		return new_str
	elif user_str[-2:] == "!!" or user_str[-2:] == "??" or user_str[-2:] == "!?" or user_str[-2:] == "?!":
		print "in the TWO tree." 
   		new_str = user_str[:-2]
    		print new_str
		return new_str
	elif user_str[-1:] == "!" or user_str[-1:] == "?":
		print "in the ONE TREE."
    		new_str = user_str[:-1]
	    	print new_str
		return new_str
	else:
    		print "there were no triggers in the text" 
		return user_str
	

exclamation_check("Wait a minute!!")
exclamation_check("No!")
exclamation_check("That is fine.")
exclamation_check("This is the first time!!!!")
exclamation_check("Well, I will be!!!")
