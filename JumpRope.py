import random

def display_game(player_position, rope_position):
    game_display = [" "] * 10
    game_display[player_position] = "P"
    game_display[rope_position] = "R"
    print(" ".join(game_display))

def main():
    player_position = 4
    rope_position = random.randint(0, 9)
    
    while True:
        display_game(player_position, rope_position)
        
        action = input("Press 'a' to move left, 'd' to move right, or 'q' to quit: ")
        
        if action == 'a':
            player_position = max(player_position - 1, 0)
        elif action == 'd':
            player_position = min(player_position + 1, 9)
        elif action == 'q':
            print("Game over!")
            break
        
        rope_position = (rope_position + 1) % 10
        
        if player_position == rope_position:
            print("You touched the rope! Game over!")
            break

if __name__ == "__main__":
    print("Jump Rope Game")
    print("Try to jump over the rope by moving left or right.")
    main()
