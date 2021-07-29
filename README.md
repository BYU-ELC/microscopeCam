# microscopeCam

Code for the microscope camera raspberry pi. Put a normally closed button between gpio pin 14 and ground. The pi will start up and show the camera view for 10 minutes before cleanly shutting down unless the reset button is pressed, which will reset the 10 minute timer.
