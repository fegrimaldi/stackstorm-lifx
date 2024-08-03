class Device:
    def __init__(self, light):
        try:
            self.mac_addr = light.get_mac_addr()
            self.ip_addr = light.get_ip_addr()
            self.color = light.get_color()
            self.power_level = light.power_level
            self.label = light.get_label()
            self.product_name = light.get_product_name()
        except AttributeError as e:
            print(f"Error initializing Device: {e}")

    def to_dict(self):
        return {
            'mac_addr': self.mac_addr,
            'ip_addr': self.ip_addr,
            'color': self.color,
            'power_level': self.power_level,
            'label': self.label,
            'product_name': self.product_name
        }
