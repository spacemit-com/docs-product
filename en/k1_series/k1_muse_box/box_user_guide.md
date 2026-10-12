---
sidebar_position: 2
---

# K1 MUSE Box User Guide

## Product Overview

**K1 MUSE Box** is a RISC-V mini PC designed for developers. It uses a standard Mini-ITX motherboard with rich expansion interfaces and headers, a fanless design, and is powered by the SpacemiT M1 chip. The M1 is the high-performance variant of the SpacemiT K1. It integrates eight SpacemiT RISC-V X60 cores, delivering 50 KDMIPS compute performance and 2 TOPS AI processing power, enabling rapid integration with all mainstream AI ecosystems. It supports 4K H.265/H.264/VP9/VP8 codec formats, a 3D graphics engine, OpenCL 3.0, OpenGL ES 3.2, and Vulkan 1.3.
![](./static/box.PNG)

**Block diagram**:
![](./static/box_block.JPEG)

## Specifications

**Processor**
SpacemiT M1, 8-core 64-bit RISC-V, 50 KDMIPS CPU performance with 2 TOPS AI processing power

**Display**
HDMI output, up to 1080P@60Hz

**Memory**
LPDDR4X, 2666 MT/s, 16 GB

**Local Storage**
eMMC 5.1, 32 GB

**Expansion Storage**
- M.2 2280 M-Key connector, supports NVMe SSD up to 1 TB
- SATA port, supports one SATA hard drive

**Wireless**
NGFF M.2 E-Key dual-antenna wireless card, RTL8852BE chipset, supports Wi-Fi 6 & BT 5.2

**Rear Panel**
2.5/5.5 DC IN x1, HDMI x1, USB 2.0 Type-A x2 (lower port is OTG), USB 3.0 Type-A x2, RJ45 (1000M) x2, 3.5mm Line in x1 & Line out x1, RS232 COM x2

**Front Panel**
USB 2.0 Type-A x2, 3.5mm Line in x1 & Line out x1

**Audio Header**
1 x 9-pin header, 2x5-1, 2.54mm pitch

**USB Headers**
2 x USB 2.0 headers (4 x USB 2.0 signals total), 2 x USB 3.0 headers

**COM Headers**
2 x 9-pin headers, 2x5-1, 2.54mm pitch, RS232

**Power Button & LED Header**
1 x 9-pin header, 2x5-1, 2.54mm pitch

**Dimensions**
Chassis: 185 x 45 x 197 mm; Motherboard: 170 x 170 mm, Mini-ITX

**Material**
Full metal

**Weight**
932 g

**OS**
Bianbu OS, Ubuntu, Linux

**Browser**
Chromium

**Power Input**
12V, 2.5/5.5 DC jack; motherboard also supports 4-pin ATX DC IN

**Interface diagram**:
![](./static/box_port1.JPEG)
![](./static/box_port2.png)

## Hardware Advantages

**Fanless design, efficient thermal dissipation**:
The heatsink paired with the SpacemiT M1 RISC-V processor sustains full CPU performance without a fan, creating a quiet environment for development, work, and entertainment.

**Compact yet rugged**:
- 1.6 L compact volume with VESA monitor-mount support, freeing up desk space
- Total weight only 0.93 kg
- Full-metal chassis with strong corrosion and impact resistance

**High-speed memory and large storage**:
- LPDDR4X-2666 MHz high-speed memory, up to 16 GB, for faster local software execution
- Up to 1 TB PCIe SSD, plus optional SATA hard drive expansion

**Full HD output**:
- Full HD display output for sharper visuals and better productivity
  - 1 x HDMI (up to 1920x1080@60Hz)

**Wireless connectivity**:
- Built-in M.2 2230 Key-E wireless module with PCIe dual-band Wi-Fi 6 and Bluetooth 5.2 for fast, stable long-range wireless

**Interfaces**:
- Dual RS232 COM ports (DB9)
- Multiple high-speed USB ports for peripherals
- Dual Gigabit Ethernet

