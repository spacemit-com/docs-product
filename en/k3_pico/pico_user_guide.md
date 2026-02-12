sidebar_position: 2

# K3 Pico-ITX User Guide

## 1. Product Overview

The K3 Pico-ITX is a single-board computer delivering 60 TOPS of AI compute performance, featuring a unified memory architecture with 8 general-purpose CPU cores and 8 AI cores. The board integrates on-board UFS high-speed storage and a 10-Gigabit optical networking interface, enabling efficient workloads in scientific computing, artificial intelligence, and edge computing scenarios.

The board follows the 2.5-inch Pico-ITX Plus form factor, designed for compact deployments across multiple industries. It provides dual M.2 expansion slots, along with interfaces for real-time motion control and system management. With rich I/O expansion and an industrial-grade architecture, the K3 Pico-ITX enables rapid evaluation, prototyping, and system integration, helping solution providers accelerate product commercialization.

## 2. Hardware Description

### 2.1 Board Overview

![](./static/keys00.png)

> **Note:** The board appearance may vary slightly depending on hardware revision.

### 2.2 LEDs and Buttons

| Indicator | Description                    |
| --------- | ------------------------------ |
| Status LED **STAT**  | Solid green: system powered on |

#### Buttons

| Button                      | Operation Description                                                                                                                  |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **Power (PWR)**             | • Press 1s (from shutdown): power on  <br>• Press 1s (from standby): wake system  <br>• Hold 3s (running): force power off |
| **Reset (RST)**             | Short press: hardware reset / forced reboot                                                                                |
| **FDL (Firmware Download)** | Hold while applying power or resetting to enter flashing mode                                                              |

### 2.3 Interface Description

#### 2.3.1 Power Input

- Interfaces: USB Type-C and ATX 2-pin (ATX preferred by default)
- Supports USB-PD 3.0, up to 20 V / 5 A
- Supports direct ATX power input, up to 12 V / 6 A
- In flashing mode, the Type-C port provides both power and USB device connectivity. When connected to a host PC via USB Type-C, the board can be detected and used for firmware flashing and upgrades.s

![](./static/power00.png)  

#### 2.3.2 Flashing Interface

When the board enters flashing mode, this port operates as a USB device for data transfer only and cannot supply power to the board. Connect the board to a host computer via USB Type-C to allow the device to be detected and perform firmware flashing or upgrades.

> **Note:**
> - The flashing Type-C port cannot power the board. During flashing, the board must be powered through another power input.
> - A data-capable USB cable is required. Charge-only cables are not supported for flashing.

![](./static/flash00.png)  

#### 2.3.3 Full-Function Type-C Port

- USB-C connector
- Supports USB-PD 3.0 voltage negotiation
- Supports DisplayPort output
- Supports USB 3.0 peripherals

![](./static/type-c00.png) 

#### 2.3.4 High-Speed Expansion — M.2 M-Key & B-Key

**M.2 M-Key**

- NVMe SSD support (2280)
- PCIe 3.0 ×2 / ×4 bandwidth

**M.2 B-Key**

- PCIe SSD (2242) — PCIe 3.0 ×2
- USB 2.0 4G modem support

**Notes**

1. If a PCIe SSD is installed in the B-Key slot, the M-Key slot runs at **PCIe 3.0 ×2**. Otherwise it runs at **PCIe 3.0 ×4**.
2. The B-Key slot supports **PCIe SSD only (no SATA)**.
3. **Hot-plugging is not supported.**

---

#### 2.3.5 eDP Display Interface

- External eDP display supported
- Up to **2560×1600 @ 90Hz**
- **No hot-plug support**
- When only eDP is connected, it is the **primary display**

---

#### 2.3.6 DP Display via Type-C

- Supports external DisplayPort monitor
- Up to **4K @ 60Hz**
- **Hot-plug supported**

Display priority:

- DP only → DP is primary
- DP + eDP → eDP is primary (configurable in OS)

---

#### 2.3.7 Audio Interface

- 1.25 mm board-to-board connector
- Supports front-panel **3.5 mm audio jack via adapter cable**

---

#### 2.3.8 1G Ethernet (RJ45)

- 10/100/1000 Mbps auto-negotiation

LED indicators:

**Green — Link Speed**

- Solid: link at highest speed
- Off: link at lower speed or no link

**Yellow — Activity**

- Blinking: data activity
- Off: no activity or no link

---

#### 2.3.9 10G Optical Ethernet

