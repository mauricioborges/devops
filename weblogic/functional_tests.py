import wl
import unittest
import deploytools
from deploytools import Deployer


#Features:
#* deploy of applications
class ApplicationDeploy_FunctionalTest(unittest.TestCase):
  def test_deploy_notConnected(self):
    deployer=Deployer()
    try:
      deployer.deploy(artifact,name,targets)
    except Exception, e: 
      self.assertTrue(isinstance(e,deploytools.NotConnectedException))
  def test_deploy_existingApplication(self):
    deployer=Deployer()
    try:
      deployer.deploy(artifact,name,targets)
    except Exception,e: 
      self.assertTrue(isinstance(e,deploytools.NotConnectedException))
  def test_deploy_newApplication(self):
    self.fail('to implement')
  def test_deploy_existingApplicationWithMaximumDifferentVersions(self):
    self.fail('to implement')
  def test_deploy_notExistingArtifact(self):
    self.fail('to implement')
  def test_deploy_notExistingServer(self):
    self.fail('to implement')
  def test_deploy_notExistingAdminServer(self):
    self.fail('to implement')
  def test_deploy_serverNotOnline(self):
    self.fail('to implement')
      
#* application removal
class ApplicationRemoval_FunctionalTest(unittest.TestCase):
  def test_todo(self):
    self.fail('to implement')

#* deploy of datasources
class DatasourceDeploy_FunctionalTest(unittest.TestCase):
  def test_todo(self):
    self.fail('to implement')


#* deploy of libraries
class LibraryDeploy_FunctionalTest(unittest.TestCase):
  def test_todo(self):
    self.fail('to implement')

#* deploy of startup classes
class StartupClassDeploy_FunctionalTest(unittest.TestCase):
  def test_todo(self):
    self.fail('to implement')

#* deploy of custom MBeans
class CustomMBeanDeploy_FunctionalTest(unittest.TestCase):
  def test_todo(self):
    self.fail('to implement')

#* deploy of security configurations
class SecurityDeploy_FunctionalTest(unittest.TestCase):
  def test_todo(self):
    self.fail('to implement')

#* creation of new servers
class ServerCreation_FunctionalTest(unittest.TestCase):
  def test_todo(self):
    self.fail('to implement')

#* creation of new clusters
class ClusterCreation_FunctionalTest(unittest.TestCase):
  def test_todo(self):
    self.fail('to implement')

#* creation of new domains
class DomainCreation_FunctionalTest(unittest.TestCase):
  def test_todo(self):
    self.fail('to implement')


   
if __name__ == "__main__" or __name == "main":
  unittest.main()   
   
