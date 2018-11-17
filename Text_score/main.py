from Text_score.streamComparator import stringSimilarity as sS
from Text_score.wordComparator import wordSimilarity as wS

man_trans_filename = "08_territorial-transcripcion_manual"
aut_trans_filename = "09_cantabria_digi-transcripcion_autom"

text_man = open("data/{}.txt".format(man_trans_filename), "r", encoding="utf-8").read()
text_aut = open("data/{}.txt".format(aut_trans_filename), "r", encoding="utf-8").read()

print("#### {} ####".format(man_trans_filename.split("-")[0]))

stream_similarity_results = sS(text_man, text_aut, "s0:", "s1:", "speaker 0:", "speaker 1:", num_to_text=True)

print("\t1 speaker similarity: {}".format(stream_similarity_results[0]))
print("\t2 speakers similarity: {}".format(stream_similarity_results[1]))

word_similarity_result = wS(text_man, text_aut)

print("\tWord similarity: {}".format(word_similarity_result))
