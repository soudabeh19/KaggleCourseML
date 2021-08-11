# def blackjack_hand_greater_than(hand_1, hand_2):
#     """
#     Return True if hand_1 beats hand_2, and False otherwise.
    
#     In order for hand_1 to beat hand_2 the following must be true:
#     - The total of hand_1 must not exceed 21
#     - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21
    
#     Hands are represented as a list of cards. Each card is represented by a string.
    
#     When adding up a hand's total, cards with numbers count for that many points. Face
#     cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.
    
#     When determining a hand's total, you should try to count aces in the way that 
#     maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
#     the total of ['A', 'A', '9', '3'] is 14.
    
#     Examples:
#     >>> blackjack_hand_greater_than(['K'], ['3', '4'])
#     True
#     >>> blackjack_hand_greater_than(['K'], ['10'])
#     False
#     >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
#     False
#     """
#     hand_1_val = calcul(hand_1)
#     hand_2_val = calcul(hand_2)
    
#     accp_hand_1 = [i for i in hand_1_val if i <= 21]
#     accp_hand_2 = [i for i in hand_2_val if i <= 21]
#     print("this is hand_1: {}".format(accp_hand_1))
#     print("this is hand_2: {}".format(accp_hand_2))
#     if max(accp_hand_1) > max(accp_hand_2):
#         return True
#     return False

def calcul (lst):
    card_val={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':[1,11]}
    #Equvalent the set cards 
    hand_val = [card_val[i] for i in lst]

    if lst.count('A') == 2:
        A_set_values = [2, 12 ,22 ]
        val_hand_without_A = sum([i for i in hand_val if type(i)!=list])
        hand_set_values = [v + val_hand_without_A for v in A_set_values]
        
    else:
        min_val_hand = [min(i) if type(i)==list else i for i in hand_val]
        max_val_hand = [max(i) if type(i)==list else i for i in hand_val]
        hand_set_values = [sum(min_val_hand), sum(max_val_hand)]
        
    return hand_set_values

    
print(calcul (lst=['9', 'Q', '8', 'A']))
# Check your answer
q3.check()