import wl
import unittest
import deploytools
from deploytools import Deployer
import traceback


#Features:
#* deploy of applications
class ApplicationDeploy_FunctionalTest(unittest.TestCase):
  def test_deploy_emptyParameters(self):
    deployer=Deployer()
    version='1.0'
    artifact=None
    name=None
    targets=None
    try:
      deployer.connect('t3://localhost:7001','user.config','user.key')
      deployer.deploy(artifact,name,targets)
    except Exception, e:
      self.assertEqual(isinstance(e,deploytools.WrongParameterException), True)
  def test_deploy_notConnected(self):
    deployer=Deployer()
    version='1.0'
    artifact='artifact.war'
    name='project'
    targets='server1'
    try:
      deployer.deploy(artifact,name,targets)
    except Exception, e:
      self.assertEqual(isinstance(e,deploytools.NotConnectedException), True)
  def test_deploy_existingApplication(self):
    deployer=Deployer()
    version='1.0-SNAPSHOT'
    artifact='/vagrant/dumb-webapp-1.0-SNAPSHOT.war'
    applicationName='dumb-webapp'
    targets=['AdminServer']
    deployer.connect('t3://localhost:7001','user.config','user.key')
    deployer.deploy(artifact,applicationName,targets)
    self.assertEqual(deployer.isActive(applicationName),True)
    self.assertEqual(deployer.getVersion(applicationName),version)
    self.assertEqual(deployer.isConnected(),True)
    traceback.print_exc()
  def test_deploy_existingApplicationWhichBeforeHasNoVersion(self):
    self.fail('to implement')
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

#TODO: deploy when editing session is opened...deploy when editing session is closed...
      
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
   
