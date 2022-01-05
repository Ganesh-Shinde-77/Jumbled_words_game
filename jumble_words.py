# A two plater game where random words are generated in jumbled manner and the player has to guess what the word is!

import random

def choose():
    words = ["ganesh", "jayesh", "computer" , "science" , "journal" , "condition" , "recursion" , "autometa", "computing"]
    pick = random.choice(words)
    return pick

def jumbled(word):
    jumbled_word = "".join(random.sample(word, len(word)))
    return jumbled_word

def thanks(p1n,p2n,p1p,p2p):
    # printing scores
    print(f"{p1n}, your score is {p1p}")
    print(f"{p2n}, your score is {p2p}")
    
    # checking winner
    if(p1p>p2p):
        print(f"{p1n} is the winner! \n")
    if(p2p>p1p):
        print(f"{p2n} is the winner! \n")
    else:
        print("It's a draw \n")

    # printing thank you message    
    print("Thank you for playing!")
    print("Have a nice day :) ")
    
def play():

    # taking input and setting initial scores and turns
    p1_name = input("Player 1, please enter your name :" )
    p2_name = input("Player 2, please enter your name : ")
    p1_points = 0
    p2_points = 0
    turn = 0
    
    while(1):

        # player 1's turn
        if(turn%2==0):

            # creating question
            picked_word = choose()
            qn = jumbled(picked_word)
            
            # printing question
            print(f"{p1_name}'s turn")
            print(qn)
            answer = input("Your guess : ")
            
            # verifying answer 
            if(answer==picked_word):
                p1_points = p1_points + 1
                print("Congrats! Your answer is right!" )
                print("Your score is :", p1_points)
            else:
                print("Better luck next time.")
                print("Correct answer was : ", picked_word)
                
            turn =  turn+1
            
            # Confirming continuation of game
            cont= int(input("Type 1 to continue or 0 to quit : "))
            if(cont==0):
                thanks(p1_name,p2_name,p1_points,p2_points)
                break
                
        # player 2's turn        
        if(turn%2==1):

            # creating question
            picked_word = choose()
            qn = jumbled(picked_word)
            
            # printing question
            print(f"{p2_name}'s turn")
            print(qn)
            answer = input("Your guess : ")
            
            # verifying answer 
            if(answer==picked_word):
                p2_points = p2_points + 1
                print("Congrats! Your answer is right!")
                print("Your score is :", p2_points)
            else:
                print("Better luck next time.")
                print("Correct answer was : ", picked_word)
                
            turn = turn+1
            
            # Confirming continuation of game
            cont= int(input("Type 1 to continue or 0 to quit : "))
            if(cont==0):
                thanks(p1_name,p2_name,p1_points,p2_points)
                break
                
        
        
play()