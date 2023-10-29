# GxPED2_Helper
Python script that makes using the GxEPD library easier to use!

I have started to work with ePaper displays, and find many of the libraries requires days of reading through the examples just to understand how to get the microcontroller to communicate with the display.  The GxEPD2 library by ZinggJM seems to be one of the least problematic once the initial parameters are set, but it is still very cumbersome to set up in the first place.

This is a script written in Python that takes nearly all the work ZinggJM has done, and allows the user to answer a few questions which will create a far simpler start to using the ePaper display.  The only part of the configuration not translated is that which is required for the largest grayscale displays.

Simply run the python script and answer the questions it asks.  The script will create an ino file named ePaper_Baseline.ino in the same directory as the script.  This file can be referenced by placing it in the Arduino project folder and using the directive ```#include "ePaper_Baseline.ino"``` or the contents can be copied to an Arduino sketch.
