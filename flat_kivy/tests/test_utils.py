""" Test module for the utility functions """

from os.path import abspath, dirname, join

import flat_kivy.utils as module

class TestGetMetricConvertion:
    """ Test of density-independant pixel convertion """

    @staticmethod
    def test_units():
        """ Test of the converted units """
        assert module.get_metric_conversion(("1", "dp")) == 1

    @staticmethod
    def test_convertion():
        """ Test of the convertion factors """
        assert module.get_metric_conversion(("3", "pt")) == 4
        assert module.get_metric_conversion(("1", "inch")) == 96
        assert module.get_metric_conversion(("1", "cm")) == 37.7952766418457
        assert module.get_metric_conversion(("1", "mm")) == 3.7795276641845703
        assert module.get_metric_conversion(("1", "sp")) == 1


class TestConstructTargetFileName:
    """ Test of the pyfile name"""

    @staticmethod
    def test_file_name_pyfile(tmpdir):
        """ Test of the path to the python file """
        temp_file = tmpdir.join("pyfile.py")
        assert module.construct_target_file_name('out', temp_file) == join(
            dirname(temp_file), 'out')

    @staticmethod
    def test_file_name_none():
        """ Test of the file name in case of none is provided """
        assert module.construct_target_file_name('out', None) == join(
            dirname(abspath('flat_kivy/utils.py')), 'out')
