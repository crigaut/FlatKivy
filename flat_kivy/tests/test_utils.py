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
