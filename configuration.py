ip = 'xxx.xx.xx.xxx'
port=22
username='xxx'
password='xxx'
rboot = "reboot"
modetest = "modetest -D a898x0000.v_mix -s 41:3840x2160-30@BG24 &"
list_off_cmds= [
    'gst-launch-1.0',
    'gst-discovery-1.0 media/usb/noads.ts',
    'vgst_app',
    ]
