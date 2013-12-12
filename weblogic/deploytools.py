import wl
import consoleUtils

#TODO: load files from SVN
#TODO: load configuration from file
#TODO: load encrypted keys from files


class Deployer:
  def __init__(self,connection):
    self.connection=connection

  def deploy(artifact,targets,domain):
    raise paintFail('not implemented yet!')

class ConnectionStatuses:
  CONNECTED='CONNECTED'
  DISCONNECTED='DISCONNECTED'




#if __name__ == "__main__" or __name == "main":
#  deploy(artifact,targets,adminServer)
  
