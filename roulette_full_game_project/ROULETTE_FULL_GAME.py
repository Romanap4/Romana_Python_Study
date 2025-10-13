# VARIABLES LIST:

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

class Bet:
    class Bet_inside_bets:
        def __init__(self, straight_up_bet, split_bet, corner_bet, street_bet, six_line_bet):
            self.straight_up_bet = straight_up_bet
            self.split_bet = split_bet
            self.corner_bet = corner_bet
            self.street_bet = street_bet
            self.six_line_bet = six_line_bet

    class Bet_outside_bets:
        def __init__(self, red_color_bet, black_color_bet, even_number_bet, odd_number_bet, big_number_bet, small_number_bet,
                     first_column_bet, second_column_bet, third_column_bet, first_dozen_bet, second_dozen_bet, third_dozen_bet):
            self.red_color_bet = red_color_bet
            self.black_color_bet = black_color_bet
            self.even_number_bet = even_number_bet
            self.odd_number_bet = odd_number_bet
            self.big_number_bet = big_number_bet
            self.small_number_bet = small_number_bet
            self.first_column_bet = first_column_bet
            self.second_column_bet = second_column_bet
            self.third_column_bet = third_column_bet
            self.first_dozen_bet = first_dozen_bet
            self.second_dozen_bet = second_dozen_bet
            self.third_dozen_bet = third_dozen_bet

class Payout:
    class Payout_inside_bets:
        def __init__(self, straight_up_payout, split_payout, corner_payout, street_payout, six_line_payout):
            self.straight_up_payout = straight_up_payout
            self.split_payout = split_payout
            self.corner_payout = corner_payout
            self.street_payout = street_payout
            self.six_line_payout = six_line_payout

    class Payout_outside_bets:
        def __init__(self, red_color_payout, black_color_payout, even_number_payout, odd_number_payout, big_number_payout, 
                     small_number_payout, first_column_payout, second_column_payout, third_column_payout, first_dozen_payout,
                     second_dozen_payout, third_dozen_payout):
            self.red_color_payout = red_color_payout
            self.black_color_payout = black_color_payout
            self.even_number_payout = even_number_payout
            self.odd_number_payout = odd_number_payout
            self.big_number_payout = big_number_payout
            self.small_number_payout = small_number_payout
            self.first_column_payout = first_column_payout
            self.second_column_payout = second_column_payout
            self.third_column_payout = third_column_payout
            self.first_dozen_payout = first_dozen_payout
            self.second_dozen_payout = second_dozen_payout
            self.third_dozen_payout = third_dozen_payout
