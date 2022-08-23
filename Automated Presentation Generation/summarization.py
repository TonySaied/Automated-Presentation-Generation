import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation as pun
from heapq import nlargest
text = """
In the distant past, many people thought bats had magical powers, but times
have changed. Today, many people believe that bats are rodents, that they cannot
see, and that they are more likely than other animals to carry rabies. All of these
beliefs are mistaken. Bats are not rodents, are not blind, and are no more likely
than dogs and cats to transmit rabies. Bats, in fact, are among the least understood
and least appreciated of animals
"""

#Some words Pre-stored in the system as stop words
def sumarize(text):
    stopwords = list(STOP_WORDS)
    nlp = spacy.load('en_core_web_sm')

    doc = nlp(text)

    # Divide sentences into words and punctuation marks: ( , . )
    tokens = [token.text for token in doc]

    # Add new line in punctuation marks
    punctuation = pun

    # Dictionary for each word
    word_frequencies = {}
    for word in doc:
        if word.text.lower() not in stopwords:
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1

    #print(word_frequencies)
    max_frequency =max(word_frequencies.values())

    # Normalized frequency
    for word in word_frequencies.keys():
        word_frequencies[word]=word_frequencies[word]/max_frequency

    sentence_tokens =[sent for sent in doc.sents]
    #print(sentence_tokens)

    # Dictionary for
    sentence_scores={}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent]=word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent]+= word_frequencies[word.text.lower()]

    # 30% only
    select_length=int(len(sentence_tokens)*0.3)
    #print(select_length)

    summary= nlargest(select_length,sentence_scores,key=sentence_scores.get)
    #print(summary)

    final_summary=[word.text for word in summary]
    #print(final_summary)

    summary = ' '.join(final_summary)
    return summary