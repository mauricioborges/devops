import wl
import consoleUtils
from java.io import File
from java.io import FileInputStream
from java.util import Properties
from java.lang import NullPointerException
import os
from wl import WLSTException


#TODO: load files from SVN
#TODO: load configuration from file
#TODO: load encrypted keys from files

class WrongParameterException(Exception):
  pass
 
class FailedConnectionException(Exception):
  pass

class NotConnectedException(Exception):
  pass

class Deployer:

  _serverURL=''
  _userConfigFile=''
  _userKeyFile=''
  _wl=None
  def connect(self, serverURL,userConfigFile,userKeyFile):
    self._wl=wl
    self._serverURL=serverURL
    self._userConfigFile=userConfigFile
    self._userKeyFile=userKeyFile
    if not (self._canConnect()):
      print consoleUtils.paintAsFail('Wrong connection parameters!')
      raise WrongParameterException
    print consoleUtils.paintAsHeader('Trying to connect to '+serverURL+' with user config file ' + userConfigFile)

    if not self._areUserFilesValid():
      print consoleUtils.paintAsFail('Check your user config files, there is something wrong with them...')
      raise WrongParameterException

    try:
      wl.connect(userConfigFile=self._userConfigFile, userKeyFile=self._userKeyFile, url=self._serverURL, timeout=60000)
    except WLSTException, e:
      wl.dumpStack()
      raise FailedConnectionException

  def deploy(self,artifact,targets,domain):
    if not self.isConnected():
      raise NotConnectedException
    if not (artifact and targets and domain):
      raise WrongParameterException
  
  #todo: test this method
  def isConnected(self):
    if not self._wl:
      return False
    else:  
#increase test accuracy...anyone can put anything here to guarantee it's working
      if self._wl.cmo:
        return True
    return False

  def isActive(self,applicationName):
    return True
  def getVersion(self,applicationName):
    return '1.0-SNAPSHOT'


  def _canConnect(self):
    if self._serverURL and self._userConfigFile and self._userKeyFile:
      return True
    return False

  def _is_non_zero_file(self,fpath):  
      if os.path.isfile(fpath) and os.path.getsize(fpath) > 0:
        return True
      else: 
        return False

#TODO: use different exceptions?
  def _areUserFilesValid(self):
    if not (self._userConfigFile and self._userKeyFile):
      return False
    if not (self._is_non_zero_file(self._userConfigFile) and self._is_non_zero_file(self._userKeyFile)):
      return False
    try:
      inStream=FileInputStream(self._userConfigFile)
      userConfigs=Properties()
      userConfigs.load(inStream)
    except NullPointerException:
      return False
    if not (userConfigs.getProperty('weblogic.management.username') and userConfigs.getProperty('weblogic.management.password')):
      return False
    return True


#if __name__ == "__main__" or __name == "main":
#  deploy(artifact,targets,adminServer)
  
