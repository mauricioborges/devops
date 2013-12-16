import wl
import consoleUtils
import java.util as util
import java.io as javaio


#TODO: load files from SVN
#TODO: load configuration from file
#TODO: load encrypted keys from files

class WrongParameterException(Exception):
  pass

class Deployer:

  _serverURL=''
  _userConfigFile=''
  _userKeyFile=''
  _wl=None
  def connect(self, serverURL,userConfigFile,userKeyFile):
    self._serverURL=serverURL
    self._userConfigFile=userConfigFile
    self._userKeyFile=userKeyFile
    if not (self._canConnect()):
      print consoleUtils.paintAsFail('Wrong connection parameters!')
      raise WrongParameterException
    print consoleUtils.paintAsHeader('Trying to connect to '+serverURL+' with user config file ' + userConfigFile)

    if self._areUserFilesValid():
      print consoleUtils.paintAsFail('Wrong connection parameters!')
      raise WrongParameterException


    wl.loadProperties(self._userConfigFile)
    wl.connect(userConfigFile=self._userConfigFile, userKeyFile=self._userKeyFile, url=self._serverURL, timeout=60000)
    self._wl=wl

  def deploy(artifact,targets,domain):
    raise paintAsFail('not implemented yet!')
  
  def isConnected(self):
    if self._wl.cmo:
      return True
    return False

  def _canConnect(self):
    #print consoleUtils.paintAsOkBlue(self._serverURL)
    #print consoleUtils.paintAsOkBlue(self._userConfigFile)
    #print consoleUtils.paintAsOkBlue(self._userKeyFile)
    if self._serverURL and self._userConfigFile and self._userKeyFile:
      return True
    return False

  def _areUserFilesValid():
    if self._userConfigFile and self._userKeyFile:



#if __name__ == "__main__" or __name == "main":
#  deploy(artifact,targets,adminServer)
  
