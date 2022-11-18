import re

from clear_ans_data import clear_ans_data
from testing_func import testing_func


def task1(text: str):
    res = re.findall(r'\[<{\\', text)
    return len(res)


results_for_testing = list()
with open(f'tests/task1/1', 'r') as f:
    for index, line in enumerate(f.readlines(), start=1):
        result = task1(line)
        results_for_testing.append(str(result))
        print(f'{index})', result)

with open(f'tests/task1/ans', 'r', encoding='utf8') as f:
    print()
    print('Tests:')
    testing_func(results_for_testing, clear_ans_data(f.readlines()))
