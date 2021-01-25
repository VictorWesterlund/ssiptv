#!/usr/bin/python3

import sys
import dbus

bus = dbus.SystemBus()

manager = dbus.Interface(bus.get_object('org.ofono', '/'),'org.ofono.Manager')

modems = manager.GetModems()
modem = modems[0][0]

if (len(sys.argv) == 2):
	modem = sys.argv[1]

manager = dbus.Interface(bus.get_object('org.ofono', modem),'org.ofono.VoiceCallManager')

manager.HangupAll()