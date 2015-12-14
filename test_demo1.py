#!/usr/bin/env python
# coding: utf-8

import unittest
import testing.postgresql
import psycopg2
from demo1 import PostgresDemo


# create initial data on create the database which is cached through testcases
def handler(postgresql):
    conn = psycopg2.connect(**postgresql.dsn())
    cursor = conn.cursor()
    cursor.execute("create table foo(bar text)")
    cursor.execute("INSERT INTO foo VALUES ('hello'), ('fixture'), ('baz')")
    cursor.close()
    conn.commit()
    conn.close()

# Use `handler()` on initialize database
Postgresql = testing.postgresql.PostgresqlFactory(use_initdb_cache=True,
                                                  initdb_handler=handler)


# def tearDownModule(self):
#     # clear cached database at end of tests
#     Postgresql.clear_cache()


class TestDemo(unittest.TestCase):

    def setUp(self):
        self.db = Postgresql()  # (base_dir='data')
        self.conn = psycopg2.connect(**self.db.dsn())
        self.cur = self.conn.cursor()
        self.pgdb = PostgresDemo(self.db.dsn())

    def tearDown(self):
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

    def test_update(self):
        result = self.pgdb.update_fixture()
        self.assertEqual(result, 'fixed')

if __name__ == '__main__':
    unittest.main()
