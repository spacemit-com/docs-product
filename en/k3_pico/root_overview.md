sidebar_position: 1

# K3 Pico-ITX Brief

**[PDF Version](https://cdn-resource.spacemit.com/file/%E8%8A%AF%E7%89%87/K3/K3_Pico-ITX_EN_0127.pdf)**

The MUSE Pico is a 2.5" Pico-ITX Plus single-board computer delivering 60 TOPS of performance with 8 CPU cores and 8 AI cores under a unified memory architecture. It features onboard UFS storage, 10 GbE optical networking, and dual M.2 expansion slots, providing strong computing and connectivity for AI and scientific applications.
With interfaces for real-time motion control and system management, and an industrial-grade compact design, MUSE Pico enables rapid evaluation, integration, and commercialization across space-constrained industrial scenarios.

## Key Features

- K3 8-core processor (RVA23 standard) delivering 60 TOPS, with IME vector extensions and full virtualization.
- Unified memory architecture for CPU and AI cores, supporting models up to 30 billion parameters.
- Onboard UFS storage—3.4× faster than typical eMMC.
- Dual M.2 slots (B-KEY & M-KEY), with M-KEY PCIe Gen3 ×4 for NVMe SSD expansion.
- 10 GbE PCIe Ethernet with 10G-BASE-R optical interface, ensuring low-latency, high-throughput data transfer and cluster deployment.
- Full-function Type-C port supporting 65 W PD power and 4K DP display—one cable for power and display.
- Onboard eDP interface for industrial-grade HD screen integration.
- RT24 real-time core I/O slot supporting EtherCAT, CAN-FD, and other interfaces for microsecond-level motion control and robotics.
- MUSE thermal architecture with separated hot/cold zones for optimal CPU performance and efficiency.

## Specifications

|Module | Description |
|------|------|
| Processor | SpacemiT K3, 8 cores @2.4 GHz, 60 TOPS AI performance, RVA23 compliant, supports IME vector extensions and full virtualization |
| Display   | DP Type-C: up to 4K (3840×2160) @ 60 Hz<br>40-pin eDP: up to 2.5K (2560×1600) @ 90 Hz                                         |
| Memory    | Dual-channel 2x32bit LPDDR5 6400 MT/s, 16 GB / 32 GB options                                                                |
| Local Storage | UFS 2.2, 128 GB / 256 GB options                                                                                       |
| Storage Expansion | M.2 M-Key (PCIe Gen3 ×4), supports 2280 NVMe SSD                                                            |
| HS Expansion | M.2 B-Key (PCIe Gen3 ×2 + USB), supports 2242/3042 cards                                                       |
| Real-Time Expansion | FPC connector for EtherCAT, 5× CAN-FD, SPI, I²C, UART, etc.                                                           |
| Wireless Communication | Onboard Wi-Fi 6 + BT 5.2, dual-band, dual-antenna, 802.11 a/b/g/n/ac/ax compliant                            |
| Wired Network | 1× RJ45 Ethernet, 10/100/1000 Mbps adaptive                                                                            |
| Optical Network | 10 GbE SFP+ port, supports 10G BASE-R / BASE-X, QinQ, MSI-X, WOL, and clustering                                 |
| Audio     | Onboard CODEC, internal audio input/output                                                                               |
| USB       | 2× USB 3.2 Gen1 Type-C (1 full-featured, one OTG)<br>4× USB 2.0 Type-A Host                                              |
| Debug     | UART, JTAG, and 3 side buttons for power, reset, and firmware update                                                      |
| System Management | Onboard EC controller for power, thermal, and system status; includes I²C/UART/GPIO expansion                    |
| Form Factor | 100 × 86 mm, Pico-ITX Plus single-board computer, approx. size of a 2.5" drive                                         |
| OS        | Pre-installed Bianbu 3.0; supports Ubuntu 26.04, OpenHarmony 6.0, OpenKylin, Deepin, Fedora, etc.                           |
| Power Input | Dual Type-C USB-PD (65 W) or ATX 2-pin 12 V @ 7 A                                                                        |
| Reliability | ESD protection: Board: ±4 kV (contact), ±8 kV (air); System: ±6 kV (contact), ±12 kV (air)<br>Compliant with CCC, CE, FCC; operating temp: -20 °C ～ 70 °C (consumer) / -40 °C ～ 85 °C (industrial) |
| Clock     | Onboard RTC with battery interface, supports G3 state                                                                      |
| Structure | Optional single-board or fan-cooled heatsink assembly<br>Optional single-board or fully-metal industrial chassis<br>Optional real-time board, touchscreen, terminal blocks|

>**Note:** The M.2 B-Key PCIe ×2 lanes are shared with the M-Key slot; when both are populated, the M.2 M-Key operates at PCIe Gen3 ×2.

## Block Diagram

![](./static/pico_bd.png)

## Optional Components

| Category             | Name                     | Description   | Interface               |
|----------------------|--------------------------|---------------|-------------------------|
| Peripheral           | SSD                      | 980 NVMe™ M.2 SSD, PCIe Gen 3.0 x4, NVMe 1.4, <br>sequential read up to 3,500 MB/s, <br>sequential write up to 3,000 MB/s | M.2 M-KEY 2280          |
| Peripheral           | SSD                      | B+M NVMe SSD 128GB  | M.2 B-KEY 2242          |
| Peripheral           | 4G Module                | EM05    | M.2 B-KEY 3042          |
| Peripheral           | SATA Expansion Card      | PCIe to 5×SATA interface   | M.2 M-KEY 2280          |
| Peripheral           | Docking Station          | Type-C dock for HD 4K display, PD charging, <br>USB 3.0 for tablets/laptops (3-in-1)                        | Full-feature Type-C     |
| Peripheral           | Ultra HD Display         | 16" 2.5K LCD, 90Hz, 2560×1600   | 40-pin eDP              |
| Peripheral           | Real-time Control Expansion Board | 19V Input, 5x CAN-FD, EtherCAT, RS232 & RS485 I/O, <br>Industrial-Grade Isolation Protection             | FAN                     |
| Structural Accessory | Embedded Fan Heatsink    | Custom aluminum design    | FAN                     |
| Structural Accessory | Metal Chassis            | 120*120*48mm Self-developed Metal Chassis                                                                | BTN                     |

## Business Cooperation & Purchase

- **WeChat (Business)**: SpacemiT1102
- **Phone**: +86 189 6649 8607
- **Email**: [business@spacemit.com](mailto:business@spacemit.com)