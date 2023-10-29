import os
# VARIABLES WHOSE VALUES ARE PROVIDED BY THE USER

colordepth = ""
driver = ""
modelnum = ""
height = ""
width = ""
chipset = ""
descr = ""
bufferpad = ""
bufferspace = ""
procindex = ""
proctype = ""
pincs = ""
pindc = ""
pinrst = ""
pinbusy = ""
pindin = ""
pinclk = ""
outputfile = None

displays = [
	['2', 'GxEPD2_102', 'GDEW0102T4', '80', '128', 'UC8175', '(WFT0102CZA2)', ''], 
	['2', 'GxEPD2_150_BN', 'DEPG0150BN', '200', '200', 'SSD1681', '(FPC8101), TTGO T5 V2.4.1', ''], 
	['2', 'GxEPD2_154', 'GDEP015OC1', '200', '200', 'IL3829', '(WFC0000CZ07), no longer available', ''], 
	['2', 'GxEPD2_154_D67', 'GDEH0154D67', '200', '200', 'SSD1681', '(HINK-E154A07-A1)', ''], 
	['2', 'GxEPD2_154_T8', 'GDEW0154T8', '152', '152', 'UC8151 (IL0373)', '(WFT0154CZ17)', ''], 
	['2', 'GxEPD2_154_M09', 'GDEW0154M09', '200', '200', 'JD79653A', '(WFT0154CZB3)', ''], 
	['2', 'GxEPD2_154_M10', 'GDEW0154M10', '152', '152', 'UC8151D', '(WFT0154CZ17)', ''], 
	['2', 'GxEPD2_154_GDEY0154D67', 'GDEY0154D67', '200', '200', 'SSD1681', '(FPC-B001 20.05.21)', ''], 
	['2', 'GxEPD2_213', 'GDE0213B1', '122', '250', 'IL3895', '(HINK-E0213-G01), phased out', ''], 
	['2', 'GxEPD2_213_B72', 'GDEH0213B72', '122', '250', 'SSD1675A (IL3897)', '(HINK-E0213A22-A0 SLH1852)', ''], 
	['2', 'GxEPD2_213_B73', 'GDEH0213B73', '122', '250', 'SSD1675B', '(HINK-E0213A22-A0 SLH1914)', ''], 
	['2', 'GxEPD2_213_B74', 'GDEM0213B74', '122', '250', 'SSD1680', 'FPC-7528B)', ''], 
	['2', 'GxEPD2_213_flex', 'GDEW0213I5F', '104', '212', 'UC8151 (IL0373)', '(WFT0213CZ16)', ''], 
	['2', 'GxEPD2_213_M21', 'GDEW0213M21', '104', '212', 'UC8151 (IL0373)', '(WFT0213CZ16)', ''], 
	['2', 'GxEPD2_213_T5D', 'GDEW0213T5D', '104', '212', 'UC8151D', '(WFT0213CZ16)', ''], 
	['2', 'GxEPD2_213_BN', 'DEPG0213BN', '122', '250', 'SSD1680', '(FPC-7528B), TTGO T5 V2.4.1, V2.3.1', ''], 
	['2', 'GxEPD2_213_GDEY0213B74', 'GDEY0213B74', '122', '250', 'SSD1680', '(FPC-A002 20.04.08)', ''], 
	['2', 'GxEPD2_260', 'GDEW026T0', '152', '296', 'UC8151 (IL0373)', '(WFT0154CZ17)', ''], 
	['2', 'GxEPD2_260_M01', 'GDEW026M01', '152', '296', 'UC8151 (IL0373)', '(WFT0260CZB2)', ''], 
	['2', 'GxEPD2_266_BN', 'DEPG0266BN', '152', '296', 'SSD1680', '(FPC7510), TTGO T5 V2.66, TTGO T5 V2.4.1', ''], 
	['2', 'GxEPD2_266_GDEY0266T90', 'GDEY0266T90', '152', '296', 'SSD1680', '(FPC-A003 HB)', ''], 
	['2', 'GxEPD2_270', 'GDEW027W3', '176', '264', 'EK79652 (IL91874)', '(WFI0190CZ22)', ''], 
	['2', 'GxEPD2_270_GDEY027T91', 'GDEY027T91', '176', '264', 'SSD1680', '(FB)', ''], 
	['2', 'GxEPD2_290', 'GDEH029A1', '128', '296', 'SSD1608 (IL3820)', '(E029A01-FPC-A1 SYX1553)', ''], 
	['2', 'GxEPD2_290_T5', 'GDEW029T5', '128', '296', 'UC8151 (IL0373)', '(WFT0290CZ10)', ''], 
	['2', 'GxEPD2_290_T5D', 'GDEW029T5D', '128', '296', 'UC8151D', '(WFT0290CZ10)', ''], 
	['2', 'GxEPD2_290_I6FD', 'GDEW029I6FD', '128', '296', 'UC8151D', '(WFT0290CZ10)', ''], 
	['2', 'GxEPD2_290_T94', 'GDEM029T94', '128', '296', 'SSD1680', '(FPC-7519 rev.b)', ''], 
	['2', 'GxEPD2_290_T94_V2', 'GDEM029T94', '128', '296', 'SSD1680', '(FPC-7519 rev.b), Waveshare 2.9" V2 variant', ''], 
	['2', 'GxEPD2_290_BS', 'DEPG0290BS', '128', '296', 'SSD1680', '(FPC-7519 rev.b)', ''], 
	['2', 'GxEPD2_290_M06', 'GDEW029M06', '128', '296', 'UC8151D', '(WFT0290CZ10)', ''], 
	['2', 'GxEPD2_290_GDEY029T94', 'GDEY029T94', '128', '296', 'SSD1680', '(FPC-A005 20.06.15)', ''], 
	['2', 'GxEPD2_371', 'GDEW0371W7', '240', '416', 'UC8171 (IL0324)', '(missing)', ''], 
	['2', 'GxEPD2_370_TC1', 'ED037TC1', '280', '480', 'SSD1677', '(ICA-FU-20 ichia 2029), Waveshare 3.7"', ''], 
	['2', 'GxEPD2_420', 'GDEW042T2', '300', '400', 'UC8176 (IL0398)', '(WFT042CZ15)', ''], 
	['2', 'GxEPD2_420_M01', 'GDEW042M01', '300', '400', 'UC8176 (IL0398)', '(WFT042CZ15)', ''], 
	['2', 'GxEPD2_420_GDEY042T91', 'GDEY042T91', '300', '400', 'SSD1683', '(no inking)', ''], 
	['2', 'GxEPD2_583', 'GDEW0583T7', '448', '600', 'UC8159c (IL0371)', '(missing)', ''], 
	['2', 'GxEPD2_583_T8', 'GDEW0583T8', '480', '648', 'EK79655 (GD7965)', '(WFT0583CZ61)', ''], 
	['2', 'GxEPD2_583_GDEQ0583T31', 'GDEQ0583T31', '480', '648', 'UC8179', '(P583010-MF1-B)', ''], 
	['2', 'GxEPD2_750', 'GDEW075T8', '384', '640', 'UC8159c (IL0371)', '(WF0583CZ09)', ''], 
	['2', 'GxEPD2_750_T7', 'GDEW075T7', '480', '800', 'EK79655 (GD7965)', '(WFT0583CZ61)', ''], 
	['2', 'GxEPD2_750_YT7', 'GDEY075T7', '480', '800', 'UC8179 (GD7965)', '(FPC-C001 20.8.20)', ''], 
	['2', 'GxEPD2_1160_T91', 'GDEH116T91', '640', '960', 'SSD1677', '(none or hidden)', ''], 
	['2', 'GxEPD2_1248', 'GDEW1248T3', '984', '1304', 'UC8179', '(WFT1248BZ23,WFT1248BZ24)', ''], 
	['3', 'GxEPD2_154c', 'GDEW0154Z04', '200', '200', 'IL0376F', '(WFT0000CZ04), no longer available', ''], 
	['3', 'GxEPD2_154_Z90c', 'GDEH0154Z90', '200', '200', 'SSD1681', '(HINK-E154A07-A1)', ''], 
	['3', 'GxEPD2_213c', 'GDEW0213Z16', '104', '212', 'UC8151 (IL0373)', '(WFT0213CZ16)', ''], 
	['3', 'GxEPD2_213_Z19c', 'GDEH0213Z19', '104', '212', 'UC8151D', '(HINK-E0213A20-A2 2020-11-19)', ''], 
	['3', 'GxEPD2_213_Z98c', 'GDEY0213Z98', '122', '250', 'SSD1680', '(FPC-A002 20.04.08)', ''], 
	['3', 'GxEPD2_266c', 'GDEY0266Z90', '152', '296', 'SSD1680', '(FPC-7510)', ''], 
	['3', 'GxEPD2_270c', 'GDEW027C44', '176', '264', 'IL91874', '(WFI0190CZ22)', ''], 
	['3', 'GxEPD2_290c', 'GDEW029Z10', '128', '296', 'UC8151 (IL0373)', '(WFT0290CZ10)', ''], 
	['3', 'GxEPD2_290_Z13c', 'GDEH029Z13', '128', '296', 'UC8151D', '(HINK-E029A10-A3 20160809)', ''], 
	['3', 'GxEPD2_290_C90c', 'GDEM029C90', '128', '296', 'SSD1680', '(FPC-7519 rev.b)', ''], 
	['3', 'GxEPD2_420c', 'GDEW042Z15', '300', '400', 'UC8176 (IL0398)', '(WFT0420CZ15)', ''], 
	['3', 'GxEPD2_420c_Z21', 'GDEQ042Z21', '300', '400', 'UC8276', '(hidden)', ''], 
	['3', 'GxEPD2_583c', 'GDEW0583Z21', '448', '600', 'UC8159c (IL0371)', '(missing)', ''], 
	['3', 'GxEPD2_583c_Z83', 'GDEW0583Z83', '480', '648', 'EK79655 (GD7965)', '(WFT0583CZ61)', ''], 
	['3', 'GxEPD2_750c', 'GDEW075Z09', '384', '640', 'UC8159c (IL0371)', '(WF0583CZ09)', ''], 
	['3', 'GxEPD2_750c_Z08', 'GDEW075Z08', '480', '800', 'EK79655 (GD7965)', '(WFT0583CZ61)', ''], 
	['3', 'GxEPD2_750c_Z90', 'GDEH075Z90', '528', '880', 'SSD1677', '(HINK-E075A07-A0)', ''], 
	['3', 'GxEPD2_1248c', 'GDEY1248Z51', '984', '1304', 'UC8179', '(WFT1248BZ23,WFT1248BZ24)', ''], 
	['4', 'GxEPD2_437c', 'Waveshare 4.37" 4-color', '', '', '', '', ''], 
	['7', 'GxEPD2_565c', 'Waveshare 5.65" 7-color', '', '', '', '', ''], 
	['7', 'GxEPD2_730c_GDEY073D46', 'GDEY073D46', '480', '800', '7-color, (N-FPC-001 2021.11.26)', '', ''], 
	['G', 'GxEPD2_it60', 'ED060SCT', '', '', '', '', ''], 
	['G', 'GxEPD2_it60_1448x1072', 'ED060KC1', '', '', '', '', ''], 
	['G', 'GxEPD2_it78_1872x1404', 'ED078KC2', '', '', '', '', ''], 
	['G', 'GxEPD2_it103_1872x1404', 'ES103TC1', '', '', '', '', '']
]

