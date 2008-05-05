from Products.PloneSoftwareCenter.tests.base import PSCTestCase
from Products.PloneSoftwareCenter.storage.interfaces import IPSCFileStorage

from Products.PloneSoftwareCenter.storage import getFileStorageNames
from Products.PloneSoftwareCenter.storage import DynamicStorage

class TestStorage(PSCTestCase):

    def afterSetUp(self):
        self.setRoles(('Manager',))
        self.portal.invokeFactory('PloneSoftwareCenter', 'psc')
        self.portal.psc.invokeFactory('PSCProject', 'proj')
        
        self.psc = self.portal.psc
        self.proj = self.portal.psc.proj
        releases = self.proj.releases 
        releases.invokeFactory('PSCRelease', '1.0')
        self.release = releases['1.0']

    def test_basic_storage(self):
        # try the registery
        wanted = ['archetype',]
        for w in wanted:
            self.assert_(w in getFileStorageNames(self.release))

    def test_adapters(self):
        # try various storage
        storage = DynamicStorage()
        self.assertEquals(storage.getName(self.release), 'archetype')
   

def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestStorage))
    return suite
