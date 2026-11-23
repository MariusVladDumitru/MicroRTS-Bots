from config import *

# Testing DIRs paths
# Making sure ALL DIR's variables are the right values
def test_paths():
    # correct values for DIR's variables
    WORKING_DIR_LOCAL_CORRECT_VALUE = "/home/marius-vlad/Builds/MicroRTS"
    WORKING_DIR_GOOGLE_COLAB_CORRECT_VALUE = ""

    assert WORKING_DIR_LOCAL == Path(WORKING_DIR_LOCAL_CORRECT_VALUE)
    assert WORKING_DIR_GOOGLE_COLAB == Path(WORKING_DIR_GOOGLE_COLAB_CORRECT_VALUE)

# Testing Flags
def test_flags():
    USE_GOOGLE_COLAB_CORRECT_VALUE = True

    assert USE_GOOGLE_COLAB == USE_GOOGLE_COLAB_CORRECT_VALUE

# Testing Instances
# One instance is one pair MicroRTS-Agents
def test_instances():
    INSTANCES_CORRECT_VALUE = 1

    assert INSTANCES == INSTANCES_CORRECT_VALUE

# Testing URL's
def test_addresses():
    SERVER_ADDRESS_CORRECT_VALUE = ""

    assert SERVER_ADDRESS == SERVER_ADDRESS_CORRECT_VALUE

def test_ports():
    MICRORTS_SERVER_PORTS_CORRECT_VALUE = [] # this is a list of int's
    AGENTS_SERVER_PORTS_CORRECT_VALUE = [] # this is a list of int's

    # total number of ports used by the server.
    total_ports = 2 * INSTANCES

    assert len(MICRORTS_SERVER_PORTS) + len(AGENTS_SERVER_PORTS) == total_ports
    assert MICRORTS_SERVER_PORTS == MICRORTS_SERVER_PORTS_CORRECT_VALUE
    assert AGENTS_SERVER_PORTS == AGENTS_SERVER_PORTS_CORRECT_VALUE