# LIST OF TESTED PROCESSORS (BOARDS) AND NORMAL SETTINGS
# 0 - Class
# 1 - recommended buffer size
# 2 - PIN_CS
# 3 - PIN_DC
# 4 - PIN_RST
# 5 - PIN_BUSY
# 6 - PIN_DIN (MOSI)
# 7 - PIN_CLK
processors = [
	["__AVR (MISC)", "800", "SS", "8", "9", "7", "", ""], 
	["ARDUINO_ARCH_RP2040", "131072", "3", "2", "1", "0", "", ""], 
	["ARDUINO_ARCH_SAM", "32768", "SS", "8", "9", "7", "", ""], 
	["ARDUINO_ARCH_SAMD", "15000", "4", "7", "6", "5", "", ""], 
	["ARDUINO_ARCH_STM32", "15000", "SS", "PA3", "PA2", "PA1", "", ""], 
	["ARDUINO_AVR_MEGA2560", "5000", "SS", "8", "9", "7", "", ""], 
	["ESP32", "65536", "SS", "17", "16", "4", "23", "18"], 
	["ESP8266", "5000", "", "", "", "", "", ""], 
]

#  VARIABLE NUMBERS FOR STATEMENTS TO BE BUILT BASED UPON USER INPUT
#  0 - Color Depth Indicator
#  1 - Driver
#  2 - ePaper Model Number
#  3 - Width
#  4 - Height
#  5 - Driver Chip
#  6 - Description
#  7 - ESP8266 buffer space allocation padding
#  8 - Display Buffer, all other arcitecture
#  9 - CS pin
# 10 - DC pin
# 11 - RST pin
# 12 - BUSY pin
# 13 - DIN (MOSI)
# 14 - CLK
predriverstmts = [
	["/*             GxEPD ePAPER DISPLAY INITIALIZATION CODE             */"], 
	["/*           SIMPLIFIES SELECTION OF PROPER CONFIGURATION           */"], 
	["/*              github.com/ChameleonGeek/GxPED2_Helper              */"], 
	["\n// PROCCESSOR TYPE SELECTED: {0}", 15], 
	["// EPAPER DISPLAY SPECS: Colors: {3} / {0}x{1} pixels / Model: {2}", 16, 3, 4, 2], 
	["// EPAPER DISPLAY SPECS: GxEPD Driver: {0} / Chipset: {1}", 1, 5], 
	["// EPAPER DISPLAY SPECS: Description: {0}", 6], 
	["\n// INCLUDE LIBRARIES FOR THE EPAPER DISPLAY"], 
	["#include <GxEPD2_{0}.h>", 0], 
	["/* ################################################# */"], 
	["/*                ADD OR DELETE FONTS                */"], 
	["/*                LIST IS AVAILABLE AT               */"], 
	["/*  ...Arduino/libraries/Adafruit_GFX_Library/Fonts  */"], 
	["/* ################################################# */"], 
	["#include <Fonts/FreeMonoBold9pt7b.h>"], 
	["#include <Fonts/FreeMonoBold12pt7b.h>"], 
	["#include <Fonts/FreeMonoBold18pt7b.h>"], 
	["\n// DECLARE PINS TO BE USED BY EPAPER DISPLAY"], 
	["#define PIN_CS   {0}", 9], 
	["#define PIN_DS   {0}", 10], 
	["#define PIN_RST  {0}", 11], 
	["#define PIN_BUSY {0}", 12], 
	["#define PIN_DIN  {0} // (MOSI) USING STANDARD SPI PINS - REFERENCE ONLY", 13], 
	["#define PIN_CLK  {0} // USING STANDARD SPI PINS - REFERENCE ONLY", 14], 
	["\n// DECLARE THE DISPLAY CLASS AND ASSOCIATED VALUES"], 
	["#define GxEPD2_DISPLAY_CLASS GxEPD2_{0}", 0], 
	["#define GxEPD2_{0}_IS_GxEPD2_{1} true", 0, 0], 
	["#define IS_GxEPD(c, x) (c##x)"],
	["#define IS_GxEPD2_{0}(x) IS_GxEPD(GxEPD2_{1}_IS_, x)", 0, 0], 
	["#define GxEPD2_{0}_IS_GxEPD2_{1} true", 0, 0], 
	["#define IS_GxEPD2_{0}(x) IS_GxEPD(GxEPD2_{1}_IS_, x)", 0, 0], 
	["\n// DECLARE THE DISPLAY DRIVER CLASS"], 
	["#define GxEPD2_DRIVER_CLASS {0} // {1}  {2}x{3}, {4}, {5}",	1, 2, 3, 4, 5, 6], 
]

