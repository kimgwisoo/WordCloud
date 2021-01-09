# -*- coding: utf-8 -*-
import re
from collections import Counter
import tag_module


def EndProcessing(count, noun_adj_list, word_tag_dict):

    counts = Counter(noun_adj_list)

    tags = counts.most_common(count)
    tags_list = []
    tags_count = 0
    print(word_tag_dict)
    for result in tags:
        if tags_count > 4:
            break
        if len(result[0]) < 2:
            pass
        else:
            tags_list.append([result[0], result[1], word_tag_dict[result[0]]])
            print(result[0], result[1], word_tag_dict[result[0]])
            tags_count = tags_count + 1

    return tags_list


def Classification(text):
    text1 = re.compile('[\u3131-\u3163\uac00-\ud7a3]+').findall(text)
    text2 = re.compile('[a-zA-Z]+').findall(text)

    if text1 and text2:
        return 'two'
    elif text1:
        return 'ko'
    elif text2:
        return 'en'
    else:
        return None


if __name__ == '__main__':

    text = "I'm In MAC OSX it still can show an exception if you try this code. So make sure you download the words corpus manually. Once you import your nltk library, make you might as in mac os it does not download the words corpus automatically. So you have to download it potentially otherwise you will face exception."

    # I'm, you're, givin'em 등 제거
    exception = re.compile("\'[a-zA-Z]+")
    text = re.sub(exception, '', text)

    count = 1000000
    result = Classification(text)
    if result is not None:
        if result == 'two':

            noun_adj_list_ko, word_tag_dict_ko = tag_module.ko_tag(text, count)

            korean = re.compile('[\u3131-\u3163\uac00-\ud7a3]+')
            text = re.sub(korean, '', text)
            noun_adj_list_en, word_tag_dict_en = tag_module.en_tag(text, count)

            noun_adj_list = noun_adj_list_ko + noun_adj_list_en
            word_tag_dict = {**word_tag_dict_ko, **word_tag_dict_en}

            taglist = EndProcessing(count, noun_adj_list, word_tag_dict)
            print(taglist)

        elif result == 'ko':
            noun_adj_list, word_tag_dict = tag_module.ko_tag(text, count)
            taglist = EndProcessing(count, noun_adj_list, word_tag_dict)
            print(taglist)

        elif result == 'en':
            noun_adj_list, word_tag_dict = tag_module.en_tag(text, count)
            taglist = EndProcessing(count, noun_adj_list, word_tag_dict)
            print(taglist)

        else:
            print('Text IS None')
