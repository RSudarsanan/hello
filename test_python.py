import os



command = nmcli -t -f active,ssid dev wifi | egrep '^yes' | cut -d\' -f2