simplebuff = ["\n#define MAX_DISPLAY_BUFFER_SIZE {0}ul", 8]
maxbuffstmts = [
	["ESP8266", ["\n#define MAX_DISPLAY_BUFFER_SIZE (81920ul-34000ul-{0}ul)", 7]],
	["ESP32", simplebuff],
	["ARDUINO_ARCH_STM32", simplebuff], 
	["__AVR", simplebuff], 
	["ARDUINO_ARCH_SAM", simplebuff], 
	["ARDUINO_ARCH_SAMD", simplebuff], 
	["ARDUINO_ARCH_RP2040", simplebuff], 
]

maxheightstmts = [
	["2", "#define MAX_HEIGHT(EPD) (EPD::HEIGHT <= MAX_DISPLAY_BUFFER_SIZE / (EPD::WIDTH / 8) ? EPD::HEIGHT : MAX_DISPLAY_BUFFER_SIZE / (EPD::WIDTH / 8))"],
	["3", "#define MAX_HEIGHT(EPD) (EPD::HEIGHT <= (MAX_DISPLAY_BUFFER_SIZE / 2) / (EPD::WIDTH / 8) ? EPD::HEIGHT : (MAX_DISPLAY_BUFFER_SIZE / 2) / (EPD::WIDTH / 8))"], 
	["4", "#define MAX_HEIGHT(EPD) (EPD::HEIGHT <= (MAX_DISPLAY_BUFFER_SIZE / 2) / (EPD::WIDTH / 8) ? EPD::HEIGHT : (MAX_DISPLAY_BUFFER_SIZE / 2) / (EPD::WIDTH / 8))"], 
	["7", "#define MAX_HEIGHT(EPD) (EPD::HEIGHT <= (MAX_DISPLAY_BUFFER_SIZE) / (EPD::WIDTH / 2) ? EPD::HEIGHT : (MAX_DISPLAY_BUFFER_SIZE) / (EPD::WIDTH / 2))"], 
]

