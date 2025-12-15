sidebar_position: 9

# FAQ

## System & Usage

### Q1: What should I do if I encounter application errors or mouse lag after the first boot?

**A**:
After the initial boot setup, some system configurations may not be fully applied yet. We recommend **restarting the device once**. The system should function normally after the reboot.

### Q2: How do I reset my password if I forget it?

**A**:

1. Connect the MUSE Book to a host computer (e.g., PC) using a serial cable.
2. Open a serial communication software on the host computer and log in with the administrator account:
    - Username: `root`
    - Password: `bianbu`
3. After logging in, execute one of the following commands based on your needs:
    - If you want to **keep the user's data**:

        ```bash
        userdel username
        ```

    - If you do **not** want to keep the user's data:

        ```bash
        userdel -r username
        ```

    *(Replace `username` with the actual username of the account whose password you forgot.)*
4. Restart the device. You will be able to enter the setup interface again to create a new username and password.

## System Support

### Q3: Which operating systems are supported by MUSE series products?

**A**:
The following operating systems are currently adapted:

- Bianbu Desktop (Pre-installed)
- Bian Linux
- Deepin
- OpenKylin
- OpenHarmony

Adaptation for more operating systems is ongoing. Please follow the official announcements from SpacemiT for the latest updates.

### Q4: Do MUSE series products support the Windows operating system?

**A**:
Windows is currently **not supported**. The MUSE Book comes pre-installed with **Bianbu Desktop**, a deeply optimized Ubuntu-based distribution. It includes essential software like LibreOffice, a web browser, and media viewers for an out-of-the-box experience. Users can also install additional applications through the Bianbu software repository.

## Firmware & Drivers

### Q5: Can I flash the firmware on MUSE series products myself?

**A**:
Yes. Users can flash the firmware using command-line tools or the Titan Tool. Please refer to the corresponding product's **User Guide** for detailed instructions.

### Q6: Where can I download the serial cable driver for MUSE Pi?

**A**:
Driver download link:
[https://www.ftdichip.cn/Drivers/D2XX.htm](https://www.ftdichip.cn/Drivers/D2XX.htm)