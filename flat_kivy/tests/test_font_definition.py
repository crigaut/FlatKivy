""" Test module for the font definitions """

from pytest import fixture

from kivy.clock import ClockEvent
from kivy.uix.gridlayout import GridLayout

import flat_kivy.font_definitions as module
from flat_kivy.flatapp import FlatApp
from flat_kivy.uix.flatlabel import FlatLabel

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


class TestRampGroup:
    """ Test of the font ramp group class """

    @classmethod
    def setup_class(cls):
        """ Method executed when the class is called """
        cls.APP = MockApp()
        cls.LABEL = FlatLabel(size=[10, 15], text="test text",
                              style="test style", halign="center", valign="top",
                              max_lines=1)
        cls.RAMP_GROUP = module.RampGroup(["test style"],
                                          "Test ramp")
        cls.RAMP_GROUP.tracked_labels.append(cls.LABEL)
        cls.APP.run()

    def teardown_method(self):
        """ Method executed after each test """
        self.RAMP_GROUP.tracked_labels[0].style = "test style"

    def test_init(self):
        """ Test of the ramp group initialisation """
        assert self.RAMP_GROUP.tracked_labels == [self.LABEL]
        assert self.RAMP_GROUP.font_ramp == ["test style"]
        assert self.RAMP_GROUP.name == "Test ramp"
        assert self.RAMP_GROUP.current_style == "test style"
        assert self.RAMP_GROUP.max_iterations == 5
        assert isinstance(self.RAMP_GROUP.trigger_fit_check, ClockEvent)

    def test_copy_label_to_test_label(self):
        """ Test of the label attribute copy """
        test_label = self.RAMP_GROUP.copy_label_to_test_label(self.LABEL,
                                                              "test style")
        assert test_label.size == [10, 15]
        assert test_label.style == "test style"
        assert test_label.text == "test text"
        assert test_label.halign == "center"
        assert test_label.valign == "top"
        assert test_label.max_lines == 1

    def test_check_fit_for_all_labels(self):
        """ Test for text to fit into the labels """
        self.RAMP_GROUP.check_fit_for_all_labels(0)
        assert self.RAMP_GROUP.tracked_labels[0].style == "test style"

    def test_set_style(self):
        """ Test of style setter """
        self.RAMP_GROUP.set_style("modified style")
        assert self.RAMP_GROUP.tracked_labels[0].style == "modified style"

    def test_reset_track_adjustments(self):
        """ Test for resetting tracking parameters """
        self.RAMP_GROUP.tracked_labels.append(FlatLabel())
        self.RAMP_GROUP.reset_track_adjustments(0)
        assert len(self.RAMP_GROUP.tracked_labels) == 2
        self.RAMP_GROUP.tracked_labels.pop()

    def test_calculate_fit(self):
        """ Test for the resize calculation """
        assert self.RAMP_GROUP.calculate_fit(self.APP.root.children[0]) == "fits"

    # TODO: get_fit
    # TODO: add_label
    # TODO: remove_widget

class TestStyleManager:
    """ Test of the style manager class """

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

class MockApp(FlatApp):

    def build(self):
        layout = GridLayout()
        layout.add_widget(FlatLabel(text="test text"))
        return layout

    def on_start(self):
        self.stop()
