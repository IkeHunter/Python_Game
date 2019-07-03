import story_library as sl
import story_classes as sc

import random

locations = sl.locations


def init_play():
    player_name = input("Please enter your name to begin: ")
    player = sc.Player(player_name)
    return player


def intro(player):
    print("Welcome {0}, the objective is to obtain a chest of gold and take it to the Grand Master at the Coffee Shop"
          .format(player.name))
    print("You must do so while trying to avoid goblins, they hide in different locations, "
          "and constantly are on the move.")
    print("If a goblin sees you, you lose a some health, with {0} healths to start with.".format(player.view_health()))
    print("However, if a doctor happens to be at that location, you can gain a health.")
    print("Good luck!")


def locations_print(current):
    global locations
    location = locations[current]["name"]

    text = "You are currently next to a {0}, you can go ".format(location)
    for i in range(0, len(locations[current]["locations"])):
        if locations[current]["locations"][i] is not "Q":
            if (i + 2) < (len(locations[current]["locations"])):
                text += str(locations[current]["locations"][i]) + ", "
            elif (i + 2) == (len(locations[current]["locations"])):
                text += str(locations[current]["locations"][i])

    return text


def get_location(current):
    global locations
    loc_list = []
    for i in locations[current]["locations"]:
        loc_list.append(i)
    return loc_list


def advance_location(current, direction):
    global locations
    move_to = locations[current]["directions"][direction]
    return move_to


def random_num(max_range):
    num = random.randint(0, 10)
    num_list = []
    for i in range(0, max_range):
        num_list.append(i)
    if num in num_list:
        return True  # If the odds are right, it returns True (player loses/gains health)
    else:
        return False  # If they are wrong, it returns False (nothing happens to player)


def location_health(player, loc):
    max_num = locations[loc]["death"]

    health_bool = random_num(max_num)
    text = "Nobody"
    if health_bool is True:
        text = "Goblin"
        player.effect_health(-1)

    else:
        max_num = locations[loc]["heal"]
        health_bool = random_num(max_num)
        if health_bool is True:
            text = "Doctor"
            player.effect_health(1)

    return text


def direction_query(user_input, current_location):
    available_keys = []
    available_directions = []
    problems = False

    for i in sl.directions.values():
        available_keys.append(i["short"])
        available_keys.append(i["long"])

    for i in sl.locations[current_location]["locations"]:
        available_directions.append(i)

    if user_input in available_keys:
        for i in range(0, len(sl.directions)):
            if user_input in sl.directions[i].values():
                user_input = sl.directions[i]["short"]
                break

    if user_input not in available_keys:
        problems = True

    if (user_input in available_keys) and (user_input not in available_directions):
        problems = True

    if problems is True:
        while problems is True:
            user_input = input("Please enter a valid direction: ").upper()
            if user_input in available_keys:
                for i in range(0, len(sl.directions)):
                    if user_input in sl.directions[i].values():
                        user_input = sl.directions[i]["short"]
                        break
                problems = False
                if user_input in available_directions:
                    problems = False
                else:
                    problems = True
            else:
                problems = True

    return user_input


def user_direction(current_location):
    loop_break = False

    player_option = input("Direction: ").upper()
    player_option = direction_query(player_option, current_location)

    if player_option == "Q":
        print("Have a good day!")
        print()
        loop_break = True

    if player_option is "Q":
        return current_location, loop_break
    else:
        current_location = advance_location(current_location, player_option)  # moves to next location
        return current_location, loop_break