finalspec = ["\n// DECLARE THE DISPLAY CLASS", 
	"GxEPD2_DISPLAY_CLASS<GxEPD2_DRIVER_CLASS, MAX_HEIGHT(GxEPD2_DRIVER_CLASS)> display(GxEPD2_DRIVER_CLASS(PIN_CS, PIN_DC, PIN_RST, PIN_BUSY));",
	"\n// CLEANUP UNNEEDED DEFINITIONS", 
	"#undef MAX_DISPLAY_BUFFER_SIZE", 
	"#undef MAX_HEIGHT", 
	"/*                      END OF CODE CREATED BY                      */",
	"/*             GxEPD ePAPER DISPLAY INITIALIZATION CODE             */",
]

def outputToDoc(stmt):
	global outputfile
	print(stmt)
	outputfile.write(stmt + "\n")

def stmt0():
	if colordepth == "2":
		return "BW"
	if colordepth == "3":
		return "3C"
	if colordepth == "4":
		return "4C"
	if colordepth == "7":
		return "7C"
	return "<error>"

def stmtvalue(index):
	global colordepth 
	global driver 
	global modelnum 
	global width 
	global height
	global chipset
	global descr
	global bufferpad
	global bufferspace
	retval = ""
	if index == 0:
		retval = stmt0()
	elif index == 1:
		retval = driver
	elif index == 2:
		retval = modelnum
	elif index == 3:
		retval = width
	elif index == 4:
		retval = height
	elif index == 5:
		retval = chipset
	elif index == 6:
		retval = descr
	elif index == 7:
		retval = bufferpad
	elif index == 8:
		retval = bufferspace
	elif index == 9:
		retval = pincs
	elif index == 10:
		retval = pindc
	elif index == 11:
		retval = pinrst
	elif index == 12:
		retval = pinbusy
	elif index == 13:
		retval = pindin
	elif index == 14:
		retval = pinclk
	elif index == 15:
		retval = proctype
	elif index == 16:
		retval = colordepth
	return retval

