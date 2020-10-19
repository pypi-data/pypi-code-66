import pynmea2

class Position:
    """ position class, used to store latitude, longitude and altitude.
        get_latitude, get_longitude and get_current_location methods
    """

    def __init__(self):
        self.latitude = ""
        self.longitude = ""
        self.altitude = ""
        self.location = ""

    def update(self, nmea_msg):
        if "GPGGA" in nmea_msg:
            msg = pynmea2.parse(nmea_msg)
            self.latitude = msg.latitude
            self.longitude = msg.longitude
            self.altitude = msg.altitude

    def get_latitude(self):
        return self.latitude

    def get_longitude(self):
        return self.longitude

    def get_altitude(self):
        return self.altitude

    def get_current_time():
        return self.time

    def get_current_location(self):
        location = (self.latitude, self.longitude)
        return location
