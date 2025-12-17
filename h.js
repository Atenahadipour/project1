─$ sudo systemctl status tor@default
● tor@default.service - Anonymizing overlay network for TCP
     Loaded: loaded (/usr/lib/systemd/system/tor@default.service; enabled-runtime; preset: disabled)
     Active: active (running) since Wed 2025-12-17 04:38:05 EST; 4min 52s ago
 Invocation: 7688d5f5ccec460abaf78ead348c7a3c
    Process: 3139 ExecStartPre=/usr/bin/install -Z -m 02755 -o debian-tor -g debian-tor -d /run/tor (code=exited, status=0/SU>
    Process: 3143 ExecStartPre=/usr/bin/tor --defaults-torrc /usr/share/tor/tor-service-defaults-torrc -f /etc/tor/torrc --Ru>
   Main PID: 3144 (tor)
      Tasks: 22 (limit: 8937)
     Memory: 49.4M (peak: 52.8M)
        CPU: 241ms
     CGroup: /system.slice/system-tor.slice/tor@default.service
             └─3144 /usr/bin/tor --defaults-torrc /usr/share/tor/tor-service-defaults-torrc -f /etc/tor/torrc --RunAsDaemon 0

Dec 17 04:38:05 kali Tor[3144]: Parsing GEOIP IPv6 file /usr/share/tor/geoip6.
Dec 17 04:38:05 kali Tor[3144]: Bootstrapped 0% (starting): Starting
Dec 17 04:38:05 kali Tor[3144]: Starting with guard context "bridges"
Dec 17 04:38:05 kali Tor[3144]: Delaying directory fetches: No running bridges
Dec 17 04:38:05 kali Tor[3144]: Signaled readiness to systemd
Dec 17 04:38:05 kali systemd[1]: Started tor@default.service - Anonymizing overlay network for TCP.
Dec 17 04:38:06 kali Tor[3144]: Opening Socks listener on /run/tor/socks
Dec 17 04:38:06 kali Tor[3144]: Opened Socks listener connection (ready) on /run/tor/socks
Dec 17 04:38:06 kali Tor[3144]: Opening Control listener on /run/tor/control
Dec 17 04:38:06 kali Tor[3144]: Opened Control listener connection (ready) on /run/tor/control
lines 1-23/23 (END)
