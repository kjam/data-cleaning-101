import random
from time import sleep
from datetime import datetime


def generate_machine_db():
    return {mid: generate_brand() for mid in range(100)}

def generate_brand():
    return random.choice(['Cisco', 'Juniper', 'Arista'])

def generate_example():
    sleep(random.random())
    return {
        'MachineId': random.randint(0,110), # yes, 110 intentionally >.<
        'AmbientTemp': random.randint(2,45) + random.random(),
        'Fan': random.randint(60, 2500),
        'CpuTemp': random.randint(2,55) + random.random(),
        'ObservationTime': datetime.now().isoformat(),
    }
