


from luhns_algorithm import validity_test, validity_print

def test_valid_card():
    card_number_1 = "4187451822793156"  # This card number should be valid based on the Luhn algorithm
    assert validity_test(card_number_1) % 10 == 0


def test_valid_card_print():
    card_number_2 = "4187451822793156"  # Valid card number
    assert validity_print(card_number_2) == "Card is Valid!!"




def test_invalid_card():
    card_number_3 = "4187451822793157"  # This card number should be invalid based on the Luhn algorithm
    assert validity_test(card_number_3) % 10 != 0

def test_invalid_card_print():
    card_number_4 = "4187451822793157"  # Invalid card number
    assert validity_print(card_number_4) == "Card is Invalid!!"

