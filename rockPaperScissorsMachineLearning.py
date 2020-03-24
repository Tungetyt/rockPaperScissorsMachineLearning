import matplotlib.pyplot as plt
import math
import numpy as np


def main():
    rps = ['r', 'p', 's']
    payment = 0
    payment_history = [payment]
    is_first_round = True
    last_user_input = 'no_input'
    end_game_key = 'e'
    info_message = f'Enter: \n{rps[0]} for rock, \n{rps[1]} for paper, \n{rps[2]} for scissors. \n{end_game_key} to end the game.'
    start_end_message = '-----------------------------'
    rps_matrix = np.array([[1, 1, 1],
                           [1, 1, 1],
                           [1, 1, 1]]
                          , np.int32)
    print(start_end_message)
    print(info_message)

    while True:
        print(start_end_message)
        user_input = input().casefold()

        if user_input == end_game_key:
            print('game has ended')
            print(start_end_message)
            plt.plot(payment_history)
            plt.xlabel('rounds')
            plt.ylabel('payment')
            plt.show()
            break

        if user_input not in rps:
            print(info_message)
            continue

        if is_first_round:
            computer_choice = np.random.choice(rps)
            is_first_round = False
            print(rps_matrix)
        elif last_user_input == rps[0]:
            computer_choice = comp_choose_and_learn(rps, rps_matrix, user_input, 0)
        elif last_user_input == rps[1]:
            computer_choice = comp_choose_and_learn(rps, rps_matrix, user_input, 1)
        else:
            computer_choice = comp_choose_and_learn(rps, rps_matrix, user_input, 2)

        print(computer_choice)

        # sprawdzenie kto wygral
        if user_input == computer_choice:
            print(f'tie! payment: {payment}')
            payment_history.append(payment)
        elif user_input == rps[0]:
            if computer_choice == rps[1]:
                payment = evaluate_winner(False, payment, payment_history)
            elif computer_choice == rps[2]:
                payment = evaluate_winner(True, payment, payment_history)
        elif user_input == rps[1]:
            if computer_choice == rps[2]:
                payment = evaluate_winner(False, payment, payment_history)
            elif computer_choice == rps[0]:
                payment = evaluate_winner(True, payment, payment_history)
        elif user_input == rps[2]:
            if computer_choice == rps[0]:
                payment = evaluate_winner(False, payment, payment_history)
            elif computer_choice == rps[1]:
                payment = evaluate_winner(True, payment, payment_history)

        last_user_input = user_input


def evaluate_winner(is_user_won, payment, payment_history):
    if is_user_won:
        payment -= 1
        payment_history.append(payment)
        print(f'user wins! payment: {payment}')
    else:
        payment += 1
        payment_history.append(payment)
        print(f'cmp wins! payment: {payment}')

    return payment


def comp_choose_and_learn(rps, rps_matrix, user_input, row_number):
    computer_guess = np.random.choice(rps, p=(rps_matrix[row_number] / sum(rps_matrix[row_number])))

    if computer_guess == rps[0]:
        computer_choice = rps[1]
    elif computer_guess == rps[1]:
        computer_choice = rps[2]
    else:
        computer_choice = rps[0]

    if user_input == rps[0]:
        rps_matrix[row_number][0] += 1
    elif user_input == rps[1]:
        rps_matrix[row_number][1] += 1
    else:
        rps_matrix[row_number][2] += 1

    print(rps_matrix)

    return computer_choice


main()