def loadDispVars(index):
	global colordepth
	global driver
	global modelnum
	global width
	global height
	global chipset
	global descr
	colordepth = displays[index][0]
	driver = displays[index][1]
	modelnum = displays[index][2]
	width = displays[index][3]
	height = displays[index][4]
	chipset = displays[index][5]
	descr = displays[index][6]

def loadProcDefaults(index):
	global bufferspace
	global proctype
	global pincs
	global pindc
	global pinrst
	global pinbusy
	global pindin
	global pinclk
	global processors
	procspec = processors[index]
	bufferspace = procspec[1]
	proctype = procspec[0]
	pincs = procspec[2]
	pindc = procspec[3]
	pinrst = procspec[4]
	pinbusy = procspec[5]
	pindin = procspec[6]
	pinclk = procspec[7]

def rebuildCommand(cmdarray):
	stmt = cmdarray[0]
	optcount = len(cmdarray)
	if optcount == 1:
		return stmt
	elif optcount == 2:
		stmt = stmt.format(stmtvalue(cmdarray[1]))
	elif optcount == 3:
		stmt = stmt.format(stmtvalue(cmdarray[1]), stmtvalue(cmdarray[2]))
	elif optcount == 4:
		stmt = stmt.format(stmtvalue(cmdarray[1]), stmtvalue(cmdarray[2]), stmtvalue(cmdarray[3]))
	elif optcount == 5:
		stmt = stmt.format(stmtvalue(cmdarray[1]), stmtvalue(cmdarray[2]), stmtvalue(cmdarray[3]), 
			stmtvalue(cmdarray[4]))
	elif optcount == 6:
		stmt = stmt.format(stmtvalue(cmdarray[1]), stmtvalue(cmdarray[2]), stmtvalue(cmdarray[3]), 
			stmtvalue(cmdarray[4]), stmtvalue(cmdarray[5]))
	elif optcount == 7:
		stmt = stmt.format(stmtvalue(cmdarray[1]), stmtvalue(cmdarray[2]), stmtvalue(cmdarray[3]), 
			stmtvalue(cmdarray[4]), stmtvalue(cmdarray[5]), stmtvalue(cmdarray[6]))
	return stmt

