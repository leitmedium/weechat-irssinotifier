# Author: Caspar Clemens Mierau <ccm@screenage.de>
# Derived from: notifo
#   Author: ochameau <poirot.alex AT gmail DOT com>
#   Homepage: https://github.com/ochameau/weechat-notifo
# An from: notify
#   Author: lavaramano <lavaramano AT gmail DOT com>
#   Improved by: BaSh - <bash.lnx AT gmail DOT com>
#   Ported to Weechat 0.3.0 by: Sharn - <sharntehnub AT gmail DOT com)
# And from: notifo_notify
#   Author: SAEKI Yoshiyasu <laclef_yoshiyasu@yahoo.co.jp>
#   Homepage: http://bitbucket.org/laclefyoshi/weechat/
#
# This plugin brings IrssiNotifier to your Weechat. Setup and install
# IrssiNotifier first: https://irssinotifier.appspot.com
#
# Requires Weechat 0.3.0, curl, openssl
# Released under GNU GPL v2
#
# 2012-10-26, au <poirot.alex@gmail.com>:
#     version 0.1: merge notify.py and notifo_notify.py in order to avoid
#                  sending notifications when channel or private buffer is
#                  already opened

import weechat, string, os, urllib, subprocess, shlex

weechat.register("irssinotifier", "Caspar Clemens Mierau <ccm@screenage.de>", "0.1", "GPL", "irssinotifier: Send push notifications to you iPhone/Android about your private message and highligts.", "", "")

settings = {
    "api_token": "",
    "encryption_password": ""
}

for option, default_value in settings.items():
    if weechat.config_get_plugin(option) == "":
        weechat.prnt("", weechat.prefix("error") + "irssinotifier: Please set option: %s" % option)
        weechat.prnt("", "irssinotifier: /set plugins.var.python.irssinotifier.%s STRING" % option)

# Hook privmsg/hilights
weechat.hook_print("", "irc_privmsg", "", 1, "notify_show", "")

# Functions
def notify_show(data, bufferp, uber_empty, tagsn, isdisplayed,
        ishilight, prefix, message):

    if weechat.buffer_get_string(bufferp, "localvar_type") == "private":
        show_notification(prefix, message)

    elif ishilight == "1":
        buffer = (weechat.buffer_get_string(bufferp, "short_name") or
                weechat.buffer_get_string(bufferp, "name"))
        show_notification(buffer, prefix + ": " + message)

    return weechat.WEECHAT_RC_OK

def encrypt(text):
    encryption_password = weechat.config_get_plugin("encryption_password")
    openssl = "openssl enc -aes-128-cbc -salt -base64 -A -pass pass:" + encryption_password 
    openssl = shlex.split(openssl)
    echo = "echo " + text
    echo = shlex.split(echo)
    p1 = subprocess.Popen(echo, stdout=subprocess.PIPE) 
    p2 = subprocess.Popen(openssl, stdin=p1.stdout, stdout=subprocess.PIPE) 
    p1.stdout.close()
    output = p2.communicate()[0]
    output = string.replace(output,"/","_")
    output = string.replace(output,"+","-")
    output = string.replace(output,"=","")
    return output

def show_notification(chan, message):
    API_TOKEN = weechat.config_get_plugin("api_token")
    if API_TOKEN != "":
        url = "https://irssinotifier.appspot.com/API/Message"
        os.system("curl -s -d apiToken=" + API_TOKEN + " -d nick=" + encrypt(chan) + " -d channel=" + encrypt(chan) + " -d message=" + encrypt(message) + " -d version=12 " + url)

# vim: autoindent expandtab smarttab shiftwidth=4
