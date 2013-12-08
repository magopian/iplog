IP Log
######

Small Flask website that displays the current IP address.

This IP address can be stored if the ``store`` parameter is present in the url.

An optional ``note`` parameter can also be provided, whic could be used to
store the local IP address.


Usage
=====

Help out a friend
-----------------

Need to connect to a remote desktop to help a friend? Just provide him the link
to your IP log install, and ask him to click on the "store" link and provide a
small note for you to quickly find which IP it is.


Where's my Raspberry-pi?
------------------------

By default, the Raspbian image has the network configured to grab an IP address
using the DHCP. This means that when you start your RPi, it could have just any
IP address.

To know which IP address it has, it could use the IP Log site to specify its
local IP address (using the ``note`` parameter).

Here's how to do it in your shell::

    curl "http://some.site.com/?store=true&note=`ifconfig|xargs|awk '{print $7}'|sed -e 's/[a-z]*:/''/'`"

There's a simpler solution that seems to work well on a Raspberry-pi::

    curl "http://some.site.com/?store=true&note=`hostname -I`"

Add one of those two lines to the ``/etc/rc.local`` script, that is launched on
each boot.

For more information and other tips regarding the Raspberry-Pi, check
https://gist.github.com/magopian/7854957.