def getIndexFromArray(array, seek, seekfld):
	for i in range(0, len(array)):
		if array[i][seekfld] == seek:
			return i
	return 999

def writeMaxBuffer():
	global maxbuffstmts
	global proctype
	bufnum = getIndexFromArray(maxbuffstmts, proctype, 0)
	outputToDoc(rebuildCommand(maxbuffstmts[bufnum][1]))

def writeMaxHeight():
	global maxheightstmts
	global colordepth
	stmtnum = getIndexFromArray(maxheightstmts, colordepth, 0)
	outputToDoc(maxheightstmts[stmtnum][1])

###################################################################################################
###################################################################################################
#                                    USER INTERACTION FUNCTIONS
###################################################################################################
###################################################################################################
def loadBasicOptsFromList(optlist, fldnum, sort = True):
	retval = []
	for opt in optlist:
		retval.append(opt[fldnum])
	if sort == True:
		retval.sort()
	return retval

def queryFromList(pretext, prompt, optlist, oneline = False):
	print("\n" * 40)
	print(pretext)
	if oneline == False:
		num = []
		for i in range(0, len(optlist)):
			print(str(i + 1) + " - " + optlist[i])
			num.append(str(i))
		retval = input(prompt)
		if retval not in num:
			queryFromList(pretext, prompt, optlist, oneline)
		else:
			return retval
	else:
		print(optlist)
		retval = input(prompt)
		if retval not in optlist:
			queryFromList(pretext, prompt, optlist, oneline)
		else:
			return retval

def queryRawInput(prompttext, default):
	print("\n" * 40)
	retval = input(prompttext.format(default))
	if retval == "":
		retval = default
	confirm = input("You entered {0}.  Is this correct? (Y|n) ".format(retval))
	if confirm == "y" or confirm == "Y" or confirm == "":
		return retval
	else:
		queryRawInput(prompttext, default)

