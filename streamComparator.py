from numToText import numero_a_letras

def levenshtein(sText1, sText2):
    #### Returns levenshtein distance between two strings
    if len(sText1) < len(sText2):
        return levenshtein(sText2, sText1)

    # len(s1) >= len(s2)
    if len(sText2) == 0:
        return len(sText1)

    previous_row = range(len(sText2) + 1)
    for i, c1 in enumerate(sText1):
        current_row = [i + 1]
        for j, c2 in enumerate(sText2):
            insertions = previous_row[
                             j + 1] + 1  # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1  # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

def stringNormalizationWOSpeakers(sText):
    l_strings_remove = ["¿", "?", ",", ".", "s0: ", "s1: ", "s0:", "s1:",
                        "speaker 0: ", "speaker 1: ", "speaker 0:", "speaker 1:"]
    outText = sText.lower().replace("€", "euros").replace("%", "por ciento").replace("\n", " ")
    for s in l_strings_remove:
        outText = outText.replace(s, "")
    return outText

def stringNormalizationWithSpeakers(sText, speaker_1_id, speaker_2_id):
    speaker_1_text = ""
    speaker_2_text = ""
    for linea in sText.lower().split("\n"):
        if linea[:len(speaker_1_id)] == speaker_1_id.lower():
            speaker_1_text += linea
        if linea[:len(speaker_2_id)] == speaker_2_id.lower():
            speaker_2_text += linea

    speaker_1_text = stringNormalizationWOSpeakers(speaker_1_text)
    speaker_2_text = stringNormalizationWOSpeakers(speaker_2_text)
    return (speaker_1_text, speaker_2_text)

def stringSimilarityOverall(s1, s2):
    s1_final = stringNormalizationWOSpeakers(s1)
    s2_final = stringNormalizationWOSpeakers(s2)
    l_distance = levenshtein(s1_final, s2_final)
    length = (len(s1_final) + len(s2_final))/2
    similarity = 1 - l_distance/length

    return similarity


def stringSimilarityBySpeakers(s1, s2, t1_speaker1_id, t1_speaker2_id, t2_speaker1_id, t2_speaker2_id):
    text_1_tuple = stringNormalizationWithSpeakers(s1, t1_speaker1_id, t1_speaker2_id)
    text_2_tuple = stringNormalizationWithSpeakers(s2, t2_speaker1_id, t2_speaker2_id)

    similarity_speaker_1 = stringSimilarityOverall(text_1_tuple[0], text_2_tuple[0])
    similarity_speaker_2 = stringSimilarityOverall(text_1_tuple[1], text_2_tuple[1])
    similarity = (similarity_speaker_1 + similarity_speaker_2)/2

    return similarity

def stringSimilarity(s1, s2, t1_speaker1_id, t1_speaker2_id, t2_speaker1_id, t2_speaker2_id, num_to_text):
    s1_ = s1
    s2_ = s2
    if num_to_text:
        return (stringSimilarityOverall(convertNumsToText(s1), convertNumsToText(s2)),
                stringSimilarityBySpeakers(convertNumsToText(s1), convertNumsToText(s2), t1_speaker1_id, t1_speaker2_id, t2_speaker1_id, t2_speaker2_id))

    return(stringSimilarityOverall(s1_, s2_),
           stringSimilarityBySpeakers(s1_, s2_, t1_speaker1_id, t1_speaker2_id, t2_speaker1_id, t2_speaker2_id))

def convertNumsToText(sText):
    lNewText = []
    for word in sText.split(" "):
        try:
            float(word)
            lNewText = lNewText + [numero_a_letras(float(word))]
        except ValueError:
            lNewText = lNewText + [word]
    return " ".join(lNewText)

# text_1 = open("dat/REVOLVENTE I - transcripcion manual.txt", "r", encoding="utf-8").read()
# text_2 = open("dat/REVOLVENTE I - transcripcion IBM.txt", "r", encoding="utf-8").read()

# text_1 = open("dat/manual/02_consumo_coche-transcripcion_manual.txt", "r", encoding="ansi").read()
# text_2 = open("dat/ibm_web/02_consumo_coche-ibm_web.txt", "r", encoding="ansi").read()
#
# stringSimilarity(text_1, text_2, "s0:", "s1:", "speaker 0:", "speaker 1:", num_to_text=False)

