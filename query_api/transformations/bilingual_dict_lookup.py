import os
from re import compile, sub
from string import punctuation
from query_api.transformations.transducers import fst_handler
from query_api.transformations.utils import transformation

punct_regex = compile("[{}]".format(punctuation))

cwd = os.path.dirname(os.path.abspath(__file__))
es2en_file = os.path.join(cwd, "transducers", "bilingual_fsts", "lookup.spa-eng.att")
en2es_file = os.path.join(cwd, "transducers", "bilingual_fsts", "lookup.eng-spa.att")

ES2EN = fst_handler.FSTHandler(es2en_file)
EN2ES = fst_handler.FSTHandler(en2es_file)


def tokenize(s):
    return s.split()


# def word_for_word_translation(s, lookup_fst):
#     translated_tokens = []
#     s = sub(punct_regex, "", s.lower())

#     for word in tokenize(s):
#         translations = lookup_fst.generate_forms(word)
#         if len(translations) > 1:
#             translated_tokens.append("({})".format('|'.join(translations)))
#         elif translations:
#             translated_tokens.append(translations[0])
    
#     return " ".join(translated_tokens)

@transformation(data_field='en_es_bilingual_dict')
def en_es_bilingual_dict(query_string):
    translations = EN2ES.generate_forms(query_string)
    translations.append(query_string)
    return "({})".format("|".join(translations))

@transformation(data_field='es_en_bilingual_dict')
def es_en_bilingual_dict(query_string):
    translations = ES2EN.generate_forms(query_string)
    translations.append(query_string)
    return "({})".format("|".join(translations))
