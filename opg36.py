from sys import exit




def pool_room():
	print "This pool is full of chlorin. You need to get up!"
	print "How do you do that swim or get rescued?"
	
	next = raw_input("> ")
	if "swim" in next:
		exit("You get out, but are heavily damaged. Good job!!")
	elif "rescued" in next:
		dead("After stabbing their friend, they wont help you.")
	else:
		print "Swim or die!"
	
		
		
def waterpark_room():
	print "There is a waterpark in here."
	print "The waterpark has a lot of waterslides."
	print "The guards is in front of both slides."
	print "How are you going to move one guard?"
	print "pay or stab?"
	guard_moved = False
	
	while True:
		next = raw_input("> ")
		
		if next == "pay":
			dead("The guard looks at you and laughs.")
		elif next == "stab" and not guard_moved:
			print "The guard bleeds and has moved from the waterslide. You can slide down now."
			guard_moved = True
		elif next == "stab" and guard_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif next == "slide" and guard_moved:
			pool_room()
		else:
			print "I got no idea what that means."



def lasertag_room():
			print "here your see the a lastertagfield."
			print "You have to get past the kids without getting hit"
			print "do you rambo your way through or bargain?"
			
			next = raw_input("> ")
			
			if "rambo" in next:
				exit("You shoot the kids and earn your freedom!")
			elif "bargain" in next:
				dead("Kids don't listen to reason!")
			else:
				lastertag_room()
				
				
def dead(why):
	print why, "Too bad"
	exit(0)
	
	
def start():
	print "You are in a dark room."
	print "There is two doors 1 and 2."
	print "Which one do you take?"
	
	next = raw_input("> ")
	
	if next == "1":
		waterpark_room()
	elif next == "2":
		lasertag_room()
	else:
		dead("You settle in the dark room and mutates into an hermaphrodite to start your own colony")
		
		
start()
		
