import matplotlib.pyplot as plt
import numpy as np


def main():
    payment = 0
    payment_history = [payment]

    rps = ['r', 'p', 's']
    rps_history = np.array([[1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1]]
                           , np.int32)

    last_input = ''
    end_game_key = 'e'
    info_message = f'Enter: \n{rps[0]} for rock, ' \
                   f'\n{rps[1]} for paper, ' \
                   f'\n{rps[2]} for scissors, ' \
                   f'\n{end_game_key} to end the game and draw result plot.'
    start_end_message = '-----------------------------'

    print(start_end_message)
    print(info_message)

    while True:
        print(start_end_message)

        input_ = input().casefold()

        if input_ == end_game_key:
            print('game has ended')
            print(start_end_message)

            plt.plot(payment_history)
            plt.xlabel('rounds')
            plt.ylabel('payment')
            plt.show()

            break

        if input_ not in rps:
            print(info_message)
            continue

        if last_input == rps[0]:
            comp_choice = comp_choose_and_learn(rps, rps_history, input_, 0)
        elif last_input == rps[1]:
            comp_choice = comp_choose_and_learn(rps, rps_history, input_, 1)
        elif last_input == rps[2]:
            comp_choice = comp_choose_and_learn(rps, rps_history, input_, 2)
        else:
            comp_choice = np.random.choice(rps)

        print(comp_choice)
        print(rps_history)

        # sprawdzenie kto wygral
        if input_ == comp_choice:
            print(f'tie! payment: {payment}')
        elif (input_ == rps[0] and comp_choice == rps[1]) or \
                (input_ == rps[1] and comp_choice == rps[2]) or \
                (input_ == rps[2] and comp_choice == rps[0]):
            payment += 1
            print(f'computer wins! payment: {payment}')
        else:
            payment -= 1
            print(f'user wins! payment: {payment}')

        payment_history.append(payment)
        last_input = input_


def comp_choose_and_learn(rps, rps_history, user_input, row):
    comp_guess = np.random.choice(rps, p=(rps_history[row] / sum(rps_history[row])))

    if comp_guess == rps[0]:
        comp_choice = rps[1]
    elif comp_guess == rps[1]:
        comp_choice = rps[2]
    else:
        comp_choice = rps[0]

    if user_input == rps[0]:
        rps_history[row][0] += 1
    elif user_input == rps[1]:
        rps_history[row][1] += 1
    else:
        rps_history[row][2] += 1

    return comp_choice


main()
