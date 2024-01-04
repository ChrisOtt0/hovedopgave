############################################################################################################
#																										   #
#												PATHS													   #
#																										   #
############################################################################################################

PROJECT_ROOT = ../..
SRC_DIR = $(PROJECT_ROOT)/App/Src
LIB_DIR = $(PROJECT_ROOT)/App/Libs
GTEST_INC_DIR = ./include
BUILD_DIR = ./build

APP_MODULES_DIR = $(SRC_DIR)/AppModules

TEST_MODULE_DIR = $(APP_MODULES_DIR)/TestModule_


############################################################################################################
#																										   #
#												INCLUDES												   #
#																										   #
############################################################################################################

# TestModule
INC = -I$(TEST_MODULE_DIR)/Inc

############################################################################################################
#																										   #
#												GTEST													   #
#																										   #
############################################################################################################

# Points to the root of Google Test
GTEST_DIR = $(GTEST_INC_DIR)/googletest/googletest

# All Google Test headers
GTEST_HEADERS = $(GTEST_DIR)/include/gtest/*.h \
				$(GTEST_DIR)/include/gtest/internal/*.h
