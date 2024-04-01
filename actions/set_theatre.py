"""Provides an action to set theatre ambiance in a media room by adjusting lights.

This module defines a class `SetTheatreAction` which inherits from `action.BaseAction`. 
It enables users to set the theatre ambiance in a media room by adjusting the color and 
brightness of the lights.

Example:
    from lib import action

    class SetTheatreAction(action.BaseAction):
        def run(self):
            self.lights.media_room.set_color(self.color.theatre, 2000)
            self.lights.media_room.set_brightness(self.brightness.third, 2000)
            return None

Attributes:
    None

Methods:
    run(): Executes the action to set theatre ambiance by adjusting the color and brightness of the lights.

"""

from lib import action

class SetTheatreAction(action.BaseAction):
    def run(self):
        """Executes the action to set theatre ambiance by adjusting the color and brightness of the lights.

        Returns:
            None: The function does not return any value.
        """
        self.lights.media_room.set_color(self.color.theatre, 2000)
        self.lights.media_room.set_brightness(self.brightness.third, 2000)
        return None