## Initial Setup

### Before You Begin

MUSE Box is a standalone mini PC. You need to connect the required peripherals before using it.

#### Power Adapter

MUSE Box is powered via the 12V DC IN port. Use the power adapter included in the package and connect it to the DC IN port.
![](./static/dcin.jpg)

#### Keyboard & Mouse

Connect a wired keyboard and mouse (or a USB receiver) to any USB port on the MUSE Box, or pair a Bluetooth keyboard and mouse wirelessly.
![](./static/keyboard_mouse.jpg)

#### Display

MUSE Box requires an external monitor. It supports HDMI video output, so connect any HDMI monitor.
![](./static/box_display.PNG)

#### Audio

MUSE Box can output audio over HDMI to the connected monitor. You can also connect audio peripherals to the 3.5mm audio jacks on the front or rear panel. Switch between the audio jack sound card (ES8326) and the HDMI sound card in your system sound settings.
![](./static/box_audio.PNG)

#### Network

MUSE Box supports wired RJ45 Ethernet — connect a network cable to either RJ45 port. For wireless, remove the two antennas from the package and install them on the antenna connectors before use.
![](./static/box_wirelss.PNG)

## Powering On

Connect all required peripherals before powering on:
Connect the device to an HDMI monitor with a video cable, then connect a keyboard and mouse. Finally, plug in the power cable — the system powers on automatically the first time. After a software shutdown, press the power button (to the left of the blue LED) for 1 second to power on again. The blue power LED lights up when the system is running.
![](./static/box_display.PNG)

## First-Boot Setup

Your MUSE Box comes pre-installed with the SpacemiT Bianbu Desktop OS and runs a setup wizard on first boot. You will need a monitor, keyboard, and mouse to complete the wizard.

**System Language**:
Choose the system language. English and Chinese are shown by default; click the three dots at the bottom for more options.
![](./static/lang.png)

**Input Method**:
Configure your keyboard layout and input method.
![](./static/keyinput.png)

**Wi-Fi**:
Connect to a Wi-Fi network by selecting it from the list. If no suitable network is available, click Skip in the upper-left corner.
![](./static/wifi.png)

**Location Services**:
Choose whether to enable location services. Enabling this improves convenience but may expose location data.
![](./static/location.png)

**Time Zone**:
Set your time zone. When connected to the internet, the system syncs the time automatically. Search for a city to set the time zone.
![](./static/time.png)

**Username and Password**:
Set your username and password. Remember your password.
![](./static/setuser01.png)

![](./static/setuser02.png)

**Setup Complete**
Click "Start Using Bianbu" to enter the desktop.
![](./static/done.png)

## Flashing Firmware

### Entering Flash Mode

Rotate and release the two screws on the back of the chassis, then slide the top cover off to access the motherboard.
![](./static/box_back.png)
Hold the Fastboot (flash) button on the motherboard, then press and hold the Reset button to reboot into flash mode. Connect the MUSE Box to your host computer via USB using the OTG port (the lower USB 2.0 Type-A port on the rear panel). Flash using the SpacemiT official flashing tool Titan or the `fastboot` command.
Note: use a USB data cable, not a charge-only cable.
![](./static/box_otg.jpg)

### Firmware Download and Installation

**Bianbu**

**About Bianbu**:
Bianbu is an operating system deeply optimized by SpacemiT for RISC-V processors. MUSE Box ships with Bianbu Desktop pre-installed.

**Bianbu website**:
[https://bianbu.spacemit.com/](https://bianbu.spacemit.com/)

**Bianbu Desktop firmware download**:
[https://archive.spacemit.com/image/k1/version/bianbu/](https://archive.spacemit.com/image/k1/version/bianbu/)

**Bianbu Desktop installation and upgrade guide**:
[https://bianbu.spacemit.com/user_guide/](https://bianbu.spacemit.com/user_guide/)
