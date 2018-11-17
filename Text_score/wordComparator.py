def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def stringNormalizationWOSpeakers(sText):
    l_strings_remove = ["¿", "?", ",", ".", ":", ";", "s0: ", "s1: ", "s0:", "s1:",
                        "speaker 0: ", "speaker 1: ", "speaker 0:", "speaker 1:"]
    outText = sText.lower().replace("€", "euros").replace("%", "por ciento").replace("\n", " ")
    for s in l_strings_remove:
        outText = outText.replace(s, "")
    return outText

def wordDictionary(sText):
    dWords = {}
    for word in sText.split(" "):
        if not hasNumbers(word):
            if len(word) not in dWords.keys():
                dWords[len(word)] = {}
            if word not in dWords[len(word)].keys():
                dWords[len(word)][word] = 0
            dWords[len(word)][word] = dWords[len(word)][word] + 1
    return dWords

def wordSimilarity(sText1, sText2):
    d1 = wordDictionary(stringNormalizationWOSpeakers(sText1))
    d2 = wordDictionary(stringNormalizationWOSpeakers(sText2))

    total_count = 0
    similar_count = 0

    lWordsNotFound = []

    for num_chars in d1.keys():
        for word in d1[num_chars].keys():
            if num_chars in d2.keys():
                if word in d2[num_chars].keys():
                    t1_num = d1[num_chars][word]
                    t2_num = d2[num_chars][word]
                    if t1_num < t2_num :
                        total_count += t1_num*(num_chars**2)
                        similar_count += t1_num*(num_chars**2)
                    else:
                        total_count += t1_num*(num_chars**2)
                        similar_count += t2_num*(num_chars**2)
                else:
                    total_count += 1 * (num_chars**2)
                    lWordsNotFound = lWordsNotFound + [word]
    # print("Words not found: ")
    # for word in lWordsNotFound:
    #     print("\t{}".format(word))
    return similar_count/total_count

# text_1 = open("dat/consumo coche - transcripcion manual.txt", "r", encoding="ansi").read()
# text_2 = open("dat/consumo coche - transcripcion IBM.txt", "r", encoding="ansi").read()
#
# wordSimilarity(text_1, text_2)