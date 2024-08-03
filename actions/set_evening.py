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

import sys
from lib import action
class SetEveningAction(action.BaseAction):
    def run(self):
        rooms = ["media_room", "office"]

        for room_name in rooms:
            self.set_room_lights(room_name)

        return True

    def set_room_lights(self, room_name):
        for room in self.rooms:
            if room["name"] == room_name:
                lights = room["lights"]
                for light in lights:
                    try:
                        self.lights[light].set_color(self.color.evening, 2000)
                        self.lights[light].set_brightness(self.brightness.two_thirds, 2000)
                    except Exception as err:
                        self.logger.error(f"Failed to set light {light} in {room_name}: {err}")
                        sys.exit(1)
                self.logger.info(f"Successfully set lights in the {room_name} to the evening scene.")
                break
        else:
            self.logger.warning(f"Room {room_name} not found.")


