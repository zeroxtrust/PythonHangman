#By ZeroTrustX
#Version 1: B1/B2 English Words with Timer and Levels

print("Welcome to the Hang man game") # Welcome message

file_name = 'hang_man_game.txt'
import random
import time

word_list_b1_b2 = [
('apple', 'a fruit that is usually red or green'),
('banana', 'a long, yellow fruit with soft, sweet flesh'),
('cat', 'a small domesticated carnivorous mammal'),
('dog', 'a domesticated carnivorous mammal'),
('elephant', 'a large herbivorous mammal with a trunk'),
('fly', 'an insect with wings'),
('goat', 'a domesticated animal known for its milk and horns'),
('hen', 'a female chicken'),
('ant', 'a small insect that lives in colonies'),
('bat', 'a flying mammal with echolocation'),
('dog', 'a domesticated carnivorous mammal'),
('eel', 'a long, snake-like fish'),
('fly', 'an insect with wings'),
('goat', 'a domesticated animal known for its milk and horns'),
('hen', 'a female chicken'),
('jay', 'a bird of the crow family'),
('kite', 'a bird of prey or a toy flown in the wind'),
('lamb', 'a young sheep'),
('moth', 'an insect similar to a butterfly'),
('newt', 'a small amphibian'),
('owl', 'a nocturnal bird of prey'),
('pig', 'a domesticated mammal kept for meat'),
('rat', 'a rodent similar to a mouse but larger'),
('seal', 'a marine mammal with flippers'),
('toad', 'a tailless amphibian similar to a frog'),
('vole', 'a small rodent resembling a mouse'),
('wasp', 'a stinging insect similar to a bee'),
('yak', 'a large, long-haired domesticated bovid'),
('bee', 'an insect known for producing honey'),
('cub', 'a young carnivorous mammal, like a bear or lion'),
('dove', 'a bird symbolizing peace'),
('elk', 'a large deer with impressive antlers'),
('frog', 'a tailless amphibian with a short body'),
('goose', 'a large waterfowl'),
('hawk', 'a bird of prey'),
('ibis', 'a wading bird with a long, curved beak'),
('jackal', 'a wild dog found in Africa and Asia'),
('koala', 'an arboreal Australian marsupial'),
('lion', 'a large wild cat'),
('mole', 'a small burrowing mammal'),
('numbat', 'a small, termite-eating Australian marsupial'),
('otter', 'a semi-aquatic mammal'),
('puma', 'a large wild cat'),
('quail', 'a small game bird'),
('robin', 'a small songbird'),
('shark', 'a large marine fish known for its sharp teeth'),
('tiger', 'a large wild cat with a striped coat'),
('urial', 'a wild sheep with large horns'),
('viper', 'a venomous snake'),
('wolf', 'a wild carnivorous mammal'),
('x-ray fish', 'a small transparent fish'),
('zebra', 'a wild horse with black-and-white stripes'),
('asp', 'a small venomous snake'),
('bison', 'a large wild ox'),
('crow', 'a large perching bird with a black plumage'),
('duck', 'a waterfowl with a broad, flat bill'),
('egret', 'a heron with white plumage'),
('fawn', 'a young deer'),
('gnu', 'a large antelope'),
('hare', 'a fast-running mammal'),
('ibex', 'a wild goat with long, curved horns'),
('jaguar', 'a large wild cat'),
('kiwi', 'a flightless bird native to New Zealand'),
('lemur', 'a primate native to Madagascar'),
('moose', 'a large deer with broad, flat antlers'),
('narwhal', 'a marine mammal with a long, spiral tusk'),
('ocelot', 'a small wild cat'),
('penguin', 'a flightless seabird'),
('quokka', 'a small marsupial native to Australia'),
('raven', 'a large bird of the crow family'),
('sheep', 'a domesticated ruminant animal'),
('toucan', 'a bird known for its large colorful beak'),
('uakari', 'a small South American monkey'),
('vulture', 'a large bird of prey'),
('walrus', 'a large marine mammal with tusks'),
('xerus', 'an African ground squirrel'),
('yak', 'a long-haired bovid found in the Himalayas'),
('zebu', 'a domesticated cattle with a hump'),
('alpaca', 'a domesticated South American camelid'),
('buffalo', 'a large bovine animal'),
('camel', 'a desert-dwelling animal with humps'),
('dingo', 'a wild dog found in Australia'),
('ermine', 'a small weasel with a white winter coat'),
('flamingo', 'a tall wading bird with pink feathers'),
('gazelle', 'a small, graceful antelope'),
('heron', 'a long-legged wading bird'),
('ibex', 'a wild goat with long, curved horns'),
('jellyfish', 'a gelatinous marine animal'),
('koala', 'an arboreal Australian marsupial'),
('leopard', 'a large wild cat with a spotted coat'),
('manatee', 'a large aquatic mammal'),
('narwhal', 'a marine mammal with a long, spiral tusk'),
('okapi', 'a forest-dwelling relative of the giraffe'),
('peacock', 'a bird known for its colorful tail feathers'),
('quagga', 'an extinct subspecies of the plains zebra'),
('racoon', 'a nocturnal mammal known for its dexterous front paws'),
('salamander', 'an amphibian resembling a lizard'),
('tapir', 'a large, herbivorous mammal'),
('urchin', 'a small, spiny marine animal'),
('vicuna', 'a wild South American camelid'),
('weasel', 'a small carnivorous mammal'),
('xerus', 'an African ground squirrel'),
('yabby', 'an Australian freshwater crayfish'),
('zebu', 'a domesticated cattle with a hump'),
('angelfish', 'a brightly colored tropical fish'),
('baboon', 'a large primate found in Africa and Arabia'),
('cheetah', 'the fastest land animal'),
('dolphin', 'an intelligent marine mammal'),
('elephant', 'the largest land animal'),
('falcon', 'a bird of prey known for its speed'),
('gecko', 'a small lizard with adhesive toe pads'),
('hippo', 'a large, semi-aquatic mammal'),
('iguana', 'a large, arboreal lizard'),
('jellyfish', 'a gelatinous marine animal'),
('kangaroo', 'a large marsupial native to Australia'),
('lemur', 'a primate native to Madagascar'),
('meerkat', 'a small mongoose found in Africa'),
('numbat', 'a small, termite-eating Australian marsupial'),
('octopus', 'a marine mollusk with eight arms'),
('platypus', 'a semi-aquatic mammal with a duck-bill'),
('quail', 'a small game bird'),
('rhinoceros', 'a large mammal with one or two horns on its snout'),
('squid', 'a marine mollusk with ten arms'),
('tapir', 'a large, herbivorous mammal'),
('urchin', 'a small, spiny marine animal'),
('viper', 'a venomous snake'),
('walrus', 'a large marine mammal with tusks'),
('xerus', 'an African ground squirrel'),
('yak', 'a large, long-haired domesticated bovid'),
('zebra', 'a wild horse with black-and-white stripes'),
('anaconda', 'a large, non-venomous snake found in South America'),
('buffalo', 'a large bovine animal'),
('cheetah', 'the fastest land animal'),
('dolphin', 'an intelligent marine mammal'),
('elephant', 'the largest land animal'),
('falcon', 'a bird of prey known for its speed'),
('gecko', 'a small lizard with adhesive toe pads'),
('hippopotamus', 'a large, semi-aquatic mammal'),
('impala', 'a medium-sized antelope found in Africa'),
('jaguar', 'a large wild cat'),
('kangaroo', 'a large marsupial native to Australia'),
('lemur', 'a primate native to Madagascar'),
('meerkat', 'a small mongoose found in Africa'),
('narwhal', 'a marine mammal with a long, spiral tusk'),

    # Add the remaining words and definitions here
]


