# this definition SHOULD take a user input in and check to see if it has exclamations
# and then return the user input to the program WITHOUT the exclamations. 
# for some reason it isn't working properly, hence all the prints. 

# also, here on github I'm not able to save it at a 2 space indent, as it just reverts 
# to an 8 space indent, which makes the code look all funky. Don't know why it won't save. 

def exclamation_check(user_str):
  print "in the body of the definition."
	if user_str[-3:] == "!!!":
    print "in the three tree"
		user_str = user_str[:-3]
    print user_str
		return user_str
	elif user_str[-2:] == "!!" or user_str[-2:] == "??" or user_str[-2:] == "!?" or user_str[-2:] == "?!":
		print "in the TWO tree." 
    user_str = user_str[:-2]
    print user_str
		return user_str
	elif user_str[-1:] == "!" or user_str[-1:] == "?":
		print "in the ONE TREE."
    user_str = user_str[:-1]
    pring user_str
		return user_str
	else:
    print "there were no triggers in the text" 
		return user_str
