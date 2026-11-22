#!/bin/bash
# Make the install

# DIRS
WORKING_DIR=~/Builds/MicroRTS
REPO_DIR=~/Projects/MicroRTS-Bots

# Install dir
# I chose $WORKING_DIR/py in the sense that it will contain python code
# Don't have a better idea at this moment.
# Don't want to have $WORKING_DIR/code
INSTALL_DIR=$WORKING_DIR/py

if [ ! -d $WORKING_DIR ]; then
	echo -e "Running command: mkdir -m 700 $WORKING_DIR\n"
	mkdir -m 700 $WORKING_DIR
fi

# Remove the old $INSTALL_DIR
echo -e "Running command: rm -r $INSTALL_DIR\n"
rm -r $INSTALL_DIR

# Create the new working dir
echo -e "Running command: mkdir -m 700 $INSTALL_DIR\n"
mkdir -m 700 $INSTALL_DIR


# Copy the new data
cp -a $REPO_DIR/code/* $INSTALL_DIR
