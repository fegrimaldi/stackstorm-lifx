"""
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

   Copyright 2024 Silver Wolf Technoglogy
"""

from st2common.runners.base_action import Action
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
        self.theatre = (0, 65535, 43973, 2500)
        self.evening = (5461, 48495, 65535, 3500) #(35, 65535, 32767, 2500)
        self.daylight = (0, 0, 65535, 5600)

class BaseAction(Action):
    """Defines a base action class for managing LIFX lights based on preset colors and brightness levels."""
    def __init__(self, config):
        super(BaseAction, self).__init__(config)
        self.lights_config = self.config.get('lights', [])
        self.rooms = self.config.get('rooms', [])
        self.lights = {}

        for light in self.lights_config:
            self.lights[light['name']] = Light(light['mac'], light['ip'])
        self.logger.info('LIFX lights initialized')

        self.color = Colors()
        self.brightness = Brightness()
    

  


