'''
author : Jaydatt
The getopt module is a parser for command-line options based on the convention established by the Unix getopt() function. It is in general used for parsing an argument sequence such as sys.argv. In other words, this module helps scripts to parse command-line arguments in sys.argv. It works similar to the C getopt() function for parsing command-line parameters.
'''

import getopt , sys

print('sys.argv : ',sys.argv)

def getData(argv):
    try: 
        opts, args = getopt.getopt(argv[1:], "f:l:") 
        print('opts : ', opts )
        print('args : ', args )

        for opt, arg in opts: 
            if opt in ['-f']: 
                print('-f : ',arg) 
            elif opt in ['-l']: 
                print('-l : ',arg) 
      
    except: 
        print("Error")

getData(sys.argv)


# Command Line PS :   D:\Python> py Arguments_getopt.py -f key -l val

# Output : 
# sys.argv :  ['Arguments_getopt.py', '-f', 'key', '-l', 'val']
# opts :  [('-f', 'key'), ('-l', 'val')]
# args :  []
# -f :  key
# -l :  val

