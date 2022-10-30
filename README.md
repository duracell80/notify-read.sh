# notify-read.sh
For GNOME based desktops, a python utility to read previous notifications via dbus, pair with notify-send

## Install
`$ ./install.sh`

## Usage
- Install enables a desktop file addition to the startup applications that will run a notifications monitor on startup.
- Desktop notifications sent by applications and notify-send are logged by timestamp to ~/.cache/notifications.log

### Watch Realtime
`$ watch cat ~/.cache/notifications.log`

### Notify-send
`grep -i "notify-send" ~/.cache/notifications.log`

### Spotify App or Spotify-QT
`$ grep -i "spotify" ~/.cache/notifications.log`

### WiFi Health
`$ grep -i "networkmanager" ~/.cache/notifications.log`
