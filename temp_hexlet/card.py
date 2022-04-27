#!/usr/bin/env python

def get_hidden_card(card, dig=4):
    print(card)
    card_num = card[-4:] print(card_num)
    stars = '*' * dig
    hidden = str(card_num)
    result = stars + hidden
    return result

def main():
    print(get_hidden_card('1234123412341234'))
    print(get_hidden_card('1234123412344321', 6))

if __name__ == '__main__':
    main()

