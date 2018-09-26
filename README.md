dualBootMouse
=============

Every time I boot a different OS, I have to pair again my bluetooth mouse. This is quite annoying, so I coded
a simple Python script that configures the Bluetooth mouse/keyboard on my dual boot system (Windows 10 and Linux),
This avoid to re-pairing the device everytime I boot different OS. Basically it follows the steps described in
many sites like this:

https://desktopi18n.wordpress.com/2018/02/02/bluetooth-mouse-in-dual-boot-of-windows-10-and-linux/

Why does this happen?
---------------------

Basically when you pair your mouse, your Bluetooth service generates a unique set of pairing keys.
First, your computer stores the Bluetooth device's mac address and pairing key. Second, your Bluetooth
mouse stores your computer's mac address and the matching key. The mac address for your Bluetooth port
will be the same on both Linux and Windows (it is set on the hardware level). However, when you re-pair
the device in Windows or Linux, it generates a new key. That key overwrites the previously stored key on
the Bluetooth device. Windows overwrites the Linux key and vice versa.

Info taken from [here](https://unix.stackexchange.com/questions/255509/bluetooth-pairing-on-dual-boot-of-windows-linux-mint-ubuntu-stop-having-to-p)

How to use this Python script
-----------------------------

1) Pair the bluetooth device in Linux. This will create a new directory like this ``/var/lib/bluetooth/xx:xx:xx:xx:xx:xx``
2) Reboot your computer and pair the device in Windows. It will screw up the pairing in Linux.
3) Get the pairing keys in Windows. Download psexec.exe from [here](https://docs.microsoft.com/en-us/sysinternals/downloads/psexec)
4) Open a command line prompt with Administrator rights and run:

```
> cd Downloads
> psexec.exe -s -i regedit /e C:\BTKeys.reg HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\BTHPORT\Parameters\Keys
```

5) The keys should be now exported to ```C:\BTKeys.reg``` (this is not a simple text file)
6) Boot Linux, open the file ```BTKeys.reg``` and copy the content to a new text file. For example ```BTKeys.txt```
7) With ```root``` privileges, run the Python script:

```
$ sudo ./dualBootMouse -w BTKeys.txt -l /var/lib/bluetooth/xx:xx:xx:xx:xx:xx/xx:xx:xx:xx:xx:xx/info
```

8) The script will change the file with the same Windows keys. Reboot and it will work.

