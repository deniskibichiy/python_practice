
def value_of_card(card):
    """Determine the scoring value of a card.

    Parameters:
        card (str): The given card.

    Returns:
        int: The value of a given card.  See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1
        3.  '2' - '10' = numerical value.
    """
    if card in ("J", "K", "Q"):
        return 10
    if card == "A":
        return 1
    card = int(card)
    if 1 < card <= 10:
        return card

def higher_card(card_one, card_two):
    """
    Determine which card has a higher value in the hand.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1
        3.  '2' - '10' = numerical value.

    Returns:
        str or tuple: The resulting tuple contains both cards if they are of equal value.
    """
    if value_of_card(card_one) > value_of_card(card_two):
        return card_one
    if value_of_card(card_one) < value_of_card(card_two):
        return card_two
    return card_one,card_two
print(higher_card('Q', '10'))

def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an upcoming ace card.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 11 (if already in hand)
        3.  '2' - '10' = numerical value.

    Returns:
        int: Either 1 or 11, which is the value of the upcoming ace card.
    """
    # RETURN ONE IF:
        #VALUE OF CARD_ONE + CARD_TWO + 11 > 21
        #oBTAIN VALUE OF CARD_ONE AND CARD_TWO
    card_one_value = value_of_card(card_one)
    card_two_value = value_of_card(card_two)
    if card_one_value == 1:
        card_one_value = 11
    if card_one_value + card_two_value + 11 > 21:
        return 1
    # RETURN 11 IF VALUE OF CARD_ONE + CARD_TWO + 11 < 21
    return 11
print(value_of_ace('6', 'K'))
print(value_of_ace('7', '3'))
print("test here")
print(value_of_ace('2', 'A'))


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 11 (if already in hand)
        3.  '2' - '10' = numerical value.

    Returns:
        bool: Is the hand is a blackjack (two cards worth 21).
    """
    qualifying_cards = ("J", "K", "Q", "10")
    if card_one in qualifying_cards and value_of_card(card_two) == 1:
        return True
    if card_two in qualifying_cards and value_of_card(card_one) == 1:
        return True
    return False
print(is_blackjack('10', '9'))
print(is_blackjack('A', 'K'))

def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.

   Returns:
        bool: Can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    return value_of_card(card_one) == value_of_card(card_two)
print(can_split_pairs('Q', 'K'))
print(can_split_pairs('10', 'A'))
def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.

    Returns:
        bool: Can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    value_of_card_one = value_of_card(card_one)
    value_of_card_two = value_of_card(card_two)
    result = value_of_card_one + value_of_card_two
    return result == 9 or result == 10 or result == 11
print (can_double_down('A', '9'))
print(can_double_down('10', '2'))