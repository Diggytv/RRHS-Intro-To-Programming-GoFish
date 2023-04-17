import random
from time import sleep

# sets up the win condition
#cards in the decks and players hands
card_list=[]
card_number=['ace','2','3','4','5','6','7','8','9','10','jack','queen','king']
card_suit=['heart','spade','dimond','club' ]
for i in card_suit:
  for n in card_number:
    card_list.append([i,n])



player_1_hand=[]
player_2_hand=[]
#this is where it will deal the cards to the players
def deal_cards():
    for i in range(0,14,2):
        player_1_hand.append(card_list[i-1])
        player_2_hand.append(card_list[i])

#this will run the choice of the player and see if the player 2 list contains that.
def check_for_card(card_selection):
  global turn
  global player_1_hand
  global player_2_hand
  lst=[]
  if turn%2==1 :
    for letter in player_2_hand:
      lst.appened(letter)
      print(lst)
  elif turn%2==0:
    print('Dog')
  

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


#varibles 

#keep track of turns
turn=1

#keeps track of player points
player_1_score=0
player_2_score=0

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
print(player_1_hand)
sleep(2)
print('lets start, You go first')
while player_1_hand or player_2_hand:
    if(turn % 2 == 1):
        print('its player 1 turn')
        card_selection = input('what number do you want to ask for  ')     
    if card_selection == 'ace' or card_selection == '2' or card_selection=='3' or card_selection=='4' or card_selection=='5' or card_selection=='6' or card_selection=='7' or card_selection=='8' or card_selection=='9' or card_selection=='10' or card_selection=='jack' or card_selection=='queen' or card_selection=='king':
         check_for_card(card_selection)   
