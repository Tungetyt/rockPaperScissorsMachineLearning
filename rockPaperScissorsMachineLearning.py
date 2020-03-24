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

    prev_input = ''
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

        input_idx = rps.index(input_)

        if prev_input != '':
            prev_input_idx = rps.index(prev_input)
            comp_guess_idx = rps.index(np.random.choice(
                rps, p=(rps_history[prev_input_idx] / sum(rps_history[prev_input_idx]))))

            if comp_guess_idx == 0:
                comp_choice_idx = 1
            elif comp_guess_idx == 1:
                comp_choice_idx = 2
            else:
                comp_choice_idx = 0

            rps_history[prev_input_idx][input_idx] += 1
        else:
            comp_choice_idx = rps.index(np.random.choice(rps))

        print(rps[comp_choice_idx])
        print(rps_history)

        # sprawdzenie kto wygral
        if input_idx == comp_choice_idx:
            print(f'tie! payment: {payment}')
        elif (input_idx == 0 and comp_choice_idx == 1) or \
                (input_idx == 1 and comp_choice_idx == 2) or \
                (input_idx == 2 and comp_choice_idx == 0):
            payment += 1
            print(f'computer wins! payment: {payment}')
        else:
            payment -= 1
            print(f'user wins! payment: {payment}')

        payment_history.append(payment)
        prev_input = input_


main()
