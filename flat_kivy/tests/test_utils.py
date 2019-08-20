""" Test module for the utility functions """

from os.path import abspath, dirname, join

import flat_kivy.utils as module

class TestGetMetricConversion:
    """ Test of density-independant pixel conversion """

    @staticmethod
    def test_units():
        """ Test of the converted units """
        assert module.get_metric_conversion(("1", "dp")) == 1

    @staticmethod
    def test_convertion():
        """ Test of the conversion factors """
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


class TestConstructDataRessource:
    """ Test of the path to the data files """

    @staticmethod
    def test_data_path():
        """ Test of the data folder """
        assert module.construct_data_resource(' ') == abspath(
            'flat_kivy/data/ ')

    @staticmethod
    def test_data_file(tmpdir):
        """ Test of the contruction of a data file """
        temp_file = tmpdir.join("datafile.dat")
        assert module.construct_data_resource(temp_file) == join(
            dirname(temp_file), temp_file)


class TestGetIconChar:
    """ Test of the unicode string corresponding to an icon """

    @staticmethod
    def test_empty_icon():
        """ Test of the returned value for an empty icon """
        assert module.get_icon_char("") == ""

    @staticmethod
    def test_icon():
        """ Test of the string for a given icon """
        assert module.get_icon_char('fa-glass') == "\uf000"


class TestGetRGBAColors:
    """ Test of the color conversion from hex to RGBA """

    @staticmethod
    def test_pure_color():
        """ Test of the conversion of a pure color """
        assert module.get_rgba_color(("Grey", "0000")) == [1, 1, 1, 1]

    @staticmethod
    def test_color_alpha():
        """ Test of the conversion of a color with alpha correction """
        assert module.get_rgba_color(("Grey", "0000"), 0.5) == [1, 1, 1, 0.5]
