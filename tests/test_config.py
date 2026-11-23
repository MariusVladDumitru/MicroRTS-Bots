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
def test_server_address():
    SERVER_ADDRESS_CORRECT_VALUE = ""

    assert SERVER_ADDRESS == SERVER_ADDRESS_CORRECT_VALUE

def test_server_port():
    # pozitive int number
    # range: [49152–65535]
    SERVER_PORT_CORRECT_VALUE = -1 # also change here

    assert isinstance(SERVER_PORT, int) == True
    assert SERVER_PORT >= 49152
    assert SERVER_PORT <= 65535
    assert SERVER_PORT == SERVER_PORT_CORRECT_VALUE