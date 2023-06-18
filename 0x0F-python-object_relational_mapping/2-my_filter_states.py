 #!/usr/bin/python3
  2 # -*- coding: utf-8 -*-
  3 """
  4 Created on sat  Jun 17 03:56
  5
  6 @author: Nebiha Dilsebo
  7 """
  8 import MySQLdb
  9 import sys
 10
 11
 12 if __name__ =='__main__':
 13     args = sys.argv
 14     if len(args) != 5:
 15         print("Usage: {} username password database_nam    e".format(args[0]))
 16         exit(1)
 17     username = args[1]
 18     password = args[2]
 19     data = args[3]
        state_name = args[4]
        db = MySQLdb.connect(host='localhost', user=usernam    e,
 21                          passwd=password, db=data, port    =3306)
 22     cur = db.cursor()
 23     num_rows = cur.execute("SELECT * FROM states ORDER     BY states.id;".format(state_name)))
 24     rows = cur.fetchall()
 25     for row in rows:
            print(row)
        cur.close()
        db.close()
