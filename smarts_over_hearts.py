"""
pls note code looks bad cuz this is 4 personal use!!!
PLAN
which round? extend this to the player one
enter kh1 for instance
shows table of both player and board
ill do board first tho
MISC
TOTOTO you aint smart but you've got heart!!1! - real forbidden deduction
memularity other name
will not do gui as thats way too long + slow to input :( which is what caused me to do this in the first place
"""

flag = False
rounds = []
west_cards = []
north_cards = []
east_cards = []
while not flag:
    round_no = input("round? or q to stop")
    if round_no == "q":
        flag = True
    else:
        count = 0
        while count != 3:
            card = input("enter either:\ncard, suit and player e.g. khw for 'west played king of hearts'\nc to skip the rest of cards for this round\nq to quit\ncard: ").lower()
            # sorry, i forgot regex :(
            if card[0] not in ("k","q","j","9","8","7","6","5","4","3","2") or card[:1] != "10" or card[-1] not in ("w","e","n","s") or card[-2] not in ("c","d","s","h"):
                card = input("you entered the card wrong, try again: ")
            elif card == "c":
                count = 4
            elif card == "q":
                flag = True
                break
            else:
                count += 1
                suit = card[-2]
                player = card[-1]
                if card[:1] != "10":
                    card_number_or_face = (card[0]) # int?
                else:
                    card_number_or_face = 10
                # debug
                print(suit, player, card_number_or_face)