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
        scene = paramaters.get("scene", None)
        self.scene = self.scenes.get(scene, None)


        if self.scene is None:
            self.logger.info(f"Scene {scene} not found. Using color and brightness input.")
            self.color = paramaters["color"]
            self.brightness = paramaters["brightness"]
        else:
            self.logger.info(f"Scene {scene} found. Using defined color and brightness settings.")
            self.color = self.scene["color"]
            self.brightness = self.scene["brightness"]

        # Check to make sure we have a valid color and brightness
        # If a scene name is provided, we don't need a color or brightness

        if not self.color or not self.brightness:
            self.logger.error("A valid scene name or color and brightness combo are required for setting a scene.")
            sys.exit(1)
      
        # * convert the brightness as a percentage to a range of 16 bit values (0-65535)
        if self.brightness < 0 or self.brightness > 100:
            raise ValueError("Brightness must be between 0 and 100%")
        self.brightness = int((self.brightness / 100) * 65535)
    
        # * set the lights in each room to the desired scene
        self.logger.info("Setting lights in each room to the requested scene.")
        for room_name in rooms:
            self.set_room_lights(room_name)
        return True

    # Sets the lights in a given room to the desired scene settings.
    # If a timeout to the response occurs, we try to set the light scene one more time. 
    def set_room_lights(self, room_name):
        for room in self.rooms:
            if room["name"] == room_name:
                lights = room["lights"]
                for light in lights:
                    try:
                        self.lights[light].set_color(self.color, 500)
                        self.lights[light].set_brightness(self.brightness, 500)
                    except WorkflowException as err:
                        self.logger.warning(f"Timeout setting light {light} in {room_name}. Retrying. msg: {err}")
                        try:
                            self.lights[light].set_color(self.color, 500)
                            self.lights[light].set_brightness(self.brightness, 500)
                        except Exception as err:
                            self.logger.warning(f"Failed to set light {light} in {room_name}: {err}")
                            pass
                    except Exception as err:
                        self.logger.error(f"Failed to set light {light} in {room_name}: {err}")
                        sys.exit(1)
                self.logger.info(f"Successfully set lights in the {room_name} to the requested scene.")
                break
        else:
            self.logger.warning(f"Room {room_name} not found.")

