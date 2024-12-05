#By Yousef Elzidani
#Version 2: Information Technology and Cybersecurity Words with Timer and Levels


print("Welcome to the Hang man game") # Welcome message

import random
import time

word_list_it_cybersecurity = [
('firewall', 'a network security system that monitors and controls incoming and outgoing network traffic'),
('encryption', 'the process of converting information or data into a code to prevent unauthorized access'),
('phishing', 'a method of trying to gather personal information using deceptive e-mails and websites'),
('malware', 'software that is specifically designed to disrupt, damage, or gain unauthorized access to a computer system'),
('ransomware', 'a type of malware that threatens to publish the victim\'s data or perpetually block access to it unless a ransom is paid'),
('antivirus', 'software designed to detect and destroy computer viruses'),
('authentication', 'the process of verifying the identity of a user or device'),
('backdoor', 'a method of bypassing normal authentication in a system'),
('biometrics', 'the measurement and statistical analysis of people’s physical and behavioral characteristics'),
('botnet', 'a network of private computers infected with malicious software and controlled as a group'),
('breach', 'an incident where data is unintentionally exposed'),
('certificate', 'a digital document used to prove the ownership of a public key'),
('cipher', 'an algorithm for performing encryption or decryption'),
('compliance', 'adherence to laws, regulations, guidelines, and specifications relevant to its business processes'),
('confidentiality', 'the property of information being accessible only to those authorized to have access'),
('cryptography', 'the practice of securing information by transforming it into a secure format'),
('cyberattack', 'an attempt to damage, disrupt, or gain unauthorized access to computer systems, networks, or devices'),
('cybersecurity', 'the practice of protecting systems, networks, and programs from digital attacks'),
('data integrity', 'the accuracy and consistency of stored data'),
('decryption', 'the process of converting encrypted data back into its original form'),
('denial-of-service', 'an attack that aims to make a machine or network resource unavailable to its intended users'),
('digital forensics', 'the process of uncovering and interpreting electronic data'),
('encryption', 'the process of converting information or data into a code to prevent unauthorized access'),
('exploit', 'a piece of software or a sequence of commands that takes advantage of a bug or vulnerability'),
('firewall', 'a network security system that monitors and controls incoming and outgoing network traffic'),
('hacker', 'a person who uses computers to gain unauthorized access to data'),
('hash function', 'a function that converts an input into a fixed-size string of characters, which is typically a hash code'),
('honeypot', 'a system intended to mimic likely targets of cyberattacks to detect, deflect, or study hacking attempts'),
('incident response', 'the approach taken to manage the aftermath of a security breach or attack'),
('information security', 'the practice of protecting information by mitigating information risks'),
('insider threat', 'a security risk that comes from within the organization being attacked'),
('integrity', 'the assurance that information is trustworthy and accurate'),
('intrusion detection', 'the process of monitoring a network or systems for malicious activity or policy violations'),
('IP spoofing', 'the creation of Internet Protocol packets with a forged source IP address'),
('keylogger', 'a type of surveillance software that has the capability to record every keystroke you make'),
('malware', 'software that is specifically designed to disrupt, damage, or gain unauthorized access to a computer system'),
('man-in-the-middle', 'an attack where the attacker secretly intercepts and relays messages between two parties'),
('network security', 'policies and practices adopted to prevent and monitor unauthorized access, misuse, modification, or denial of a computer network and network-accessible resources'),
('penetration testing', 'the practice of testing a computer system, network, or web application to find security vulnerabilities'),
('phishing', 'the fraudulent attempt to obtain sensitive information by disguising as a trustworthy entity'),
('privacy', 'the right of individuals to keep their personal information from being disclosed'),
('ransomware', 'a type of malicious software designed to block access to a computer system until a sum of money is paid'),
('risk assessment', 'the identification and analysis of relevant risks to achieve the objectives'),
('rootkit', 'a set of software tools that enable an unauthorized user to gain control of a computer system without being detected'),
('social engineering', 'the use of deception to manipulate individuals into divulging confidential or personal information'),
('spam', 'irrelevant or unsolicited messages sent over the internet'),
('SSL certificate', 'a digital certificate that provides authentication for a website and enables an encrypted connection'),
('threat', 'a potential cause of an unwanted incident'),
('trojan horse', 'a type of malware that is often disguised as legitimate software'),
('two-factor authentication', 'a method of confirming a user’s identity by using two different components'),
('vulnerability', 'a weakness in a system that can be exploited by a threat'),
('virus', 'a type of malicious software that, when executed, replicates by inserting copies of itself into other programs'),
('VPN', 'a Virtual Private Network that extends a private network across a public network'),
('worm', 'a type of malware that spreads copies of itself from computer to computer'),
('zero-day', 'a vulnerability in software that is unknown to the vendor'),
('access control', 'the selective restriction of access to a place or other resource'),
('adware', 'software that automatically displays or downloads advertising material'),
('anomaly detection', 'the identification of items, events, or observations which do not conform to an expected pattern'),
('asset management', 'the systematic process of developing, operating, maintaining, and selling assets'),
('audit trail', 'a record showing who has accessed a computer system and what operations they have performed during a given period'),
('authentication token', 'a physical device used to gain access to an electronically restricted resource'),
('authorization', 'the function of specifying access rights to resources'),
('availability', 'the property of being accessible and usable upon demand by an authorized entity'),
('backdoor', 'a method of bypassing normal authentication in a system'),
('biometric authentication', 'a security process that relies on the unique biological characteristics of an individual'),
('blacklist', 'a list of entities that are denied access to certain privileges, services, or recognition'),
('blockchain', 'a decentralized digital ledger used to record transactions across many computers'),
('brute force attack', 'a trial and error method used to decode encrypted data such as passwords'),
('certificate authority', 'an entity that issues digital certificates'),
('ciphertext', 'the result of encryption performed on plaintext using an algorithm'),
('clickjacking', 'a technique used to trick users into clicking on something different from what they perceive'),
('cloud security', 'a set of policies, technologies, and controls to protect data, applications, and the associated infrastructure of cloud computing'),
('cyber hygiene', 'practices and steps that users of computers and other devices take to maintain system health and improve online security'),
('cyber threat intelligence', 'information about threats and threat actors that helps mitigate harmful events in cyberspace'),
('data breach', 'an incident where information is stolen or taken from a system without the knowledge or authorization of the system’s owner'),
('data encryption', 'the process of converting data into a code to prevent unauthorized access'),
('data loss prevention', 'a strategy for ensuring that end users do not send sensitive or critical information outside the corporate network'),
('decryption key', 'a piece of information, usually a string of numbers or letters, used to decrypt encoded data'),
('digital certificate', 'an electronic document used to prove the ownership of a public key'),
('digital signature', 'a mathematical scheme for verifying the authenticity of digital messages or documents'),
('distributed denial-of-service', 'an attack where multiple systems flood the bandwidth or resources of a targeted system'),
('DNS spoofing', 'a form of computer security hacking in which corrupt DNS data is introduced into the cache of a DNS resolver'),
('end-to-end encryption', 'a method of secure communication that prevents third-parties from accessing data while it’s transferred from one end system to another'),
('ethical hacking', 'the practice of bypassing system security to identify potential data breaches and threats in a network'),
('exploit kit', 'a toolkit used to exploit security holes in software applications to spread malware'),
('federated identity', 'a means of linking a user’s identity across multiple separate identity management systems'),
('firewall', 'a network security system that monitors and controls incoming and outgoing network traffic based on predetermined security rules'),
('GDPR', 'General Data Protection Regulation, a regulation in EU law on data protection and privacy'),
('hash', 'the result of a hash function, which is a function that converts an input into a fixed-size string of characters'),
('identity management', 'the process of identifying, authenticating, and authorizing individuals or groups of people to have access to applications, systems, or networks'),
('incident management', 'the process of identifying, analyzing, and correcting hazards to prevent a future re-occurrence'),
('information assurance', 'the practice of managing information-related risks'),
('Internet of Things', 'the network of physical devices that are embedded with sensors, software, and other technologies to connect and exchange data with other devices and systems over the internet'),
('intrusion prevention system', 'a system that monitors network and/or system activities for malicious activity'),
('IP address', 'a numerical label assigned to each device connected to a computer network that uses the Internet Protocol for communication'),
('key management', 'the process of managing cryptographic keys in a cryptosystem'),
('malvertising', 'the use of online advertising to spread malware'),
('network monitoring', 'the use of a system that constantly monitors a computer network for slow or failing components'),
('network segmentation', 'the practice of splitting a computer network into subnetworks, each being a network segment'),
('patch management', 'the process of managing a network of computers by regularly performing patch deployment to keep computers up to date'),
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
def get_random_word_it_cybersecurity():
    return random.choice(word_list_it_cybersecurity)


# Function to display the word with guessed letters revealed
def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])


# Main game logic for IT and Cybersecurity words with timer and levels
def play_game_it_cybersecurity(users, user):
    level = 1
    while True:
        print(f"\nLevel {level}")
        word, definition = get_random_word_it_cybersecurity()
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
            users = play_game_it_cybersecurity(users, user)
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
    sorted(scores, key=lambda x: x[1], reverse=True)
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
                        users = play_game_it_cybersecurity(users, user)
                    elif option == '2':
                        display_high_scores(users)
                    elif option == '3':
                        play_in_team(users)
                    elif option == '4':
                        break
                    else:
                        print("Invalid option. Please try again.")
        elif choice == '3':
            save_users(users, 'users.txt')
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
