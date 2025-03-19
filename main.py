from tabnanny import check
from art import logo, vs
from game_data import data
import random

print(logo)

def compare_a(data1):
    account_name = data1["name"]
    account_followers= data1["follower_count"]
    account_description = data1["description"]
    account_country= data1["country"]
    return f"{account_name}, {account_description}, from {account_country}"

def compare_followers(u_choice,a_followers,b_followers):
    if a_followers > b_followers:
        if u_choice == "a":
            return True
        else:
            return False
    elif a_followers < b_followers:
        if u_choice == "b":
            return True
        else:
            return False


score = 0
game_over = False
account_b = random.choice(data)

while not game_over:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    a_followers_count= account_a["follower_count"]
    b_followers_count= account_b["follower_count"]

    print(f"Compare A: {compare_a(account_a)}")
    print(vs)
    print(f"Against B: {compare_a(account_b)}")


    user_input = str(input("Who has more followers? Type 'A' or 'B': ")).lower()

    is_correct= compare_followers(user_input,a_followers_count,b_followers_count)

    if is_correct:
        score +=1
        print(f"You are right! Current score: {score}")

    else:
        game_over = True
        print(f"Sorry, that's wrong. Final score: {score}.")