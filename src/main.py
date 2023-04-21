import random
from time import sleep

#this will be a list of valid inputs that the user can do that will run
#the next part of the code
valid_inputs=['ace','2','3','4','5','6','7','8','9','10','jack','queen','king']


#for the card selection output 


# sets up the win condition
#cards in the decks and players hands
card_list=[]
card_number=['ace','2','3','4','5','6','7','8','9','10','jack','queen','king']
card_suit=['heart','spade','dimond','club' ]
for i in card_suit:
  for n in card_number:
    card_list.append([i,n])

#keep track of turns
turn=1

#keeps track of player points
player_1_score=0
player_2_score=0

output=' '

player_1_hand=[]
player_2_hand=[]
#this is where it will deal the cards to the players
def deal_cards():
  for i in range(0,14,2):
    player_1_hand.append(card_list[i-1])
    player_2_hand.append(card_list[i])

#this will run the choice of the player and see if the other player list contains that.
amount_of_cards_in_hand_2=0
amount_of_cards_in_hand_1=0
def check_for_card(output):
  global turn
  global amount_of_cards_in_hand_2
  global amount_of_cards_in_hand_1
  lst=[]
  if (turn%2==1) :
    for letter in player_2_hand:
      lst.append(letter)
      #print(lst)
    for items in player_2_hand:
      amount_of_cards_in_hand_2+=1
      for i in range (1,amount_of_cards_in_hand_2):
        if player_2_hand[i][1] == card_selection:
          output='looks like you guessed right'
          return output
          
        elif player_2_hand[i][1] != card_selection:
          output='sorry go fish'
          return output

#same line of code for player one but now for player 2         
  elif turn%2==0:
    for letter in player_1_hand:
      lst.append(letter)
      #print(lst)
    for items in player_1_hand:
      amount_of_cards_in_hand_1+=1
      for i in range (1,amount_of_cards_in_hand_1):
        if player_1_hand[i][1] == card_selection:
          output='looks like you guessed right'
          return output
          
        if player_1_hand[i][1] != card_selection:
          output='sorry go fish'
          return output
  

#keep track of player name
player_name=str(input('Hi player what should I call you '))

#introduction to the game
print(' ')
sleep(2)
print('Well hello '+ player_name)
print(' ')
sleep(2)
print('welcome to go fish onlinie')
print(' ')
sleep(2)
print('your oppenet will be me ')
print(' ')
sleep(2)
print('lets start ')

#keeps track of amount of cards in players hand

#shuffle deck
for i in range(8):
  random.shuffle(card_list)

print(' ')
sleep(2)

print('lets deal the cards')
deal_cards()

print(' ')
sleep(2)
print('here are your cards '+ player_name)
print('')
print(player_1_hand)
sleep(2)
print('lets start, You go first')
#taking turn system is below uses a while stament to keep it in hear till player one
# hand and player 2 had are empty.
while player_1_hand or player_2_hand:
  
  #this is for player 1 turn 
  
  if(turn % 2 == 1):
    print('its player 1\'s turn')
    card_selection = input('what number do you want to ask for  ')     

    #while the card_selection is a invalid input it will ask the user again
    #this is used for a better user experience 

    while card_selection not in valid_inputs:
      print('sorry but you not alllowed to put that try again')
      print('')
      card_selection = input('what number do you want to ask for  ')
      print(' ')
      if card_selection in valid_inputs:
        break
    #this will become a function i think for now not yet.
    #this will check the other players hand to see if they have it or not
    check_for_card(output)
  sleep(2)
  print(check_for_card(output))
  #allows for a turn change 
  turn+=1
  



  #this is for player 2 hand 
  if(turn % 2==0):
    print('its player 2\'s turn')
    
    card_selection = input('what number do you want to ask for  ')     

    #while the card_selection is a invalid input it will ask the user again
    #this is used for a better user experience 

    while card_selection not in valid_inputs:
      print('sorry but you not alllowed to put that try again')
      print('')
      card_selection = input('what number do you want to ask for  ')
      print(' ')
      if card_selection in valid_inputs:
        break
    check_for_card(output)
  sleep(2)
  print(check_for_card(output))
  #allows for a turn change
  turn+=1