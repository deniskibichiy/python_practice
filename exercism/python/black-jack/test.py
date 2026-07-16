def value_of_card(card):
    """Determine the scoring value of a card.

    Parameters:
        card (str): The given card.

    Returns:
        int: The value of a given card.  See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1
        3.  '2' - '10' = numerical value.
    
    if card == "J" == "Q" == "K":
        return 10
    if card == "A":
        return 1
    if type(int(card)) == int:
        return int(card)
    print(value_of_card('J'))
    print(value_of_card('4'))
    print(value_of_card('A'))
    """
    if card == "J":
        return 10
    if card == "Q":
        return 10
    if card == "K":
        return 10
    if card == "A":
        return 1
    card = int(card)
    if 1 < card <= 10:
        return card
print(value_of_card("J"))
print(value_of_card("K"))
print(value_of_card("A"))
print(value_of_card("3"))
print(value_of_card("5")) 
def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

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