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
      self.assertEqual(deploytools.WrongParameterException,e.type)
  def test_connection_valid(self):
    deployer=Deployer()
    deployer.connect('t3://localhost:7001','user.config','user.key')
    self.assertEqual(deployer.isConnected(),True)
  def test_connection_invalid_url(self):
    deployer=Deployer()
    deployer.connect('t3://someserveranywhere:7002','user.config','user.key')
    self.assertEqual(deployer.isConnected(),False)
  def test_connection_invalid_configFile(self):
    deployer=Deployer()
    deployer.connect('t3://localhost:7001','user.config.invalid','user.key')
    self.assertEqual(deployer.isConnected(),False)
  def test_connection_invalid_keyFile(self):
    deployer=Deployer()
    deployer.connect('t3://localhost:7001','user.config','user.key.invalid')
    self.assertEqual(deployer.isConnected(),False)


#class deployEditMode_Test(unittest.TestCase):
#  def
   
if __name__ == "__main__" or __name == "main":
  unittest.main()   
   
