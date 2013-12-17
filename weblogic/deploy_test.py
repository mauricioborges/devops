import wl
import unittest
import deploytools
import consoleUtils
from deploytools import Deployer

artifact=['example.war']
targets=['server1']


def getStatusApplication():
  raise(consoleUtils.paintAsFail('not implemented yet'))


class deployConnections_Test(unittest.TestCase):

  def test_deployConnNone(self):
    #Context Management to assertRaises is available only in Python 2.7+
    #self.assertRaises(deploytools.WrongParameterException,Deployer().connect,(None,None,None))
    try:
      Deployer().connect,(None,None,None)
    except e:
      self.assertEqual(deploytools.WrongParameterExceptionException.__name__,e.__class__.__name__)
  def test_connection_valid(self):
    deployer=Deployer()
    deployer.connect('t3://localhost:7001','user.config','user.key')
    self.assertEqual(deployer.isConnected(),True)
  def test_connection_invalid_url(self):
    try:
      deployer=Deployer()
      deployer.connect('t3://someserveranywhere:7002','user.config','user.key')
    except Exception, e:
      self.assertEqual(deployer.isConnected(),False)
      self.assertEqual(deploytools.FailedConnectionException.__name__,e.__class__.__name__)
  def test_connection_invalid_configFile(self):
    try:
      deployer=Deployer()
      deployer.connect('t3://localhost:7001','user.config.invalid','user.key')
    except Exception, exception:
      self.assertEqual(deploytools.WrongParameterException.__name__,exception.__class__.__name__)

  def test_connection_invalid_keyFile(self):
    try:
      deployer=Deployer()
      deployer.connect('t3://localhost:7001','user.config','user.key.invalid')
    except Exception, exception:
      self.assertEqual(deploytools.FailedConnectionException.__name__,exception.__class__.__name__)

class UserConfigAndKeyFile_Test(unittest.TestCase):
  def test_userConfigOkAndUserKeyOk(self):
    deployer=Deployer()
    deployer._userConfigFile='user.config'
    deployer._userKeyFile='user.key'
    self.assertEqual(deployer._areUserFilesValid(),True)
  def test_userConfigEmptyAndUserKeyOk(self):
    deployer=Deployer()
    deployer._userConfigFile='user.config.empty'
    deployer._userKeyFile='user.key'
    self.assertEqual(deployer._areUserFilesValid(),False)
  def test_userConfigWrongAndUserKeyOk(self):
    deployer=Deployer()
    deployer._userConfigFile='user.config.invalid'
    deployer._userKeyFile='user.key'
    self.assertEqual(deployer._areUserFilesValid(),False)
  def test_userConfigOkAndUserKeyEmpty(self):
    deployer=Deployer()
    deployer._userConfigFile='user.config'
    deployer._userKeyFile='user.key.empty'
    self.assertEqual(deployer._areUserFilesValid(),False)
  def test_userConfigWrongAndUserKeyWrong(self):
    deployer=Deployer()
    deployer._userConfigFile='user.config.invalid'
    deployer._userKeyFile='user.key.invalid'
    self.assertEqual(deployer._areUserFilesValid(),False)


#class deployEditMode_Test(unittest.TestCase):
#  def
   
if __name__ == "__main__" or __name == "main":
  unittest.main()   
   
