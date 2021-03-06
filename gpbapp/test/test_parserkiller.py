#!/usr/bin/python

# Pytest file
from gpbapp.utils.parserkiller import get_stopwords_list
from gpbapp.utils.parserkiller import split_user_question
from gpbapp.utils.parserkiller import get_address

# Parserkiller test

def test_get_stopwords_file():
    """ Get the stop word list """
    assert type(get_stopwords_list()) == list

def test_split_the_user_question():
    """ Split the question in list """
    assert split_user_question("J'ai été au 7 rue des champs à Paris avant hier") == [
        "j", "ai", "été", "au", "7", "rue", "des", "champs", "à", "paris", "avant", "hier"]

def test_compare_the_user_sentence_to_dict_list():
    """ Compare the user_sentence to the stop words list """
    assert get_address("J'ai été au 7 rue des champs à Paris avant hier") == "7 rue des champs paris"
    assert get_address("Ou est la Tour Eiffel ?") == "tour eiffel"
    assert get_address("Sais tu où est le Ministère de la défense ?") == "ministère défense"

    
