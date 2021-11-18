from stack import Stack

print("\nLet's play Towers of Hanoi!!!!!!!!!!")

#initialization of 3 stacks

stacks = []
left_stack = Stack("Left")
middle_stack = Stack("Middle")
right_stack = Stack("Right")
stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

#choosing how many disks you want to play with (bigger than 2)

num_disks = int(input("\nHow many disks do you want to play with?\n"))

while num_disks < 3:
  num_disks = int(input("\nEnter a number greater than or equal to 3\n"))
  
for n in range(num_disks, 0, -1):
  left_stack.push(n)
  
#optimal solution maths

num_optimal_moves = (2 ** num_disks) - 1
print('\nThe fastest you can solve this game is in {} moves'.format(num_optimal_moves))

#GET INPUT HELPER FUNCTION to choose stack
def get_input():
  
  choices = [stack.get_name()[0] for stack in stacks]
  
  while True:
 
    
    print("Choose your stack:\n")
    
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print("Enter {} for {}".format(letter, name))
      
    user_input = input("")
    
    if user_input in choices:
      
      for i in range(len(stacks)):
        
        if user_input == choices[i]:
          
          print(stacks[i].print_items())
          return stacks[i]

#every move is counted

num_user_moves = 0

#game logic :)

while right_stack.get_size() != num_disks:
  
  #current layout
  print("\n\n\n...Current Stacks...")
  for i in range(len(stacks)):
    stacks[i].print_items()
    
  while True:
    
    print("\nWhich stack do you want to move from?\n")  #self-explenatory
    from_stack = get_input()
    
    print("\nWhich stack do you want to move to?\n")
    to_stack = get_input()
    
    #checking if you can move disk
    
    if from_stack.is_empty():
      print("\n\nInvalid Move. Try Again")
      
    elif to_stack.is_empty or from_stack.peek() < to_stack():
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1
      break
    
    else:
      print("\n\nInvalid Move. Try Again")


#end of game, comparison of player's and optimal moves

print("\n\nYou completed the game in {} moves, and the optimal number of moves is {}".format(num_user_moves, num_optimal_moves))