- SFP+ interface
- Supports **10GbE**

---

#### 2.3.10 USB 2.0

- USB Type-A host
- Plug-and-play
- Supports multiple peripherals

---

#### 2.3.11 FPC Expansion Connector

- 0.5 mm pitch, **26-pin + 36-pin**
- Provides:

  - CAN ×5
  - UART ×2
  - GMAC ×1
  - PWM ×2
  - I²C ×1
  - SPI ×1
- Supports direct connection to expansion boards

---

### 2.4 Specifications

| Item                     | Specification                                                                                          |
| ------------------------ | ------------------------------------------------------------------------------------------------------ |
| **Processor**            | SpacemiT K3, 8-core @ 2.4 GHz, 60 TOPS AI compute, RVA23 compliant, IME extension, full virtualization |
| **Display**              | DP (USB-C) up to 4K@60Hz; eDP up to 2.5K@90Hz                                                          |
| **Memory**               | Dual-channel LPDDR5 6400 MT/s, 16GB / 32GB                                                             |
| **Storage**              | UFS 2.2, 128GB / 256GB                                                                                 |
| **Storage Expansion**    | M.2 M-Key NVMe SSD, PCIe Gen3 ×4                                                                       |
| **High-Speed Expansion** | M.2 B-Key PCIe Gen3 ×2 + USB                                                                           |
| **Real-Time Expansion**  | FPC connector: EtherCAT, CAN-FD ×5, SPI, I²C, UART                                                     |
| **Wireless**             | Wi-Fi 6 + Bluetooth 5.2 (dual-band, dual-antenna)                                                      |
| **Ethernet**             | 1× RJ45 GbE                                                                                            |
| **Optical Network**      | 10GbE SFP+ (10G BASE-R / BASE-X, QinQ, MSI-X, WoL)                                                     |
| **Audio**                | On-board codec                                                                                         |
| **USB**                  | 2× USB-C (1 full-function, 1 OTG), 4× USB 2.0 Type-A                                                   |
| **Debug**                | UART & JTAG, onboard control buttons                                                                   |
| **Management**           | On-board EC for power, thermal, and system monitoring                                                  |
| **Form Factor**          | 100 × 86 mm Pico-ITX Plus                                                                              |
| **OS Support**           | Bianbu 3.0 (preinstalled), Ubuntu 26.04, OpenHarmony 6.0, OpenKylin, Deepin, Fedora                    |
| **Power**                | Dual USB-C PD (65W), ATX 2-pin 12V@7A                                                                  |
| **Reliability**          | ESD protection, CCC / CE / FCC compliance                                                              |
| **Operating Temp**       | Consumer: −20°C ~ 70°C; Industrial: −40°C ~ 85°C                                                       |
| **RTC**                  | Battery-backed RTC                                                                                     |
| **Mechanical Options**   | Fan heatsink, industrial enclosure, expansion boards                                                   |

---

## 3. OS Installation

### 3.1 Flash via Type-C

#### Scenario A — Device Powered Off

1. Hold **FDL button**
2. Connect Type-C cable to host and apply power
3. Release FDL button
4. Flash using **Titan** or `fastboot`

#### Scenario B — Device Powered On

1. Hold **FDL button**
2. Press **RST**
3. Release FDL button
4. Flash using **Titan** or `fastboot`

---

### 3.2 Serial Debugging

Connect a **USB-to-TTL adapter** to **TX / RX / GND**.

#### Windows Example (MobaXterm)

- Select detected COM port
- Baud rate: **115200**

---

## 4. Quick Start

Required peripherals:

- Power supply
- Display
- Keyboard
- Mouse

Connect peripherals and power on the board to start using it.

> A power-capable monitor can supply power via DisplayPort.

---

## 5. Safety Notes

- Do **not hot-plug** display, CSI, or expansion boards.
- Use **ESD protection** during handling.
- Hold the board by the edges only.
- Keep away from heat, EMI, and sensitive medical devices.
- Ensure proper ventilation for long-term full-load operation.

---

## 6. Open Resources

Mechanical drawings and dimensions are provided.

---

## 7. Appendix — Pin Definitions

### 7.1 FPC Expansion (26-pin + 36-pin)

**26-pin:** CAN + I²C + UART + PWM + 3.3V
**36-pin:** GMAC-MII + CAN + SPI + 1.8V

### 7.2 UART Debug Header

1×3 header pinout (bottom → top):

**GND → RX → TX**

> Board appearance may vary by hardware revision.
