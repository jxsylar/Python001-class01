#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd


class Simulate:
    """Simulate SQL statements with pandas"""

    def __init__(self):
        self.file1 = "./mock_data1.csv"
        self.file2 = "./mock_data2.csv"
        self.count = 0
        self.width = 70
        self._init_data()

    def _init_data(self):
        self._table1 = pd.read_csv(self.file1)
        self._table2 = pd.read_csv(self.file2)

    @property
    def table1(self):
        return self._table1.copy()

    @property
    def table2(self):
        return self._table2.copy()

    def _print(self, sql, pandas_res):
        self.count += 1
        print(f"{self.count:-^{self.width}}")
        print(f"|{sql: ^{self.width - 2}}|")
        print(f"{'-':-^{self.width}}")
        print(pandas_res)

    def case1(self):
        sql = "SELECT * FROM data;"
        res = self.table1
        self._print(sql, res)

    def case2(self):
        sql = "SELECT * FROM data LIMIT 10;"
        self._print(sql, self.table1.head(10))

    def case3(self):
        sql = "SELECT id FROM data;"
        self._print(sql, self.table1['id'])

    def case4(self):
        sql = "SELECT COUNT(id) FROM data;"
        res = self.table1['id'].count()
        self._print(sql, res)

    def case5(self):
        sql = "SELECT * FROM data WHERE id<1000 AND age>30;"
        condition = (self.table1['id'] < 1000) & (self.table1['age'] > 30)
        res = self.table1[condition]
        self._print(sql, res)

    def case6(self):
        sql = "SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;"
        sales = [
            {'account': 'Jones LLC', 'id': 'A', 'order_id': 3},
            {'account': 'Alpha Co', 'id': 'B', 'order_id': 2},
            {'account': 'Blue Inc', 'id': 'A', 'order_id': 1},
            {'account': 'Tax', 'id': 'B', 'order_id': 2},
            {'account': 'Axt', 'id': 'B', 'order_id': 1},
        ]
        table = pd.DataFrame(sales)
        res = table.groupby('id').aggregate({'id': 'count', 'order_id': 'nunique'})
        self._print(sql, res)

    def case7(self):
        sql = "SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;"
        res = self.table1.merge(self.table2, on='id', how='inner').reset_index()
        self._print(sql, res)

    def case8(self):
        sql = "SELECT * FROM table1 UNION SELECT * FROM table2;"
        res = pd.concat([self.table1, self.table2]).reset_index()
        self._print(sql, res)

    def case9(self):
        sql = "DELETE FROM table1 WHERE id=10;"
        # res = self.table1[self.table1['id']!=10]
        labels = self.table1[self.table1['id'] == 10].index
        res = self.table1.drop(labels, axis=0)
        self._print(sql, res.iloc[8:12])

    def case10(self):
        sql = "ALTER TABLE table1 DROP COLUMN column_name;"
        self.table1.drop("age", axis=1, inplace=True)
        self._print(sql, self.table1.head())

    def run(self):
        for i in self.__dir__():
            if i.startswith("case"):
                getattr(self, i).__call__()


def main():
    p = Simulate()
    p.run()


if __name__ == '__main__':
    main()
