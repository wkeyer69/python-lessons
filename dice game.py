import random 

def roll():
    min_value = 1 
    max_value = 6 
    roll = random.randint(min_value, max_value)
    return roll

while True:
    players = input("Enter players 2/4: ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break

print(players)

max_score = 50 
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    
    for player1 in range(players):
        print("\nplayer ", player1 + 1, " turn has started")
        print("your score: ", player_scores[player1], "\n")
        current_score = 0 
        while True:
            should_roll = input("would you like to roll (y)")
            if should_roll.lower() != "y":
                break
     
            value = roll()
            if value == 1:
                current_score = 0
                print("you rolled a 1, turn done")
                break
                
            else: 
                current_score += value 
                print("you rolled a ", value)

            print("current score: ", current_score) 
        player_scores[player1] += current_score
        print("your final score: ", player_scores[player1])

max_score = max(player_scores) 
winning1 = player_scores.index(max_score)  
print("player numeber ", winning1 + 1, "is the winnder with a score of", max_score)




    


    

                                




