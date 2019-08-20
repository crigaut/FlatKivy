""" Test module for the log manager"""

from os.path import abspath

from pytest import fixture

from flat_kivy.dbinterface import DBInterface
import flat_kivy.logmanager as module

class TestLogManager:
    """ Test of the LogManager object """

    @classmethod
    @fixture(autouse=True)
    def setup_class(cls, tmpdir):
        """ Method called before every test """
        cls.LOG_PATH = abspath(tmpdir.mkdir("log"))
        cls.LOG_MANAGER = module.LogManager(cls.LOG_PATH)

    def test_init(self):
        """ Test of the log manager initialisation """
        assert self.LOG_MANAGER.log_path == self.LOG_PATH
        assert isinstance(self.LOG_MANAGER.log_interface, DBInterface)
        assert self.LOG_MANAGER.touch_id == 0

    def test_on_device_id(self, capsys):
        """ Test of the device id collection """
        self.LOG_MANAGER.on_device_id(DBInterface, 0)
        capture = capsys.readouterr()
        assert capture.out == 'in on device id 0\n'
