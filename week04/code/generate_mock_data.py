#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import random
import string

file_fmt = "mock_data{}.csv"
file_num = 2
data_num = 2000


def generate_names():
    names = set()
    while True:
        name = ''.join(random.sample(string.ascii_uppercase, 5))
        names.add(name)
        if len(names) > data_num * file_num:
            break
    return names


def main():
    names = generate_names()
    for count in range(1, file_num + 1):
        file = file_fmt.format(count)
        with open(file, 'w', encoding='utf-8') as f:
            csvwriter = csv.writer(f, lineterminator='\n')
            csvwriter.writerow(['id', 'order_id', 'name', 'age'])
            for i in range(data_num):
                csvwriter.writerow([
                    i,
                    random.randint(1, 100),
                    names.pop(),
                    random.randint(1, 81)
                ])
        print(f"generate file success: {file}")


if __name__ == '__main__':
    main()
