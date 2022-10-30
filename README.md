# notify-read.sh
For GNOME based desktops, a python utility to read previous notifications via dbus, pair with notify-send

## Install
`$ ./install.sh`

## Usage
- Install enables a desktop file addition to the startup applications that will run a notifications monitor on startup.
- Desktop notifications send by applications and notify-send are logged by timestamp to ~/.cache/notifications.txt

### Spotify App or Spotify-QT
Find your listening history by running
`$ grep -i "spotify" ~/.cache/notifications.log`

### WiFi Connections
Lookup network connects and disconnects
`$ grep -i "networkmanager" ~/.cache/notifications.log`
