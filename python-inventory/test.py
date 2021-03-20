# open file with read parameter and save it, then, print it that list 
with open("rl.txt", "r") as rl:
     rl_list = rl.readlines()
     
     rl_list_as_list = []
    
     for l in rl_list:
              rl_list_as_list = l.split("\n")
	 print(rl_list_as_list)
       #print(type(rl_list))
# Apply a split to the list



# EXAMPLE: 

#"with open("grilled_cheese.txt", "r") as grilled_cheese:
#	   lines = grilled_cheese.readlines()
#
#	   quantities = []
#	   ingredients = []
#
#	   for l in lines:
#	  			 as_list = l.split(", ")
#			     quantities.append(as_list[0])
#			     ingredients.append(as_list[1].replace("\n", ""))
#
#	   print(quantities)
#	   print(ingredients)"