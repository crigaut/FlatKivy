""" Test module for the font definitions """

from pytest import fixture

import flat_kivy.font_definitions as module

# TODO: get_style
# TODO: get_font_ramp_group

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


# TODO: RampGroup

class TestStyleManager:
    """ Test of the style manager instance """

    @classmethod
    def setup_class(cls):
        """ Method executed when the class is called """
        cls.STYLE_MANAGER = module.StyleManager()

    def test_init(self):
        """ Test of the stye manager initialisation """
        assert self.STYLE_MANAGER.styles == {}
        assert self.STYLE_MANAGER.ramp_groups == {}
        assert self.STYLE_MANAGER.font_ramps == {}

    def test_add_style(self, tmpdir):
        """ Test of style addition """
        font_file = tmpdir.mkdir("fonts").join("test_add")
        self.STYLE_MANAGER.add_style(font_file, "Test add", 6, 10, 1)
        assert "Test add" in self.STYLE_MANAGER.styles
