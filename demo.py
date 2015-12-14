#!/usr/bin/env python3
# coding: utf-8
import psycopg2


def db(dsn):
    conn = psycopg2.connect(**dsn)
    conn.autocommit = True
    return conn


class PostgresDemo():
    """ A simple demonstration module to show how to test database methods
    with testing.postgresql
    """

    def __init__(self, dsn={}):
        """ Make connection to arbitrary database
        specified via dsn mapping
        """
        self.dsn = dsn
        self.conn = db(self.dsn)
        self.cur = self.conn.cursor()

    def create_foo(self):
        """ Create table named 'foo' with one text column """
        self.cur.execute("create table foo(bar text)")

    def insert_fixture(self):
        """ Insert the literal 'fixture' into our table """
        self.cur.execute("insert into foo (bar) values ('fixture')"
                         " returning bar")
        result = self.cur.fetchone()[0]
        return result

    def select_fixture(self):
        """ Select one row from the table """
        self.cur.execute("select bar from foo where bar = 'fixture'")
        result = self.cur.fetchone()[0]
        try:
            self.conn.close()
        except psycopg2.core.InterfaceError:
            pass  # error would just mean db is closed already. Don't care.
        return result


if __name__ == '__main__':
    host = 'postgres'
    user = 'demo'
    password = 'qqqWww111'
    database = 'yardstick'
    port = 5432
    dsn = zip(['host', 'user', 'password', 'database', 'port'],
              [host, user, password, database, port])
    dsn = dict(dsn)
    demo = PostgresDemo(dsn)
    demo.create_foo()
    demo.insert_fixture()
    fixture = demo.select_fixture()
    print(fixture)
