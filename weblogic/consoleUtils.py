

class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'

  def disable(self):
    self.HEADER = ''
    self.OKBLUE = ''
    self.OKGREEN = ''
    self.WARNING = ''
    self.FAIL = ''
    self.ENDC = ''
  
def __endText(message):
  return '\n'+message + bcolors.ENDC

def paintAsHeader(message):
  return __endText(bcolors.HEADER + message)

def paintAsFail(message):
  return __endText(bcolors.FAIL + message)

def paintAsOkBlue(message):
  return __endText(bcolors.OKBLUE + message)

def paintAsOkGreen(message):
  return __endText(bcolors.OKGREEN + message)

def paintAsWarning(message):
  return __endText(bcolors.WARNING + message)

#examples
#print bcolors.FAIL+ 'naldo'+ bcolors.ENDC
#print bcolors.OKBLUE+ 'naldo'+ bcolors.ENDC
#print bcolors.OKGREEN+ 'naldo'+ bcolors.ENDC
#print bcolors.WARNING+ 'naldo'+ bcolors.ENDC
#print bcolors.HEADER+ 'naldo'+ bcolors.ENDC

