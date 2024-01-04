#!/usr/bin/bash

################################################################################
# startup.sh                                                                   #
#                                                                              #
# Using systemd like rc.local, due to the deprecated nature of rc.local        #
# by Sophus Christoffer Ott (2sct@agramkow.com)                                #
#                                                                              #
################################################################################

# This program should be placed under /usr/local/bin
# Scripts, programs, etc to run at startup should be placed here
/usr/bin/python3 /home/agramkow/code/py/rflash.server/src/main.py &
/home/agramkow/.dotnet/dotnet /home/agramkow/code/dotnet/PMTester/bin/Release/net6.0/PMTester.dll