# Function to load users from a file
def load_users(file_name):
    users = {}
    try:
        with open(file_name, 'r') as file:
            for line in file:
                username, password, nickname = line.strip().split(',')
                users[username] = {'password': password, 'nickname': nickname, 'scores': []}
    except FileNotFoundError:
        pass
    return users


# Function to save users to a file
def save_users(users, file_name):
    with open(file_name, 'w') as file:
        for username, details in users.items():
            file.write(f"{username},{details['password']},{details['nickname']}\n")


# Function to register a new user
def register_user(users):
    username = input("Enter a new username: ")
    if username in users:
        print("Username already exists. Please choose another username.")
        return
    password = input("Enter a password: ")
    nickname = input("Enter a nickname: ")
    users[username] = {'password': password, 'nickname': nickname, 'scores': []}
    print("User registered successfully!")


# Function to login a user
def login_user(users):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users and users[username]['password'] == password:
        print("Login successful!")
        return username
    else:
        print("Invalid username or password.")
        return None


# Function to display the menu
def display_menu():
    print("\nMenu:")
    print("1. Start a new game")
    print("2. View high scores")
    print("3. Play in team")
    print("4. Logout")
    return input("Choose an option: ")


# Function to get a random word and its definition
def get_random_word_b1_b2():
    return random.choice(word_list_b1_b2)


