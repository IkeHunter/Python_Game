import story_functions as sf


def main():
    player = sf.init_play()
    print()

    sf.intro(player)
    print()

    current_location = 0

    while True:

        if current_location is 12:
            print("You have obtained the chest, hurry to the Coffee Shop!")
            print()
            player.obtains_chest()

        if (player.has_chest is True) and (current_location is 11) and (player.view_health() is not 0):
            print("You win!")
            print()
            break

        if player.view_health() == 0:
            print("You have no more life, you lose")
            print()
            break

        print(sf.locations_print(int(current_location)))

        current_location, loop_break = sf.user_direction(current_location)

        if loop_break is True:
            break

        player.add_move()

        encountered = sf.location_health(player, current_location)

        print()
        print('-' * 46)
        print("| Encountered: {}, Health: {:2}, Moves: {:2} |".format(encountered, player.view_health(),
                                                                      str(player.moves)))
        print('-' * 46)



if __name__ == '__main__':
    main()
