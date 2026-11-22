# Configuration file for the project
# Intended to be imported by other modules.
# Preferred to have a config.py instead of .env because i want to track it with git.
# I don't think i will have a .env file, but if so, i will invalidate this file.

from pathlib import Path

# Directories
# When working with paths:
#   - Use absolute paths
#   - wrap the path inside a Path object from the pathlib module

# Change this if needed
WORKING_DIR_LOCAL = Path("/home/marius-vlad/Builds/MicroRTS")
WORKING_DIR_GOOGLE_COLAB = Path("") # Google colab may need it's own working din. Don't know yet if i need this or nor. I may or i may not need it. I put in a dummy path for now.