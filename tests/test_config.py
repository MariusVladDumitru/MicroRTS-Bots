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

# Testing URL's
def test_addresses():
    MANAGER_LOCAL_SERVER_ADDRESS_CORRECT_VALUE = ""

    assert MANAGER_LOCAL_SERVER_ADDRESS == MANAGER_LOCAL_SERVER_ADDRESS_CORRECT_VALUE

def test_ports():
    MANAGER_LOCAL_SERVER_PORTS_CORRECT_VALUE = [""]

    assert MANAGER_LOCAL_SERVER_PORTS == MANAGER_LOCAL_SERVER_PORTS_CORRECT_VALUE