""" Test module for the database interbase """

from datetime import datetime, timedelta, date
from os.path import exists, join

from pytest import fixture
from kivy.storage.jsonstore import JsonStore
from kivy.clock import ClockEvent

import flat_kivy.dbinterface as module

class TestDBInterface:
    """ Test of the data base interface class """

    @classmethod
    @fixture(autouse=True)
    def setup_class(cls, tmpdir):
        """ Method executed when the class is called """
        cls.data_dir = tmpdir.mkdir("data")
        cls.INTERFACE = module.DBInterface(cls.data_dir, "Test")
        cls.INTERFACE.data.put("table", row={"label":{"value":[0, 1]}})


    def test_init(self):
        """ Test of the interface initialisation """
        assert isinstance(self.INTERFACE.data, JsonStore)
        assert isinstance(self.INTERFACE.reset_timers, JsonStore)
        assert isinstance(self.INTERFACE.sync, ClockEvent)

    def test_ensure_dir(self):
        """ Test of the folder existance verification """
        self.INTERFACE.ensure_dir(self.data_dir)
        assert exists(self.data_dir)

    def test_check_reset(self):
        """ Test of the clock reset verification """
        self.INTERFACE.check_reset(0)
        assert not exists(join(
            self.data_dir, "Test-%Y-%m-%d-reset_timers.json"))
        assert not exists(join(self.data_dir, "Test-reset_timers.json"))

    def test_trigger_sync(self, capsys):
        """ Test of data synch """
        self.INTERFACE.trigger_sync(0)
        capture = capsys.readouterr()
        assert capture.out == 'syncing\n'

    def test_get_entry(self):
        """ Test of the database value getter """
        tmp_data = JsonStore(self.data_dir + "Temp")
        tmp_data.put("table", row={"label":{"value":[0, 1]}})
        assert self.INTERFACE.get_entry("table", "row", "label") == (
            tmp_data["table"]["row"]["label"]["value"]
        )

    def test_get_row(self):
        """ Test of the database row getter """
        tmp_data = JsonStore(self.data_dir + "Temp")
        tmp_data.put("table", row={"label":{"value":[0, 1]}})
        assert self.INTERFACE.get_row("table", "row") == (
            tmp_data["table"]["row"]
        )

    def test_get_table(self):
        """ Test of the database table getter """
        tmp_data = JsonStore(self.data_dir + "Temp")
        tmp_data.put("table", row={"label":{"value":[0, 1]}})
        assert self.INTERFACE.get_table("table") == tmp_data["table"]

    def test_remove_entry(self):
        """ Test of database entry removal """
        self.INTERFACE.remove_entry("table", "row", "label", 0)
        assert self.INTERFACE.data["table"]["row"]["label"] == {"value":[1]}

    def test_append_entry(self):
        """ Test of a database entry adding """
        self.INTERFACE.append_entry("table", "row", "label", 2)
        assert self.INTERFACE.data["table"]["row"]["label"] == (
            {"value":[0, 1, 2]}
        )

    def test_set_entry(self):
        """ Test of the database entry setter """
        self.INTERFACE.set_entry("table", "row", "label", ["a", "b"])
        assert self.INTERFACE.data["table"]["row"]["label"] == (
            {"value":["a", "b"]}
        )

    def test_get_time(self):
        """ Test of the time getter """
        assert self.INTERFACE.get_time() <= (
            datetime.utcnow() + timedelta(seconds=1)
        )

    def test_convert_time_to_json_ymd(self):
        """ Test of the date conversion """
        ymd = date(2000, 12, 31)
        assert self.INTERFACE.convert_time_to_json_ymd(ymd) == '2000-12-31'

    def test_convert_time_to_json(self):
        """ Test of the time conversion """
        time = datetime(2000, 12, 31, hour=7, minute=35, second=18)
        assert self.INTERFACE.convert_time_to_json(time) == (
            '2000-12-31T07:35:18'
        )

    def test_convert_time_from_json(self):
        """ Test of the time conversion from a file """
        time = self.INTERFACE.convert_time_from_json('2000-12-31T07:35:18')
        assert time.year == 2000
        assert time.month == 12
        assert time.day == 31
        assert time.hour == 7
        assert time.minute == 35
        assert time.second == 18
