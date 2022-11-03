#!/usr/bin/env python3
import array, os, time, json

import gi.repository.GLib
import dbus
from dbus.mainloop.glib import DBusGMainLoop
    


def init_log():
    file_checks = os.path.expanduser('~') + "/.cache/notifications.log"
    file_exists = os.path.exists(file_checks)
    if not file_exists:
        os.system("touch " + file_checks)        
        
def notifications(bus, message):
    
    c = 0; msg = []
    for arg in message.get_args_list(): 
        if "dbus" not in str(arg) and str(arg) != "0" and str(arg) != "-1" and str(arg) != "" and int(len(str(arg))) > 6 :
            msg.append(str(arg))
            c+=1
            
    dat = str(int(time.time()))
    if len(msg) == 4:
        #DEALS WITH ICONS AND IMAGES
        out = dat + "::" + msg[0].lower() + "::" + msg[2] + "::" + msg[3]
        data_new = {"timestamp":dat,
                    "application":msg[0].lower(),
                    "title": msg[2],
                    "description":msg[3]}
        
    elif len(msg) == 3:
        out = dat + "::" + msg[0].lower() + "::" + msg[1] + "::" + msg[2]
        data_new = {"timestamp":dat,
                    "application":msg[0].lower(),
                    "title": msg[1],
                    "description":msg[2]}
        
    elif len(msg) == 2:
        out = dat + "::" + msg[0].lower() + "::" + msg[1]
        data_new = {"timestamp":dat,
                    "application":msg[0].lower(),
                    "title": msg[1],
                    "description":""}
        
    else:
        out = dat + "::" + msg[0].lower()
        data_new = {"timestamp":dat,
                    "application":"generic",
                    "title": "",
                    "description":""}
        
    
    print(out)
    os.system("echo " + out + " >> " + os.path.expanduser('~') + "/.cache/notifications.log")
    
    filename = str(os.path.expanduser('~') + "/.cache/notifications.json")
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data["notifications"].append(data_new)
        file.seek(0)
        json.dump(file_data, file, indent = 4)

init_log()    





DBusGMainLoop(set_as_default=True)

bus = dbus.SessionBus()
bus.add_match_string_non_blocking("eavesdrop=true, interface='org.freedesktop.Notifications', member='Notify'")
bus.add_message_filter(notifications)

mainloop = gi.repository.GLib.MainLoop()
mainloop.run()