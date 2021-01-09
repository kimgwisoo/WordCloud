from konlpy.tag import Okt
import nltk
import re
from nltk.tokenize import TweetTokenizer
from collections import Counter


def ko_tag(title, count):
    twitter = Okt()

    sentences_tag = []
    morph = twitter.pos(title)
    sentences_tag.append(morph)
    # for w in twitter:
    #     if w not in stop_words:
    #         sentences_tag(w)

    noun_adj_list = []
    word_tag_dict = {}
    for sentence1 in sentences_tag:
        for word, tag in sentence1:
            if tag in ['Noun', 'Adjective']:
                #print(word, tag)

                noun_adj_list.append(word)
                word_tag_dict[word] = tag

    return noun_adj_list, word_tag_dict


def en_tag(title, count):
    twitter = TweetTokenizer(strip_handles=True, reduce_len=True)

    sentences_tag = []
    wd = re.sub("[-=+,·#/\?:^$.@*\"※~&%ㆍ!’』\\‘|\(\)\[\]\<\>`\'…》]", '', title)
    morph = twitter.tokenize(wd)
    sentences_tag.append(morph)

    noun_adj_list = []
    tagged = nltk.pos_tag_sents(sentences_tag)
    word_tag_dict = {}
    for sentence1 in tagged:
        for word, tag in sentence1:
            if tag in ['NNP', 'JJ', 'NN']:
                if tag == 'NNP' or tag == 'NN':
                    tag = 'Noun'
                else:
                    tag = 'Adjective'
                noun_adj_list.append(word)
                word_tag_dict[word] = tag

    return noun_adj_list, word_tag_dict
