straight_up_bet = 0
split_bet = 0
corner_bet = 0
street_bet = 0
six_line_bet = 0
red_color_bet = 0
black_color_bet = 0
even_number_bet = 0
odd_number_bet = 0
big_number_bet = 0
small_number_bet = 0
first_column_bet = 0
second_column_bet = 0
third_column_bet = 0
first_dozen_bet = 0
second_dozen_bet = 0
third_dozen_bet = 0

total_bet = 0

total_payout = []

straight_up_payout = 0
split_payout = 0
corner_payout = 0
street_payout = 0
six_line_payout = 0
red_color_payout = 0
black_color_payout = 0
even_number_payout = 0
odd_number_payout = 0
big_number_payout = 0
small_number_payout = 0
first_column_payout = 0
second_column_payout = 0
third_column_payout = 0
first_dozen_payout = 0
second_dozen_payout = 0
third_dozen_payout = 0

bet_number = 0
winning_number = 0
winning_even_chance = 0
bet_even_chance = 0
winning_dozen = 0
bet_dozen = 0
winning_column = 0
bet_column = 0

# inner payouts

for straight_up_payout in total_payout:
    if bet_number == winning_number:
        straight_up_payout += straight_up_bet * 35

for split_payout in total_payout:
    if bet_number == winning_number:
        split_payout += split_bet * 17

for corner_payout in total_payout:
    if bet_number == winning_number:
        corner_payout += corner_bet * 8

for street_payout in total_payout:
    if bet_number == winning_number:
        street_payout += street_bet * 11

for six_line_payout in total_payout:
    if bet_number == winning_number:
        six_line_payout += six_line_bet * 5

# outer payouts

for red_color_payout in total_payout:
    if bet_even_chance == winning_even_chance:
        red_color_payout += red_color_bet

for black_color_payout in total_payout:
    if bet_even_chance == winning_even_chance:
        black_color_payout += black_color_bet

for even_number_payout in total_payout:
    if bet_even_chance == winning_even_chance:
        even_number_payout += even_number_bet

for odd_number_payout in total_payout:
    if bet_even_chance == winning_even_chance:
        odd_number_payout += odd_number_bet

for big_number_payout in total_payout:
    if bet_even_chance == winning_even_chance:
        big_number_payout += big_number_bet

for small_number_payout in total_payout:
    if bet_even_chance == winning_even_chance:
        small_number_payout += small_number_bet

for first_column_payout in total_payout:
    if bet_even_chance == winning_even_chance:
        first_column_payout += first_column_bet * 2

for second_column_payout in total_payout:
    if bet_even_chance == winning_even_chance:
        second_column_payout += second_column_bet * 2

for third_column_payout in total_payout:
    if bet_even_chance == winning_even_chance:
        third_column_payout += third_column_bet * 2

for first_dozen_payout in total_payout:
    if bet_even_chance == winning_even_chance:
        first_dozen_payout += first_dozen_bet * 2

for second_dozen_payout in total_payout:
    if bet_even_chance == winning_even_chance:
        second_dozen_payout += second_dozen_bet * 2

for third_dozen_payout in total_payout:
    if bet_even_chance == winning_even_chance:
        third_dozen_payout += third_dozen_bet * 2

total_payout.append(straight_up_payout)
total_payout.append(split_payout)
total_payout.append(corner_payout)
total_payout.append(street_payout)
total_payout.append(six_line_payout)
total_payout.append(red_color_payout)
total_payout.append(black_color_payout)
total_payout.append(even_number_payout)
total_payout.append(odd_number_payout)
total_payout.append(big_number_payout)
total_payout.append(small_number_payout)
total_payout.append(first_column_payout)
total_payout.append(second_column_payout)
total_payout.append(third_column_payout)
total_payout.append(first_dozen_payout)
total_payout.append(second_dozen_payout)
total_payout.append(third_dozen_payout)

print(sum(total_payout))
