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

class Device:
    def __init__(self, light):
        try:
            self.label = light.get_label()
            self.mac_addr = light.get_mac_addr()
            self.ip_addr = light.get_ip_addr()
            self.color = str(light.get_color())
            self.power_level = light.power_level          
            self.product_name = light.get_product_name()
            self.product_features = light.get_product_features()
        except AttributeError as e:
            print(f"Error initializing Device: {e}")

    def to_dict(self):
        return {
            'label': self.label,
            'mac_addr': self.mac_addr,
            'ip_addr': self.ip_addr,
            'color': self.color,
            'power_level': self.power_level,
            'product_name': self.product_name,
            'product_features': self.product_features
        }
