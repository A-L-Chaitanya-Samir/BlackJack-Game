#BlackJack Game Project
import random

def deal_card(): 
    '''Returns a random card from the deck'''
    cards =[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card


def scores(cards):
    '''Take a list of cards and return the calculated score'''
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    while 11 in cards and sum(cards) > 21 :
            cards.remove(11)
            cards.append(1)
    return sum(cards) 

def compare(score_1,score_2):
    if score_1 == score_2:
        return "It's a Draw" 
    elif score_2 == 0:
        return "You Lose , opponent has BlackJack"
    elif score_1 == 0:
        return "You have won with a BlackJack"
    elif  score_1 > 21:
        return "You have Lost due to exceeding score over 21"
    elif score_2 > 21:
        return "You have Won as the Opponent's score has exceeded 21"
    elif score_1 > score_2:
        return "You have Won"
    else:
        return "You have Lost"

def play_game():
    print("Welcome to Black Jack Game !!")    
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_gameover = False

    for _ in range(2) :
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_gameover:
        user_score = scores(user_cards)
        computer_score = scores(computer_cards)

        print(f"\nYour cards:{user_cards},current score:{user_score}")
        print(f"Computer's cards:{computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score >21 :
            is_gameover = True
        else:
            user_turn = input("Type 'y' to get another card or type 'n' to pass :")
            if user_turn == "y":
                user_cards.append(deal_card())
            else:
                is_gameover = True

    computer_score = scores(computer_cards)
    if user_score <= 21:        
        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = scores(computer_cards)
    #Finale results
    print(f"\nYour final cards: {user_cards}, final score: {user_score}")
    print(f"Computer's final cards: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

#Gameplay
while input("\nDo You want to play BlackJack game ? (y/n): ").lower() == "y":
    play_game()

print("\nThanks for Playing the game!")