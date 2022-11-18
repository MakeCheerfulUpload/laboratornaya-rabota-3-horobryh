import re

from clear_ans_data import clear_ans_data
from testing_func import testing_func


def task3(text: str):
    pattern = fr'(^[\w\._]*@([A-z]+\.)+[A-z]+$)'
    res = re.findall(pattern, text)
    return res[0][0].split('@')[-1] if res else 'Fail!'


results_for_testing = list()
with open('tests/task3/3', 'r') as f:
    for index, i in enumerate(f.readlines(), start=1):
        result = task3(i)
        results_for_testing.append(result)
        print(f'{index}) {result}')


with open(f'tests/task3/ans', 'r', encoding='utf8') as f:
    print()
    print('Tests:')
    testing_func(results_for_testing, clear_ans_data(f.readlines()))
