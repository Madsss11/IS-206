print "How much cheese do you have?"
cheese_count = raw_input()
print "How many crackers do you have?"
boxes_of_crackers = raw_input()
print "How many crackers is used per cheese?"
crackers_per_cheese = raw_input()
crackers_eaten = (int (boxes_of_crackers) / int (crackers_per_cheese))
enough_cheese = (int (crackers_eaten) <= int (cheese_count))


print "It is", enough_cheese, "that it is enough cheese today!"