# Function to display the word with guessed letters revealed
def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])


# Main game logic for B1/B2 words with timer and levels
def play_game_b1_b2(users, user):
    level = 1
    while True:
        print(f"\nLevel {level}")
        word, definition = get_random_word_b1_b2()
        guessed_letters = []
        incorrect_guesses = 0
        max_incorrect = 5
        while incorrect_guesses < max_incorrect and set(word) != set(guessed_letters):
            print(display_word(word, guessed_letters))
            start_time = time.time()
            guess = input("Enter your guess (you have 30 seconds): ").lower()
            guess_time = time.time() - start_time

            if guess_time > 30:
                print("Time's up! You took too long to guess.")
                incorrect_guesses += 1
            elif guess in guessed_letters:
                print("You already guessed that letter.")
            elif guess in word:
                guessed_letters.append(guess)
            else:
                incorrect_guesses += 1
                print(f"Wrong guess. {max_incorrect - incorrect_guesses} attempts remaining.")

        if set(word) == set(guessed_letters):
            print(f"Congratulations! You guessed the word: {word}")
            print(f"Definition: {definition}")
            score = (len(word) * 10) - int(time.time() - start_time)
            users[user]['scores'].append(score)
            print(f"Your score for this level is: {score}")
            level += 1
        else:
            print(f"Game over. The word was: {word}")
            print(f"Definition: {definition}")
            break

    return users


# Function to play game in teams
def play_in_team(users):
    team_size = input("Enter the number of players in the team: ")
    if team_size.isnumeric():
        team_scores = [0] * int(team_size)
        for i in range(int(team_size)):
            user = input(f"Enter username for player {i + 1}: ")

            if user not in users:
                print(f"User {user} not found. Please register first.")
                return
            users = play_game_b1_b2(users, user)
            team_scores[i] = sum(users[user]['scores'])
        print("Team scores:")
        for i in range(int(team_size)):
            print(f"Player {i + 1}: {team_scores[i]}")
    else:
        print("Please enter a valid number")


# Function to display high scores
def display_high_scores(users):
    print("\nHigh Scores:")
    scores = [(details['nickname'], score) for user, details in users.items() for score in details['scores']]
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    for nickname, score in scores[:10]:
        print(f"{nickname}: {score}")


# Main function to run the program
def main():
    users = load_users('users.txt')
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            register_user(users)
        elif choice == '2':
            user = login_user(users)
            if user:
                while True:
                    option = display_menu()
                    if option == '1':
                        users = play_game_b1_b2(users, user)
                    elif option == '2':
                        display_high_scores(users)
                    elif option == '3':
                        play_in_team(users)
                    elif option == '4':
                        break
                    else:
                        print("Invalid option. Please try again.")
        elif choice == '3':
            save_users(users,'users.txt')
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
 main()
