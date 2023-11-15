import os
import socket
from bme280 import readBME280ID, readBME280All

class Stats():
    def __init__(self):
        (chip_id, chip_version) = readBME280ID()
        print('getting BME280 info:')
        print(f"\tchip id: {chip_id}")
        print(f"\tchip_version: {chip_version}")
        
        self.hostname = os.getenv('SENSO_HOST_NAME', socket.gethostname())
        self.ip = os.getenv('SENSO_HOST_IP', '0.0.0.0')
   
    def get_environment(self):
        temperature, pressure, humidity = readBME280All()
        
        baro_sensor = {
            'temperature': round(temperature, 1),
            'pressure': round(pressure, 1),
            'humidity': round(humidity, 1)
        }

        return baro_sensor
    
    def get_network(self):
        net = {
            'hostname': self.hostname,
            'local_ip': self.ip
        }

        return net

    def get_all(self, influx_format=False):
        environment = self.get_environment()
        network = self.get_network()

        tags = {
            'hostname': network['hostname'],
            'ip': network['local_ip']
        }

        if influx_format:
            stats = [
                {
                    'measurement': 'environment',
                    'tags': tags,
                    'fields': {
                        'temperature_c': environment['temperature'],
                        'pressure': environment['pressure'],
                        'humidity': environment['humidity']
                    }
                }
            ]
        else:
            stats = {
                'environment': environment,
                'network': network
            }

        return stats