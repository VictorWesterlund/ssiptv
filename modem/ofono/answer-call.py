#!/usr/bin/python3

import dbus

bus = dbus.SystemBus()

manager = dbus.Interface(bus.get_object('org.ofono', '/'),'org.ofono.Manager')
modems = manager.GetModems()

for path, properties in modems:
	print("[ %s ]" % (path))

	if "org.ofono.VoiceCallManager" not in properties["Interfaces"]:
		continue

	mgr = dbus.Interface(bus.get_object('org.ofono', path),'org.ofono.VoiceCallManager')

	calls = mgr.GetCalls()

	for path, properties in calls:
		state = properties["State"]
		print("[ %s ] %s" % (path, state))

		if state != "incoming":
			continue

		call = dbus.Interface(bus.get_object('org.ofono', path),'org.ofono.VoiceCall')

		call.Answer()