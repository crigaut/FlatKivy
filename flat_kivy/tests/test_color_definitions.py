""" Test module for the color definitions """

import flat_kivy.color_definitions as module

class TestColors:
    """ Test of the pre-defined colors """

    @staticmethod
    def test_keys():
        """ Test the names of the pre-defined colors """
        assert list(module.colors.keys()).sort() == [
            "Red", "Pink", "Purple", "DeepPurple", "Indigo", "Blue",
            "LightBlue", "Cyan", "Teal", "Green", "LightGreen", "Lime",
            "Yellow", "Amber", "Orange", "DeepOrange", "Brown", "Grey",
            "BlueGrey", "Gray", "BlueGray"].sort()

    @staticmethod
    def test_colors():
        """ Test of the pre-defined colors tones """
        assert list(module.colors["Red"].values()).sort() == [
            'e51c23', 'fde0dc', 'f9bdbb', 'f69988', 'f36c60', 'e84e40',
            'e51c23', 'dd191d', 'd01716', 'c41411', 'b0120a', 'ff7997',
            'ff5177', 'ff2d6f', 'e00032',].sort()
