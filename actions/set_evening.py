"""Provides an action to set evening ambiance in a media room by adjusting lights.

This module defines a class `SetEveningAction` which inherits from `action.BaseAction`. 
It enables users to set the evening ambiance in a media room by adjusting the color and 
brightness of the lights.

Example:
    from lib import action

    class SetEveningAction(action.BaseAction):
        def run(self):
            self.lights.media_room.set_color(self.color.evening, 2000)
            self.lights.media_room.set_brightness(self.brightness.half, 2000)
            return None

Attributes:
    None

Methods:
    run(): Executes the action to set evening ambiance by adjusting the color and brightness of the lights.

"""

from lib import action

class SetEveningAction(action.BaseAction):
    def run(self):
        """Executes the action to set evening ambiance by adjusting the color and brightness of the lights.

        Returns:
            None: The function does not return any value.
        """
        self.lights.media_room.set_color(self.color.evening, 2000)
        self.lights.media_room.set_brightness(self.brightness.two_thirds, 2000)

        self.lights.office_one.set_color(self.color.evening, 2000)
        self.lights.office_one.set_brightness(self.brightness.two_thirds, 2000)

        self.lights.office_two.set_color(self.color.evening, 2000)
        self.lights.office_two.set_brightness(self.brightness.two_thirds, 2000)

        self.lights.office_three.set_color(self.color.evening, 2000)
        self.lights.office_three.set_brightness(self.brightness.two_thirds, 2000)                        
        return None

