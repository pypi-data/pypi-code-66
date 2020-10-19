"""Main module."""
import serial
import haversine
from . import position

class GPS:
    def __init__(self, port):
        self.port = port
        self.ser = serial.Serial(port, baudrate=9600, timeout=0.5)
        self.nmea_msg = ""
        self.position = position.Position()

    def setup(self):
        pass

    def restart(self):
        pass

    def clean_string(self):
        self.nmea_msg = ""

    def get_latitude(self):
        clean_string()
        while "GPGGA" not in self.nmea_msg:
            self.nmea_msg = ser.readline().decode("utf-8", "ignore")
        self.position.update(self.nmea_msg)
        return self.position.get_latitude()

    def get_longitude(self):
        clean_string()
        while "GPGGA" not in self.nmea_msg:
            self.nmea_msg = ser.readline().decode("utf-8", "ignore")
        self.position.update(self.nmea_msg)
        return self.position.get_longitude()

    def get_altitude(self):
        clean_string()
        while "GPGGA" not in self.nmea_msg:
            self.nmea_msg = ser.readline().decode("utf-8", "ignore")
        self.position.update(self.nmea_msg)
        return self.position.get_altitude()

    def get_current_location(self):
        clean_string()
        while "GPGGA" not in self.nmea_msg:
            self.nmea_msg = ser.readline().decode("utf-8", "ignore")
        self.position.update(self.nmea_msg)
        return self.position.get_current_location()

    def get_current_time(self):
        clean_string()
        while "GPGGA" not in self.nmea_msg:
            self.nmea_msg = ser.readline().decode("utf-8", "ignore")
        self.position.update(self.nmea_msg)
        return self.position.get_current_time()

    def set_distination(self, latitude, longitude):
        self.distination = (latitude, longitude)

    def get_distance(self, latitude, longitude):
        self.set_distination(latitude, longitude)
        distance = haversine(self.get_current_location(), self.distination)
        pass

    def get_speed(self):
        pass

    def get_time_of_arrival(self):
        pass

    def get_time_of_arrival(self, latitude, longitude):
        pass

    def store_distance(self):
        pass

    def get_mileage(self, date1, date2):
        pass
