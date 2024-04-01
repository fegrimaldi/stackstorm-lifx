"""Defines classes for managing LIFX lights and preset colors and brightness levels.

This module defines classes `Brightness`, `Colors`, and `HomeLights` for managing LIFX 
lights and preset colors and brightness levels.

Example:
    from lifxlan import Light

    class Brightness:
        def __init__(self):
            self.third = 21627
            self.half = 32767
            self.two_thirds = 43254
            self.full = 65535

    class Colors:
        def __init__(self):
            self.theatre = (0, 65535, 43973, 3500)
            self.evening = (5461, 48495, 65535, 3500)
            self.daylight = (0, 0, 65535, 5600)

    class HomeLights:
        def __init__(self):
            self.media_room = Light("d0:73:d5:27:20:7b", "172.16.1.104")
            self.bedroom = Light("d0:73:d5:21:a2:db", "172.16.1.90")
            self.living_room_left = Light("d0:73:d5:72:0d:d7", "172.168.1.91")
            self.living_room_right = Light("d0:73:d5:71:b9:2c", "172.168.1.143")
            self.office_one = Light("d0:73:d5:71:66:d1", "172.16.1.141")
            self.office_two = Light("d0:73:d5:5a:84:7e", "172.16.1.163")
            self.office_three = Light("d0:73:d5:71:ac:f1", "172.16.1.153")

Attributes:
    None
"""

from lifxlan import Light

class Brightness:
    """Defines brightness levels for LIFX lights."""
    def __init__(self):
        self.third = 21627
        self.half = 32767
        self.two_thirds = 43254
        self.full = 65535

class Colors:
    """Defines preset colors for LIFX lights."""
    def __init__(self):
        self.theatre = (0, 65535, 43973, 3500)
        self.evening = (5461, 48495, 65535, 3500)
        self.daylight = (0, 0, 65535, 5600)

class HomeLights:
    """Defines LIFX lights for various rooms in a home."""
    def __init__(self):
        self.media_room = Light("d0:73:d5:27:20:7b", "172.16.1.104")
        self.bedroom = Light("d0:73:d5:21:a2:db", "172.16.1.90")
        self.living_room_left = Light("d0:73:d5:72:0d:d7", "172.168.1.91")
        self.living_room_right = Light("d0:73:d5:71:b9:2c", "172.168.1.143")
        self.office_one = Light("d0:73:d5:71:66:d1", "172.16.1.141")
        self.office_two = Light("d0:73:d5:5a:84:7e", "172.16.1.163")
        self.office_three = Light("d0:73:d5:71:ac:f1", "172.16.1.153")
