import os
import random
import sys
from time import sleep
from datetime import datetime

# PYTHON_PATH is an issue for some OS re: dask execution
sys.path.append(os.path.dirname(__file__))

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
