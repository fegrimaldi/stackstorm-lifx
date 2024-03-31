from st2common.runners.base_action import Action

from lib.orion_manor import Brightness, Colors, HomeLights


class BaseAction(Action):
    def __init__(self, config):
        super(BaseAction, self).__init__(config)
        # self._latitude = self.config['latitude']
        self.color = Colors()
        self.brightness = Brightness()
        self.lights = HomeLights()

  


