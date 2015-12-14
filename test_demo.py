#!/usr/bin/env python
# coding: utf-8

import unittest
import testing.postgresql
import psycopg2
from demo import PostgresDemo
# from time import sleep


class TestDemo(unittest.TestCase):

    def setUp(self):
        self.db = testing.postgresql.Postgresql()  # (base_dir='data')
        self.conn = psycopg2.connect(**self.db.dsn())
        self.cur = self.conn.cursor()
        self.pgdb = PostgresDemo(self.db.dsn())
        self.pgdb.create_foo()

    def tearDown(self):
        # sleep(180)
        self.db.stop()

    def test_pg_up(self):
        self.cur.execute(u"select version()")
        result = self.cur.fetchone()
        self.assertTrue(result)

    def test_create_foo(self):
        self.cur.execute(u"select exists(select * from information_schema."
                         "tables where table_name={})".format("'foo'"))
        result = self.cur.fetchone()[0]
        self.assertTrue(result)

    def test_insert(self):
        result = self.pgdb.insert_fixture()
        self.assertEqual(result, 'fixture')

    def test_select(self):
        self.pgdb.insert_fixture()
        result = self.pgdb.select_fixture()
        self.assertEqual(result, 'fixture')

if __name__ == '__main__':
    unittest.main()