def QueryProcessor():
	global bufferspace
	global pinbusy
	global pinclk
	global pincs
	global pindc
	global pindin
	global pinrst
	global processors
	global procindex
	global proctype
	proclist = loadBasicOptsFromList(processors, 0, False)
	procnum = queryFromList("Please select which processor (board) will be used", "Please select from this list: ", proclist, False)
	procindex = int(procnum) - 1
	loadProcDefaults(procindex)
	bufferspace = queryRawInput("Please input the number of bytes to be used as display buffer ({0}):  ", bufferspace)
	pincs = queryRawInput("Please enter the pin number for Chip Select (CS) ({0})", pincs)
	pindc = queryRawInput("Please enter the pin number for DC ({0})", pindc)
	pinrst = queryRawInput("Please enter the pin number for Reset ({0})", pinrst)
	pinbusy = queryRawInput("Please enter the pin number for Busy ({0})", pinbusy)
	pinclk = queryRawInput("Please enter the pin number for SPI Clock ({0})", pinclk)
	pindin = queryRawInput("Please enter the pin number for SPI MOSI (DIN) ({0})", pindin)

def convertListtype(optlist, tostring = True):
	if tostring == True:
		for i in range(0, len(optlist)):
			optlist[i] = str(optlist[i])
	else:
		for i in range(0, len(optlist)):
			optlist[i] = int(optlist[i])
	return optlist

def QueryDisplayWidth():
	global colordepth
	global width
	opts = []
	for display in displays:
		if display[0] == colordepth and int(display[3]) not in opts:
			opts.append(int(display[3]))
	opts.sort()
	opts = convertListtype(opts)
	width = queryFromList("Display width in pixels", "Please enter from the list above: ", opts, True)

def QueryDisplayHeight():
	global colordepth
	global width
	global height
	opts = []
	for display in displays:
		if display[0] == colordepth and display[3] == width and int(display[4]) not in opts:
			opts.append(int(display[4]))
	if len(opts) == 1:
		height = opts[0]
		return 0
	opts.sort()
	opts = convertListtype(opts)
	height = queryFromList("Display height in pixels", "Please enter from the list above: ", opts, True)

def QueryDisplayModel():
	global colordepth
	global width
	global driver
	global modelnum
	global height
	global chipset
	print("\n" * 40)
	opts = []
	nums = []
	for i in range(0, len(displays)):
		display = displays[i]
		if display[0] == colordepth and display[3] == width and display[4] == str(height):
			opts.append([display[2], display[6], i])
	opts.sort()
	for index in range(0, len(opts)):
		print(str(index + 1) + " - " + opts[index][0] + "   (" + opts[index][1]  + ")")
		nums.append(str(index + 1) )
	retval = input("Please select the board being used: ")
	if retval not in nums:
		QueryDisplayModel()
	optindex = int(retval) - 1
	loadDispVars(optindex)

def QueryDisplay():
	global colordepth
	global width
	global driver
	global modelnum
	global height
	global chipset
	colors = []
	for display in displays:
		if display[0] not in colors:
			colors.append(display[0])
	colors.sort()
	colordepth = queryFromList("Please select the number of colors the ePaper supports", "Please select from this list: ", colors, True)
	QueryDisplayWidth()
	QueryDisplayHeight()
	QueryDisplayModel()

def Main():
	global outputfile
	QueryProcessor()
	QueryDisplay()
	outputfile = open("ePaper_Baseline.ino", "w")
	for index in range(0, len(predriverstmts)):
		outputToDoc(rebuildCommand(predriverstmts[index]))
	writeMaxBuffer()
	writeMaxHeight()
	for index in range(0, len(finalspec)):
		outputToDoc((finalspec[index]))
	outputfile.close()
	print("\n" * 40)
	print("Initialization code has been created for the configuration")
	print("you have selected.  It is saved as" + os.path.join(os.getcwd(), "ePaper_Baseline.ino"))

Main()
