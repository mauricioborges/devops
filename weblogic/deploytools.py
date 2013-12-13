import wl
import consoleUtils

#TODO: load files from SVN
#TODO: load configuration from file
#TODO: load encrypted keys from files


class Deployer:

  def connect(self, serverURL,userConfigFile,userKeyFile):
    print consoleUtils.paintAsHeader('Connecting to '+serverURL+' with user Config File ' + userConfigFile)
  def deploy(artifact,targets,domain):
    raise paintAsFail('not implemented yet!')

class ConnectionStatuses:
  CONNECTED='CONNECTED'
  DISCONNECTED='DISCONNECTED'




#if __name__ == "__main__" or __name == "main":
#  deploy(artifact,targets,adminServer)
  
