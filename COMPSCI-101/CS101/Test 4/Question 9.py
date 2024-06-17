source = [('Andrew', 'George'), ('Andrew', 'George'), ('Andrew', 'Susan')]
def vote_calculator(data):
    already_voted_list = []
    candidates = {}
    for vote in data:
        if vote[0] not in already_voted_list:
            already_voted_list.append(vote[0])
            if vote[1] not in candidates:
                candidates[vote[1]] = 1
            else:
                candidates[vote[1]] += 1
    sorted_candidates = {key: candidates[key] for key in sorted(candidates.keys())}
    for candidate in sorted_candidates:
        print(f"{candidate} {sorted_candidates[candidate]}")

def vote_calculator(data):
    already_voted = set()
    candidates = {}

    for voter, candidate in data:
        if voter not in already_voted:
            already_voted.add(voter)
            if candidate not in candidates:
                candidates[candidate] = 1
            else:
                candidates[candidate] += 1

    # Convert the dictionary to a list of tuples and sort it by votes in descending order
    sorted_candidates = []
    while candidates:
        max_candidate = max(candidates, key=candidates.get)
        sorted_candidates.append((max_candidate, candidates[max_candidate]))
        del candidates[max_candidate]

    for candidate, count in sorted_candidates:
        print(f"{candidate} {count}")



vote_calculator(source)