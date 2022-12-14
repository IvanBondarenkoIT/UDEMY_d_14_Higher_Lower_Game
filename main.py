import random
import art
from game_data import data


def random_element():
    rand_index = random.randint(0,len(data))
    return data[rand_index]


score = 0
game_ower = False
while True:
    print(art.logo)
    if game_ower:
        print(f"Sorry, that's wrong. Final score: {score}")
        break
    if score > 0:
        print(f"You're right! Current score: {score}.")
    fans_count = [0, 0]
    for i, _ in enumerate(fans_count):
        obj_ = random_element()
        if i > 0:
            print(art.vs)
        print(f"{'Compare A' if i == 0 else 'Against B'}: {obj_['name']}, {obj_['description']} from {obj_['country']}.")
        fans_count[i] = (obj_['follower_count'])

    answer = input("Who has more followers? Type 'A' or 'B':").lower()
    if (answer == 'a' and fans_count[0] >= fans_count[1]) or answer == 'b' and fans_count[1] >= fans_count[0]:
        score += 1
    else:
        game_ower = True
