

score_dict = {"Ryu": 500, "Ken": 300, "Gouki": 700, "Dhalsim": 250}
def print_high_scores(score_dict):
    sorted_pairs = sorted(score_dict.items(), key=lambda x: (-x[1], x[0]))
    # sort by score then alphabetical for text

    print("--------------------")
    print("Name           Score")
    print("--------------------")
    for pair in sorted_pairs:
        spacer_multiplier = 15 - len(pair[0])
        spacer = " " * spacer_multiplier
        print(f"{pair[0]}{spacer}{pair[1]}")
    print("--------------------")

print_high_scores(score_dict)
print()