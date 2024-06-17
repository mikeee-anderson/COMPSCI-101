scores_list = [(1500, "Ken"), (2700, "Ryu"), (1200, "Blanka"), (1100, "Zangief")]
filename = 'mand341.txt'

def write_high_score(filename, scores_list):
    output_stream = open(filename, "w")
    output_stream.write("High Scores" + "\n")
    output_stream.write("===========" + "\n")
    output_stream.write("\n")
    sorted_scores = sorted(scores_list, key=lambda x: x[0], reverse=True)
    for score in sorted_scores[:-1]:
        score = list(score)
        output_stream.write(score[1] + "\t" + str(score[0]) + "\n")
    final_score = sorted_scores[-1]
    output_stream.write(final_score[1] + "\t" + str(final_score[0]))
    output_stream.close()






write_high_score(filename, scores_list)
print_contents(filename)