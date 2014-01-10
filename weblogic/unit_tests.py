import wl
import unittest
import deploytools
import consoleUtils
from deploytools import Deployer
import os

artifact=['example.war']
targets=['server1']


def getStatusApplication():
  raise(consoleUtils.paintAsFail('not implemented yet'))




class deployConnections_Test(unittest.TestCase):

  def test_deployConnNone(self):
    #Context Management to assertRaises is available only in Python 2.7+
    #self.assertRaises(deploytools.WrongParameterException,Deployer().connect,(None,None,None))
    try:
      Deployer().connect(None,None,None)
    except Exception, e:
      #only in 2.7 
      #self.assertIsInstance(e,deploytools.WrongParameterException)
      self.assertEqual(isinstance(e,deploytools.WrongParameterException), True)
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
      self.assertEqual(isinstance(e,deploytools.FailedConnectionException), True)
  def test_connection_invalid_configFile(self):
    try:
      deployer=Deployer()
      deployer.connect('t3://localhost:7001','user.config.invalid','user.key')
    except Exception, e:
      self.assertEqual(isinstance(e,deploytools.WrongParameterException), True)

  def test_connection_invalid_keyFile(self):
    try:
      deployer=Deployer()
      deployer.connect('t3://localhost:7001','user.config','user.key.invalid')
    except Exception, e:
      self.assertEqual(isinstance(e,deploytools.FailedConnectionException), True)

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
  def test_userConfigMissingAndUserKeyOk(self):
    inexistentFile='user.config.idontexist'
    if not os.path.isfile(inexistentFile):
      deployer=Deployer()
      deployer._userConfigFile=inexistentFile
      deployer._userKeyFile='user.key'
      self.assertEqual(deployer._areUserFilesValid(),False)
    else:
      raise "the file "+inexistentFile + " should not exist!"
  def test_userConfigWrongAndUserKeyWrong(self):
    deployer=Deployer()
    deployer._userConfigFile='user.config.invalid'
    deployer._userKeyFile='user.key.invalid'
    self.assertEqual(deployer._areUserFilesValid(),False)


#class deployEditMode_Test(unittest.TestCase):
#  def
   
if __name__ == "__main__" or __name == "main":
  unittest.main()   
   
