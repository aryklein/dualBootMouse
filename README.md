dualBootMouse
=============

This Python script deals with the configuration of a Bluetooth mouse/keyboard on a dual boot system
(Windows 10 and Linux), to avoid re-pairing the device everytime you boot different OS. It follows
the steps described in many sites like this:

https://desktopi18n.wordpress.com/2018/02/02/bluetooth-mouse-in-dual-boot-of-windows-10-and-linux/

Why does this happen?
---------------------

Basically, when you pair your device, your Bluetooth service generates a unique set of pairing keys.
First, your computer stores the Bluetooth device's mac address and pairing key. Second, your Bluetooth
device stores your computer's mac address and the matching key. The mac address for your Bluetooth port
will be the same on both Linux and Windows (it is set on the hardware level). However, when you re-pair
the device in Windows or Linux, it generates a new key. That key overwrites the previously stored key on
the Bluetooth device. Windows overwrites the Linux key and vice versa.
