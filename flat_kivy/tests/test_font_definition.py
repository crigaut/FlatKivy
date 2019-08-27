""" Test module for the font definitions """

from pytest import fixture

import flat_kivy.font_definitions as module

class TestFontStyle:
    """ Test of the font style object """

    @classmethod
    @fixture(autouse=True)
    def setup_class(cls, tmpdir):
        """ Method executed when the class is called """
        cls.FONT_FILE = tmpdir.mkdir("fonts").join("test_font")
        cls.FONT_STYLE = module.FontStyle(cls.FONT_FILE, "Test font", 8, 12, 1)

    def test_init(self):
        """ Test of the font style initialisation """
        assert self.FONT_STYLE.font_file == self.FONT_FILE
        assert self.FONT_STYLE.name == "Test font"
        assert self.FONT_STYLE.size_mobile == 8
        assert self.FONT_STYLE.size_desktop == 12
        assert self.FONT_STYLE.alpha == 1


    def test_instance(self):
        """ Test of the instance creation """
        assert isinstance(self.FONT_STYLE, module.FontStyle)
