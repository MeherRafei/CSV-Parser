#!/usr/bin/env python2.7

import sys, getopt, MySQLdb, re

def stripped(text):
   return "".join([i if ord(i) < 128 else ' ' for i in text])

def main (argv):
   csv_file = ''
   users = []
   sections = ''
   mysql_user = ''
   mysql_pass = ''
   mysql_host = ''
   try:
      opts, args = getopt.getopt(argv,"u:p:h:",["help","file=","create_table"
      ,"dry_run"])
   except getopt.GetoptError:
      print './user_upload.py --file <CSV file name>'
      print './user_upload.py --create_table'
      print './user_upload.py --dry_run'
      print './user_upload.py -u'
      print './user_upload.py -p'
      print './user_upload.py -h'
      print './user_upload.py --help'
      sys.exit(2)

   for opt, arg in opts:
      if opt == "--help":
         print './user_upload.py --file <CSV file name>'
         print './user_upload.py --create_table'
         print './user_upload.py --dry_run'
         print './user_upload.py -u'
         print './user_upload.py -p'
         print './user_upload.py -h'
	 print './user_upload.py --help'
         sys.exit()
      elif opt == "--file":
         csv_file = arg
         if (not mysql_user or not mysql_pass or not mysql_host):
            print "You must enter your mysql information to continue.\n"
            print "Please use the correct tags and try again.\n"
            sys.exit(2)

            for line in fp:
	       users.append(line.lower().rstrip().replace(" ","").split(','))
	    fp.close()
            print users

            for line2 in users:
	       print stripped(re.sub(r'\W+','', line2[0].title()))
	    sections = users[0]
	    print sections

            db = MySQLdb.connect(mysql_host, mysql_user, mysql_pass, "ftest2")
            cursor = db.cursor()

            sql = """INSERT INTO USERS(FIRST_NAME, SURNAME, EMAIL)
                  VALUES (%s,%s,%s)"""

            try:
               cursor.execute(sql (users[1][0], users[1][1], users[1][2]))
               db.commit()
            except:
               db.rollback()
 
            db.close() 
      elif opt == "--create_table":
         if (not mysql_user or not mysql_pass or not mysql_host):
            print "You must enter your mysql information to continue.\n"
            print "Please use the correct tags and try again.\n"
            sys.exit(2)
            
         db = MySQLdb.connect(mysql_host, mysql_user, mysql_pass, "ftest2")
         cursor = db.cursor()
         cursor.execute("DROP TABLE IF EXISTS USERS")
         sql = """CREATE TABLE USERS ( FIRST_NAME CHAR(20),
               SURNAME CHAR(20),
               EMAIL VARCHAR(254) )"""
         cursor.execute(sql) 
         db.close()
      elif opt == "--dry_run":
         with open(csv_file) as fp:
	    for line in fp:
	       users.append(line.lower().rstrip().replace(" ","").split(','))
	    fp.close()
            print users
            for line2 in users:
	       print stripped(re.sub(r'\w+','', line2[0].title()))
	    sections = users[0]
	    print sections
      elif opt == "-u":
         mysql_user = arg
      elif opt == "-p":
         mysql_pass = arg
      elif opt == "-h":
         mysql_host = arg


if __name__ == "__main__":
   main(sys.argv[1:])
