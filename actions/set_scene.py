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
from lifxlan import WorkflowException

class SetScene(action.BaseAction):
    def run(self, **paramaters):
        rooms = paramaters.get("rooms", [])
        self.color = paramaters.get("color", "daylight")
        self.brightness = paramaters.get("brightness", "full")

        if self.brightness < 0 or self.brightness > 100:
            raise ValueError("Brightness must be between 0 and 100%")
        self.brightness = int((self.brightness / 100) * 65535)
    
        for room_name in rooms:
            self.set_room_lights(room_name)
        return True

    def set_room_lights(self, room_name):
        for room in self.rooms:
            if room["name"] == room_name:
                lights = room["lights"]
                for light in lights:
                    try:
                        self.lights[light].set_color(self.color, 500)
                        self.lights[light].set_brightness(self.brightness, 500)
                    except WorkflowException as err:
                        self.logger.warning(f"Timeout setting light {light} in {room_name}: {err}")
                        try:
                            self.lights[light].set_color(self.color, 500)
                            self.lights[light].set_brightness(self.brightness, 500)
                        except Exception as err:
                            self.logger.warning(f"Failed to set light {light} in {room_name}: {err}")
                            pass
                    except Exception as err:
                        self.logger.error(f"Failed to set light {light} in {room_name}: {err}")
                        sys.exit(1)
                self.logger.info(f"Successfully set lights in the {room_name} to the daylight scene.")
                break
        else:
            self.logger.warning(f"Room {room_name} not found.")

