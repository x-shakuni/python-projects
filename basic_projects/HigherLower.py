import random


def comparison(d1, d2, guess):
    if d1>d2:
        return guess == "a"
    else:
        return guess == "b"


def home_page(d1, d2):

    print(f"Compare A: {d1["name"]}, a {d1["occupation"]}, from {d1['country']}")
    print("""
    ██    ██ ███████ 
    ██    ██ ██      
    ██    ██ ███████ 
     ██  ██       ██ 
      ████   ███████                    
     """)
    print(f"Compare B: {d2["name"]}, a {d2["occupation"]}, from {d2['country']}")


print('''                                                                    
    ██╗  ██╗██╗ ██████╗ ██╗  ██╗███████╗██████╗         ██╗      ██████╗ ██╗    ██╗███████╗██████╗ 
    ██║  ██║██║██╔════╝ ██║  ██║██╔════╝██╔══██╗        ██║     ██╔═══██╗██║    ██║██╔════╝██╔══██╗
    ███████║██║██║  ███╗███████║█████╗  ██████╔╝        ██║     ██║   ██║██║ █╗ ██║█████╗  ██████╔╝
    ██╔══██║██║██║   ██║██╔══██║██╔══╝  ██╔══██╗        ██║     ██║   ██║██║███╗██║██╔══╝  ██╔══██╗
    ██║  ██║██║╚██████╔╝██║  ██║███████╗██║  ██║        ███████╗╚██████╔╝╚███╔███╔╝███████╗██║  ██║
    ╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝        ╚══════╝ ╚═════╝  ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝                                                                                            
    ''')

data = [
    {"name": "Cristiano Ronaldo", "follower_count": 673, "occupation": "Footballer", "country": "Portugal"},
    {"name": "Lionel Messi", "follower_count": 512, "occupation": "Footballer", "country": "Argentina"},
    {"name": "Selena Gomez", "follower_count": 414, "occupation": "Musician and Actress", "country": "United States"},
    {"name": "Kylie Jenner", "follower_count": 390, "occupation": "Media Personality", "country": "United States"},
    {"name": "Dwayne Johnson", "follower_count": 390, "occupation": "Actor and Wrestler", "country": "United States"},
    {"name": "Ariana Grande", "follower_count": 371, "occupation": "Musician and Actress", "country": "United States"},
    {"name": "Kim Kardashian", "follower_count": 352, "occupation": "Media Personality", "country": "United States"},
    {"name": "Beyoncé", "follower_count": 307, "occupation": "Musician", "country": "United States"},
    {"name": "Khloé Kardashian", "follower_count": 298, "occupation": "Media Personality", "country": "United States"},
    {"name": "Justin Bieber", "follower_count": 292, "occupation": "Musician", "country": "Canada"},
    {"name": "Kendall Jenner", "follower_count": 284, "occupation": "Model", "country": "United States"},
    {"name": "Taylor Swift", "follower_count": 280, "occupation": "Musician", "country": "United States"},
    {"name": "Virat Kohli", "follower_count": 275, "occupation": "Cricketer", "country": "India"},
    {"name": "Jennifer Lopez", "follower_count": 246, "occupation": "Musician and Actress", "country": "United States"},
    {"name": "Neymar Jr", "follower_count": 234, "occupation": "Footballer", "country": "Brazil"},
    {"name": "Nicki Minaj", "follower_count": 229, "occupation": "Musician", "country": "Trinidad and Tobago"},
    {"name": "Kourtney Kardashian", "follower_count": 215, "occupation": "Media Personality", "country": "United States"},
    {"name": "Miley Cyrus", "follower_count": 210, "occupation": "Musician and Actress", "country": "United States"},
    {"name": "Katy Perry", "follower_count": 201, "occupation": "Musician", "country": "United States"},
    {"name": "Zendaya", "follower_count": 176, "occupation": "Actress", "country": "United States"},
    {"name": "Kevin Hart", "follower_count": 176, "occupation": "Comedian and Actor", "country": "United States"},
    {"name": "Cardi B", "follower_count": 161, "occupation": "Musician", "country": "United States"},
    {"name": "LeBron James", "follower_count": 154, "occupation": "Basketball Player", "country": "United States"},
    {"name": "Rihanna", "follower_count": 145, "occupation": "Musician", "country": "Barbados"},
    {"name": "Drake", "follower_count": 139, "occupation": "Musician", "country": "Canada"}
]
game_should_continue = True
score = 0


while game_should_continue:
    data1 = random.choice(data)
    data2 = random.choice(data)

    while data1 == data2:
        data2 = random.choice(data)
    home_page(data1, data2)

    choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    is_correct = comparison(data1["follower_count"], data2["follower_count"], choice)

    if is_correct:
        score += 1
        print(f"\nCorrect! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"\nSorry, that's wrong. Final score: {score}")

