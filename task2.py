import re

from clear_ans_data import clear_ans_data
from testing_func import testing_func

VOWELS = r'АЕЁИОУЫЭЮЯаеёиоуыэюя'
RUSSIAN_ALPHABET = r'А-Яа-яЁё0-9'
CONSONANTS = fr'БВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬбвгджзйклмнпрстфхцчшщъь'
B_START = fr'( |^)'
B_END = fr'( |$)'


def task2(text: str):
    first_word = fr'[{RUSSIAN_ALPHABET}]*[{VOWELS}]' + '{2}' + fr'[{RUSSIAN_ALPHABET}]*'
    vowel_cons = fr'[{VOWELS}]*[{CONSONANTS}]?'
    second_word = fr'{vowel_cons * 3}[{VOWELS}]*'
    res = re.findall(f'({first_word})(?={B_START}{second_word}{B_END})', text)
    return [i[0] for i in res]


results_for_testing = list()
with open('tests/task2/2', 'r', encoding='utf8') as f:
    for index, line in enumerate(f.readlines(), start=1):
        result = task2(line)
        results_for_testing.append(' '.join(result) if result else 'Fail!')
        print(f'{index})', *result if result else ['Fail!'], sep=' ')

with open(f'tests/task2/ans', 'r', encoding='utf8') as f:
    print()
    print('Tests:')
    testing_func(results_for_testing, clear_ans_data(f.readlines()))
