import matplotlib.pyplot as plt
import math
import numpy as np


def main():
    payment = 0
    payment_history = [payment]

    rps = ['r', 'p', 's']
    rps_history = np.array([[1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1]]
                           , np.int32)

    is_first_round = True
    last_input = 'no_input'
    end_game_key = 'e'
    info_message = f'Enter: \n{rps[0]} for rock, \n{rps[1]} for paper, \n{rps[2]} for scissors. \n{end_game_key} to end the game.'
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

        if is_first_round:
            comp_choice = np.random.choice(rps)
            is_first_round = False
            print(rps_history)
        elif last_input == rps[0]:
            comp_choice = comp_choose_and_learn(rps, rps_history, input_, 0)
        elif last_input == rps[1]:
            comp_choice = comp_choose_and_learn(rps, rps_history, input_, 1)
        else:
            comp_choice = comp_choose_and_learn(rps, rps_history, input_, 2)

        print(comp_choice)

        # sprawdzenie kto wygral
        if input_ == comp_choice:
            print(f'tie! payment: {payment}')
            payment_history.append(payment)
        elif input_ == rps[0]:
            if comp_choice == rps[1]:
                payment = evaluate_payment(False, payment, payment_history)
            elif comp_choice == rps[2]:
                payment = evaluate_payment(True, payment, payment_history)
        elif input_ == rps[1]:
            if comp_choice == rps[2]:
                payment = evaluate_payment(False, payment, payment_history)
            elif comp_choice == rps[0]:
                payment = evaluate_payment(True, payment, payment_history)
        elif input_ == rps[2]:
            if comp_choice == rps[0]:
                payment = evaluate_payment(False, payment, payment_history)
            elif comp_choice == rps[1]:
                payment = evaluate_payment(True, payment, payment_history)

        last_input = input_


def evaluate_payment(is_user_won, payment, payment_history):
    if is_user_won:
        payment -= 1
        payment_history.append(payment)
        print(f'user wins! payment: {payment}')
    else:
        payment += 1
        payment_history.append(payment)
        print(f'cmp wins! payment: {payment}')

    return payment


def comp_choose_and_learn(rps, rps_history, user_input, row_number):
    comp_guess = np.random.choice(rps, p=(rps_history[row_number] / sum(rps_history[row_number])))

    if comp_guess == rps[0]:
        comp_choice = rps[1]
    elif comp_guess == rps[1]:
        comp_choice = rps[2]
    else:
        comp_choice = rps[0]

    if user_input == rps[0]:
        rps_history[row_number][0] += 1
    elif user_input == rps[1]:
        rps_history[row_number][1] += 1
    else:
        rps_history[row_number][2] += 1

    print(rps_history)

    return comp_choice


main()
