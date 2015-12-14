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

    def update_fixture(self):
        """ Select one row from the table """
        self.cur.execute("update foo set bar = 'fixed' "
                         "where bar = 'fixture' "
                         "returning bar")
        result = self.cur.fetchone()[0]
        try:
            self.conn.close()
        except psycopg2.core.InterfaceError:
            pass
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
    fixture = demo.update_fixture()
    print(fixture)
