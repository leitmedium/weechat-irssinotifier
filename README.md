weechat-irssinotifier
=====================

Weechat plugin to bring the great IrssiNotifier push notifications with end-to-end encryption to your Weechat client.

## Installation and Configuration

In order to use the plugin you need to take the following steps:

1. Apply for an account at https://irssinotifier.appspot.com
2. Note the "API token" from your profile page: https://irssinotifier.appspot.com/#profile 
3. Install the IrssiNotifier app from the Play store https://play.google.com/store/apps/details?id=fi.iki.murgo.irssinotifier
4. Setup the app by logging in and choosing an encryption password
5. put "irssinotifier.py" to ~/.weechat/python
6. start the plugin with "/python load irssinotifier.py"
7. Set api key and encryption password by doing:
8. /set plugins.var.python.irssinotifier.api_token YOUR_API_TOKEN
9. /set plugins.var.python.irssinotifier.encryption_password YOUR_ENCRYPTION_PASSWORD

You're done. From now on you should receive push notifications to your Android for query messages and channel hilights.

## Todo

1. Make it configurable to notify about current window or not.
2. Make it configurable to notify only while being in away mode.
3. Make it configurable to send more details (e.g. local timestamp).
4. Get rid of curl dependency and use python itself to do the http call (non-blocking).

## Security

This plugin enforces end-to-end encryption. It uses openssl aes-128-cbc for symmetric encryption in the Weechat client and decrypts it on your Android phone. 

## Dependencies

This script needs

* Weechat
* Openssl
* Curl

All of these dependencies should be available from your package manager.

## License

The script is derived from other scripts (see irssinotifier.py for history). It is released under the GPL v2. See LICENSE file for details.

## Author

Author: Caspar Clemens Mierau <ccm@screenage.de>

