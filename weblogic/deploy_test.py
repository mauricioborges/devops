import wl
import unittest
import deploytools
import consoleUtils
from deploytools import Deployer

artifact=['example.war']
targets=['server1']


def getStatusApplication():
  raise(consoleUtils.paintFail('not implemented yet'))


class deployConnections_Test(unittest.TestCase):

  def test_deployConnNone(self):
    unittest.assertEqual(Deployer().connect(None).connectionStatus(),'DISCONNECTED')
  def test_connection_valid(self):
    unittest.assertEqual(Deployer().connect('t3://localhost:7001','user.config','user.key').connectionStatus(),deployTools.ConnectionStatuses.CONNECTED)
  def test_connection_invalid_url(self):
    unittest.assertEqual(Deployer().connect('t3://someserveranywhere:7002','user.config','user.key').connectionStatus(),deployTools.ConnectionStatuses.DISCONNECTED)
  def test_connection_invalid_configFile(self):
    unittest.assertEqual(Deployer().connect('t3://localhost:7001','user.config.invalid','user.key').connectionStatus(),deployTools.ConnectionStatuses.DISCONNECTED)
  def test_connection_invalid_keyFile(self):
    unittest.assertEqual(Deployer().connect('t3://localhost:7001','user.config','user.key.invalid').connectionStatus(),deployTools.ConnectionStatuses.DISCONNECTED)


#class deployEditMode_Test(unittest.TestCase):
#  def
   
if __name__ == "__main__" or __name == "main":
  unittest.main()   
   
