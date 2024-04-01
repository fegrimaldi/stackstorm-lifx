"""Defines a base action class for managing LIFX lights based on preset colors and brightness levels.

This module defines a class `BaseAction` which inherits from `st2common.runners.base_action.Action`. 
It provides a base action for managing LIFX lights based on preset colors and brightness levels.

Example:
    from st2common.runners.base_action import Action
    from lib.orion_manor import Brightness, Colors, HomeLights

    class BaseAction(Action):
        def __init__(self, config):
            super(BaseAction, self).__init__(config)
            self.color = Colors()
            self.brightness = Brightness()
            self.lights = HomeLights()

Attributes:
    None

Methods:
    __init__(config): Initializes the base action class with preset colors, brightness levels, and LIFX lights.

"""

from st2common.runners.base_action import Action
from lib.orion_manor import Brightness, Colors, HomeLights

class BaseAction(Action):
    """Defines a base action class for managing LIFX lights based on preset colors and brightness levels."""
    def __init__(self, config):
        """Initializes the base action class with preset colors, brightness levels, and LIFX lights.

        Args:
            config (dict): Configuration parameters for the action.

        """
        super(BaseAction, self).__init__(config)
        self.color = Colors()
        self.brightness = Brightness()
        self.lights = HomeLights()

  


