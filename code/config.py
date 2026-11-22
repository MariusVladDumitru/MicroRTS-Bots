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

# Manager spawns an internal server where all instances of MicroRTS and all instances of agents connect to.
# This means that there can be more that 1 pair MicroRTS-Agents Running.
# An instance is one pair MicroRTS-Agents
# There is only one server address -> the internal server of the manager.
# Minimum number of ports is 2 -> on one port MicroRTS connects, on the other the agents connect.
# Total Number of ports used by the server = 2 x INSTANCES (how many pairs of MicroRTS-Agents) i have

# Instances
# The number of pairs MicroRTS-Agents.
# Each pair MicroRTS-Agents is unique
INSTANCES = 1

# Manager local server address
SERVER_ADDRESS = ""

# Ports

# Ports where instances of MicroRTS are allowed to connect to.
MICRORTS_SERVER_PORTS=[""]

# Ports where instances of Agents are allowed to connect to.
AGENTS_SERVER_PORTS=[""]