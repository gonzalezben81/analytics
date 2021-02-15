import random
import string


def randomString2(stringLength):
    stringLength = stringLength
    """Generate a random string of fixed length """
    letters= string.ascii_lowercase
    return ''.join(random.sample(letters,stringLength))
    
    
def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return
