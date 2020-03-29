dualBootMouse
=============

Every time I boot a different OS, I have to pair my bluetooth mouse again. This is quite annoying, so I coded
a simple Python script that configures the Bluetooth mouse on my dual boot system (Windows 10 and Linux).
This avoid to re-pairing the device everytime I boot a different OS.

Why does it happen?
-------------------

Basically when you pair your mouse, your Bluetooth service generates a unique set of pairing keys.
First, your computer stores the Bluetooth device's mac address and pairing key. Second, your Bluetooth
mouse stores your computer's mac address and the matching key. The mac address for your Bluetooth port
will be the same on both operative systems (Linux and Windows) because it is set on the hardware level).
However, when you re-pair the device in Windows or Linux, it generates a new key. That key overwrites the
previously stored key on the Bluetooth device. Windows overwrites the Linux key and vice versa.

Info taken from [here](https://unix.stackexchange.com/questions/255509/bluetooth-pairing-on-dual-boot-of-windows-linux-mint-ubuntu-stop-having-to-p)

How to use this Python script
-----------------------------

1) Pair the bluetooth mouse in Linux. That creates a new file ``/var/lib/bluetooth/XX:XX:XX:XX:XX:XX/YY:YY:YY:YY:YY:YY/info``
(``XX:XX:XX:XX:XX:XX`` is the Bluetooth adapter MAC address and ``YY:YY:YY:YY:YY:YY`` is the mouse MAC address)
2) Reboot your computer and pair the device in Windows. This step breaks the bluetooth pairing done in Linux.
3) Get the pairing keys in Windows using ``PsExec``. Download it from [here](https://docs.microsoft.com/en-us/sysinternals/downloads/psexec)
4) Open Windows command line prompt (``cmd``) with Administrator permission and execute:

::

    psexec64.exe -s -i regedit /e C:\BTKeys.reg HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\BTHPORT\Parameters\Keys

5) The file will be saved to ``C:\BTKeys.reg``. You can use a different path.
6) Export this file (``BTKeys.reg``) to Linux.
7) In Linux, execute script with root permissions:

::

    $ sudo ./dualBootMouse -w /some/path/BTKeys.reg -l /var/lib/bluetooth/XX:XX:XX:XX:XX:XX/YY:YY:YY:YY:YY:YY/info -m YY:YY:YY:YY:YY:YY

8) The script will change the Linux file with the Windows keys. Restart bluetooth service or reboot the system.

::

    sudo systemctl restart bluetooth.service

