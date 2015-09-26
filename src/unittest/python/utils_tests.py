import unittest
from pybuilder.core import Project
import os
from pybuilder_nose import utils

class UtilsTest(unittest.TestCase):

  def setUp(self):
    self.project = Project('/path/to/project')
    self.project.set_property('dir_source_unittest_python', 'src/unittest/python')
    self.project.set_property('dir_source_main_python', 'src/main/python')
    self.project.set_property('dir_target','target')

  def test_properCwd(self):
    cwd = os.path.realpath(os.path.dirname(__file__) + "/../../../")

    self.assertEquals(cwd, utils.getProperCwd())

  def test_importDirs(self):
    cwd = utils.getProperCwd()
    dirs = utils.getImportantDirs(self.project)
    
    # src_dir
    self.assertEquals(dirs[0], cwd + "/" + self.project.get_property('dir_source_main_python'))

    # test_dir
    self.assertEquals(dirs[1], cwd + "/" + self.project.get_property('dir_source_unittest_python'))

    # html_dir
    self.assertEquals(dirs[2], cwd + "/target/reports/coverage_html")

    # xml_file
    self.assertEquals(dirs[3], cwd + "/target/reports/coverage.xml")

    # xunit_file
    self.assertEquals(dirs[4], cwd + "/target/reports/coverage.xunit.xml")

  def test_prepareArgs(self):
    self.project.set_property('nose_numeric', 1)
    self.project.set_property('nose_string', 'foobar')
    self.project.set_property('nose_array', ['one','two','three'])
    self.project.set_property('nose_true', True)
    self.project.set_property('nose_true-array', [True, True])
    
    self.project.set_property('nose_unused1', False)
    self.project.set_property('nose_unused2', None)

    args = utils.prepareArgs(self.project)

    self.assertEquals(len(args), 8)

    self.assertEquals('--numeric' in args, True)
    self.assertEquals('--string=foobar' in args, True)
    self.assertEquals('--array=one' in args, True)
    self.assertEquals('--array=two' in args, True)
    self.assertEquals('--array=three' in args, True)
    self.assertEquals('--true' in args, True)
    self.assertEquals('--true-array' in args, True)
    self.assertEquals('--true-array' in args, True)

