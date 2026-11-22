# Configuration file for the project
# Intended to be imported by other modules.
# Preferred to have a config.py instead of .env because i want to track it with git.
# I don't think i will have a .env file, but if so, i will invalidate this file.

# Directories
# When working with paths:
#   - Use absolute paths
#   - wrap the path inside a Path object from the pathlib module

from pathlib import Path

# Paths
WORKING_DIR_LOCAL = Path("/home/marius-vlad/Builds/MicroRTS")
WORKING_DIR_GOOGLE_COLAB = Path("") # Google colab may need it's own working dir. Don't know yet if i need this or nor. I may or i may not need it. I put in a dummy path for now.

# Flags (True/False)
USE_GOOGLE_COLAB = True

# Addresses

# Manager has an internal server where MicroRTS and agents connect to.
# Manager local server address
MANAGER_LOCAL_SERVER_ADDRESS = ""

# Ports

# Manager local server ports.
# If more that 1 ports are needed, specify in the list.
# Probably 1 is enough, but don't know this yet.
MANAGER_LOCAL_SERVER_PORTS = [""]