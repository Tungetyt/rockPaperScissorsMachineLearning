import matplotlib.pyplot as plt
import math
import numpy as np


def main():
    choices = ['r', 'p', 's']
    payment = 0
    is_first_round = True
    last_user_input = '0'
    computer_choice = ''
    rps_matrix = np.array([[1, 1, 1],
                           [1, 1, 1],
                           [1, 1, 1]]
                          , np.int32)
    while True:
        # wybor usera
        user_input = input().casefold()

        # wybor compa
        if user_input == 'end':
            print('end')
            break

        if user_input not in choices:
            continue

        if is_first_round:
            print(np.random.choice(choices))
            is_first_round = False
        elif last_user_input == choices[0]:
            computer_choice = comp_choose_and_learn(choices, rps_matrix, user_input, 0)
        elif last_user_input == choices[1]:
            computer_choice = comp_choose_and_learn(choices, rps_matrix, user_input, 1)
        else:
            computer_choice = comp_choose_and_learn(choices, rps_matrix, user_input, 2)

        # aktualizacja macierzy

        # sprawdzenie kto wygral
        if user_input == computer_choice:
            print('tie! payment: {}'.format(payment))
        elif user_input == choices[0]:
            if computer_choice == choices[1]:
                payment = evaluate_winner(False, payment)
            elif computer_choice == choices[2]:
                payment = evaluate_winner(True, payment)
        elif user_input == choices[1]:
            if computer_choice == choices[2]:
                payment = evaluate_winner(False, payment)
            elif computer_choice == choices[0]:
                payment = evaluate_winner(True, payment)
        elif user_input == choices[2]:
            if computer_choice == choices[0]:
                payment = evaluate_winner(False, payment)
            elif computer_choice == choices[1]:
                payment = evaluate_winner(True, payment)

        last_user_input = user_input
        print(user_input)

def evaluate_winner(is_user_won, payment):
    if is_user_won:
        payment -= 1
        print('user wins! payment: {}'.format(payment))
        return payment
    else:
        payment += 1
        print('cmp wins! payment: {}'.format(payment))
        return payment

# def checkWinner(userInput, computerChoice, choices):
def comp_choose_and_learn(choices, rps_matrix, user_input, row_number):
    rps_matrix[row_number]
    lowest_value_index = 0
    highest_value_index = 2
    lowest_value = rps_matrix[row_number][0]
    highest_value = 0

    for x in range(3):
        curr_num = rps_matrix[row_number][x]
        if curr_num >= highest_value:
            highest_value = curr_num
            highest_value_index = x
        if curr_num < lowest_value:
            lowest_value = curr_num
            lowest_value_index = x

    reversed_values_matrix = []

    computer_choice = np.random.choice(choices, p= (rps_matrix[row_number] / sum(rps_matrix[row_number])))
    print('cmp: {}'.format(computer_choice))
    if user_input == choices[0]:
        rps_matrix[row_number][0] += 1
    elif user_input == choices[1]:
        rps_matrix[row_number][1] += 1
    elif user_input == choices[2]:
        rps_matrix[row_number][2] += 1
    print(rps_matrix)
    return computer_choice

main()
