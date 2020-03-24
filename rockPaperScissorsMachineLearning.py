import matplotlib.pyplot as plt
import math
import numpy as np


def main():
    choices = ['r', 'p', 's']
    payment = 0
    is_first_round = True
    last_user_input = 'no_input'
    end_game_key = 'e'
    info_message = f'Enter: \n{choices[0]} for rock, \n{choices[1]} for paper, \n{choices[2]} for scissors. \n{end_game_key} to end the game.'
    start_end_message = '-----------------------------'
    rps_matrix = np.array([[1, 1, 1],
                           [1, 1, 1],
                           [1, 1, 1]]
                          , np.int32)

    print(start_end_message)
    print(info_message)

    while True:
        # wybor usera
        print(start_end_message)
        user_input = input().casefold()

        if user_input == end_game_key:
            print('game has ended')
            print(start_end_message)
            break

        if user_input not in choices:
            print(info_message)
            continue

        if is_first_round:
            computer_choice = np.random.choice(choices)
            is_first_round = False
            print(rps_matrix)
        elif last_user_input == choices[0]:
            computer_choice = comp_choose_and_learn(choices, rps_matrix, user_input, 0)
        elif last_user_input == choices[1]:
            computer_choice = comp_choose_and_learn(choices, rps_matrix, user_input, 1)
        else:
            computer_choice = comp_choose_and_learn(choices, rps_matrix, user_input, 2)

        print(computer_choice)

        # sprawdzenie kto wygral
        if user_input == computer_choice:
            print('tie! payment: {}'.format(payment))
        elif user_input == choices[0]:
            if computer_choice == choices[1]:
                payment = evaluate_winner(False, payment, start_end_message)
            elif computer_choice == choices[2]:
                payment = evaluate_winner(True, payment, start_end_message)
        elif user_input == choices[1]:
            if computer_choice == choices[2]:
                payment = evaluate_winner(False, payment, start_end_message)
            elif computer_choice == choices[0]:
                payment = evaluate_winner(True, payment, start_end_message)
        elif user_input == choices[2]:
            if computer_choice == choices[0]:
                payment = evaluate_winner(False, payment, start_end_message)
            elif computer_choice == choices[1]:
                payment = evaluate_winner(True, payment, start_end_message)

        last_user_input = user_input


def evaluate_winner(is_user_won, payment, start_end_round_message):
    if is_user_won:
        payment -= 1
        print('user wins! payment: {}'.format(payment))
    else:
        payment += 1
        print('cmp wins! payment: {}'.format(payment))

    return payment


def comp_choose_and_learn(choices, rps_matrix, user_input, row_number):
    computer_guess = np.random.choice(choices, p=(rps_matrix[row_number] / sum(rps_matrix[row_number])))

    if computer_guess == choices[0]:
        computer_choice = choices[1]
    elif computer_guess == choices[1]:
        computer_choice = choices[2]
    else:
        computer_choice = choices[0]

    if user_input == choices[0]:
        rps_matrix[row_number][0] += 1
    elif user_input == choices[1]:
        rps_matrix[row_number][1] += 1
    elif user_input == choices[2]:
        rps_matrix[row_number][2] += 1

    print(rps_matrix)

    return computer_choice


main()
