hand1 = ["8", "8", "7", "8", "7"]
hand2 = ["9", "4", "4", "9", "4"]


def compare_full_house_hands(hand1, hand2):
    # Define the ranking of cards
    card_rank = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
                 '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    # Function to extract triplet and double from a hand
    def get_triplet_and_double(hand):
        card_count = {}
        for card in hand:
            card_count[card] = card_count.get(card, 0) + 1

        triplet = double = None
        for card, count in card_count.items():
            if count == 3:
                triplet = card
            elif count == 2:
                double = card

        return triplet, double

    # Extract triplet and double from both hands
    triplet1, double1 = get_triplet_and_double(hand1)
    triplet2, double2 = get_triplet_and_double(hand2)

    # Compare triplet values
    if card_rank[triplet1] > card_rank[triplet2]:
        print(f"The full house {hand1} wins over the full house {hand2}.")
    elif card_rank[triplet1] < card_rank[triplet2]:
        print(f"The full house {hand2} wins over the full house {hand1}.")
    else:
        # Triplets are the same, compare double values
        if card_rank[double1] > card_rank[double2]:
            print(f"The full house {hand1} wins over the full house {hand2}.")
        elif card_rank[double1] < card_rank[double2]:
            print(f"The full house {hand2} wins over the full house {hand1}.")
        else:
            print("It's a draw!")

compare_full_house_hands(hand1, hand2)