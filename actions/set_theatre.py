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

class SetTheatreAction(action.BaseAction):
    def run(self):
        # * Set lights in the media room to evening scene.
        for room in self.rooms:
            if room["name"] == "media_room":
                lights = room["lights"]
        for light in lights:
            try:
                self.lights[light].set_color(self.color.theatre, 2000)
                self.lights[light].set_brightness(self.brightness.third, 2000)
            except Exception as err:
                self.logger.error(f"Failed to set theatre scene in the media room. msg: {err}")
                sys.exit(1)
        self.logger.info("Successfully set light in the media room to the theatre scene.")
        return True
