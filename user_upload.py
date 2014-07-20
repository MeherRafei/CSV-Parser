#!/usr/bin/env python2.7

import sys, getopt, MySQLdb

def stripped(x):
   return "".join([i for i in x if 31 < ord(i) < 127])


def main (argv):
   csv_file = ''
   users = []
   sections = ''
   mysql_user = ''
   mysql_pass = ''
   mysql_host = ''
   try:
      opts, args = getopt.getopt(argv,"u:p:h:",["help","file=","create_table","dry_run"])
   except getopt.GetoptError:
      print 'user_upload.py --file <CSV file name>'
      print 'user_upload.py --create_table'
      print 'user_upload.py --dry_run'
      print 'user_upload.py -u'
      print 'user_upload.py -p'
      print 'user_upload.py -h'
      print 'user_upload.py --help'
      sys.exit(2)

   for opt, arg in opts:
      if opt == "--help":
         print 'user_upload.py --file <CSV file name>'
         print 'user_upload.py --create_table'
         print 'user_upload.py --dry_run'
         print 'user_upload.py -u'
         print 'user_upload.py -p'
         print 'user_upload.py -h'
	 print 'user_upload.py --help'
         sys.exit()
      elif opt == "--file":
         csv_file = arg
         with open(csv_file) as fp:
            for line in fp:
               users.append(line.rstrip().strip(" ").split(','))
            fp.close()
            print users
            sections = users[0]
            print sections
      elif opt == "--create_table":
         csv_file = arg
      elif opt == "--dry_run":
         csv_file = arg
      elif opt == "-u":
         mysql_user = arg
      elif opt == "-p":
         mysql_pass = arg
      elif opt == "-h":
         mysql_host = arg


if __name__ == "__main__":
   main(sys.argv[1:])
