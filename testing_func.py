def testing_func(test_data, ans_data):
    for index, (test, ans) in enumerate(zip(test_data, ans_data), start=1):
        if test == ans:
            print(f'{index}) Complete!')
        else:
            print(f'{index}) Fail!')
