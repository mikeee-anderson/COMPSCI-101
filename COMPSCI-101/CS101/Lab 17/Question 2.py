score_dict = {"Peter": 25, "Jane": 32, "Kathy": 36, "Mark": 28}
def get_max_min_scores(score_dict):
    score_list = []
    for score in score_dict.values():
        score_list.append(score)
    maximum = max(score_list)
    minimum = min(score_list)
    score_tuple = (maximum, minimum)
    return score_tuple


max_score, min_score = get_max_min_scores(score_dict)
print(f"Max score: {max_score}, Min score: {min_score}")