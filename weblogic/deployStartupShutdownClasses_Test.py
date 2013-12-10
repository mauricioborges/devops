
import wl
import unittest
import time
import shutil

"""
class TestApplyStartupClass(unittest.TestCase):
	def setUp(self):
		raise 'not implemented'
	def test_applyInexistentStartupClassOffline(self):
		wl.connect(raise 'not implemented'
	def test_applyInexistentStartupClassOnline(self):
		raise 'not implemented'
	def test_applyExistentStartupClassOffline(self):
		raise 'not implemented'
	def test_applyExistentStartupClassOnline(self):
		raise 'not implemented'
	def tearDown(self):
		raise 'not implemented'
"""

class TestStartupClassComparable(unittest.TestCase):
	def setUp(self):
		self.domainDir='/tmp/'+repr(time.time())
		templateFile='/home/vagrant/Oracle/Middleware/wlserver_10.3/common/templates/domains/wls.jar'
		self.username='weblogic'
		self.password='aaahL00k@AllDLon3lyPPl'
		print "Creating domain "+ self.domainDir
		wl.createDomain(templateFile,self.domainDir,self.username,self.password)
		wl.startServer(domainDir=self.domainDir,serverLog='/dev/null',username=self.username,password=self.password)
		wl.connect(self.username,self.password,'t3://localhost:7001')
		domainConfig=wl.domainConfig()
		wl.edit()
		editor=wl.startEdit()
		editor.createStartupClass('teste-1')
		editor.createStartupClass('teste-2')
	def test_compareEqual(self):
		expectedStartupClasses=["teste-1","teste-2"]
		print self.domainConfig.getStartupClasses()
		self.assertEqual(self.domainConfig.getStartupClasses(),expectedStartupClasses)

#	def test_compareDifferent(self):
#	def test_compareOneIsNull(self):
#	def test_withProductionMode(self):

	def tearDown(self):
		wl.shutdown()
		shutil.rmtree(self.domainDir)
"""
class TestStartupClassesAbstraction(unittest.TestCase):

	def setUp(self):
		self.test_domain=None
		self.newStartupClass=None
		self.alreadyExistentStartupClass=None
	def test_includeNewStartupClassArgument(self):
		listOfExpectedStartupClasses=None
		self.test_domain.add(self.newStartupClass)
		assert(test_domain.get)
		self.assertTrue(test_domain.getStartupClasses()==listOfExpectedStartupClasses)

	def test_updateStartupClassArgument(self):
		self.test_domain.add(self.alreadyExistentStartupClass)
		self.assertTrue
"""
if __name__ == "__main__" or __name == "main":
	unittest.main()
