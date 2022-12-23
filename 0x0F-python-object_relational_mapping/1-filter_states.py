#!/usr/bin/python3
"""This script lists all states from the database hbtn_0e_0_usa"""
import MySQLdb


def sql_error(error, db=None, cur=None):
    """Handler for MySQL errors"""
    if (not isinstance(error, Exception)):
        return None
    if cur:
        cur.close()
    if db:
        db.close()
    try:
        print("MySQL Error [{:d}]: {:s}".format(error.args[0], error.args[1]))
    except IndexError:
        print("MySQL Error: {:s}".format(str(error)))


def main():
    """Main function"""
    from sys import argv

    db = None
    cur = None
    kwargs = {"host": "localhost", "port": 3306, "db": "hbtn_0e_0_usa"}
    try:
        # if (len(argv) > 3):
        kwargs["user"] = argv[1]
        kwargs["passwd"] = argv[2]
        kwargs["db"] = argv[3]

        db = MySQLdb.connect(**kwargs)
        cur = db.cursor()

    except MySQLdb.Error as e:
        # sql_error(e, db, cur)
        raise e

    if (not db or not cur):
        return

    try:
        query = '''
        SELECT *
        FROM `states`
        WHERE `name` LIKE 'N%'
        ORDER BY `id` ASC
        '''
        cur.execute(query)
        table = cur.fetchall()

        for row in table:
            print(row)
    except MySQLdb.Error as e:
        # sql_error(e, db, cur)
        raise e
    # finally:
    #     cur.close()
    #     db.close()


if __name__ == "__main__":
    main()
