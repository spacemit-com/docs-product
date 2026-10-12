---
sidebar_position: 2
---

# K1 MUSE Card User Guide

## Product Overview

**K1 MUSE Card** is the first board in SpacemiT's developer ecosystem series. It is powered by the SpacemiT M1, an 8-core RISC-V high-performance processor with 2 TOPS AI processing power built in, enabling rapid deployment of any AI model algorithm.

**K1 MUSE Card** fully demonstrates the versatility of the M1 chipset. It exposes M1 native interfaces including HDMI, a single RJ45 port, USB 3.0, USB 2.0, and dual M.2 2242 M-KEY slots. It supports SpacemiT Bianbu OS, Bianbu NAS, OpenHarmony, OpenKylin, Deepin, and other operating systems, making it suitable for rapid evaluation and prototyping of industry control, NAS, machine vision, gateway, and other product forms.

## Preface

### Overview

This document describes the basic functions, hardware features, multi-function hardware configuration, and software debugging procedures of the **K1 MUSE Card**. It is intended to help engineers use MUSE Card more quickly and accurately, and to familiarize them with M1 chip development application solutions.

**Product Version**

| Product Name | Product Version |
| --- | --- |
| MUSE Card | MUSE Card_P1_LP4X200B32X1_V20_08061538 |

## Abbreviations

| Abbreviation | English Description |
| --- | --- |
| X60 | self-innovate X60 RISC-V processor core |

## Specifications

<table>
<tbody>
<tr>
<td><strong>SoC</strong></td>
<td>CPU</td>
<td>SpacemiT M1 (SpacemiT Key Stone® M1 high-performance variant), 8-core RISC-V processor with 2 TOPS AI processing power<br/>8 x RISC-V X60 Core 64-bit</td>
</tr>
<tr>
<td><strong>Display</strong></td>
<td>Interface</td>
<td>MIPI DSI 4-lane & HDMI standard video interface<br/>Up to 1080P@60Hz output</td>
</tr>
<tr>
<td rowspan=2><strong>Memory</strong></td>
<td>Type</td>
<td>LPDDR4X, 2400 MT/s, on-board</td>
</tr>
<tr>
<td>Capacity</td>
<td>8 GB / 16 GB optional</td>
</tr>
<tr>
<td rowspan=3><strong>Storage</strong></td>
<td>SSD</td>
<td>PCIe (NVMe)</td>
</tr>
<tr>
<td>SPI NOR Flash</td>
<td>64 Mb, for board ID and SSD boot loader</td>
</tr>
<tr>
<td>TF Card</td>
<td>Supported; interface can also be used as UART / JTAG for debugging</td>
</tr>
<tr>
<td rowspan=2><strong>I/O</strong></td>
<td>Side I/O</td>
<td>1 x USB 2.0 Type-C (Device, supports up to 12V 3A PD power input)<br/>1 x USB 3.0 Type-A<br/>1 x USB 2.0 Type-A<br/>1 x RJ45 (1000M/100M/10M auto-adaptive)<br/>1 x HDMI<br/>1 x TF Card</td>
</tr>
<tr>
<td>On-board I/O</td>
<td>2 x MIPI CSI 4-lane (4+4 or 4+2+2)<br/>1 x MIPI DSI 4-lane<br/>2 x M.2 2242 M-KEY<br/>40-pin standard GPIO header</td>
</tr>
<tr>
<td><strong>Buttons</strong></td>
<td>Function</td>
<td>Reset, Flash (download)</td>
</tr>
<tr>
<td rowspan=2><strong>Appearance</strong></td>
<td>Dimensions</td>
<td>85 x 56 mm</td>
</tr>
<tr>
<td>Material</td>
<td>Black PCB, optional transparent acrylic case</td>
</tr>
<tr>
<td><strong>Software</strong></td>
<td>OS</td>
<td>Bianbu OS, Ubuntu, Bianbu Linux, OpenHarmony, OpenKylin, Deepin, and more</td>
</tr>
<tr>
<td><strong>Power</strong></td>
<td>Input</td>
<td>PD3.0 Type-C power supply</td>
</tr>
<tr>
<td rowspan=2><strong>Reliability</strong></td>
<td>ESD</td>
<td>Interface protection: contact ±4 kV, air ±8 kV</td>
</tr>
<tr>
<td>Operating temp.</td>
<td>Consumer-grade (-20°C to 70°C) or industrial-grade (-40°C to 85°C)</td>
</tr>
</tbody>
</table>

## System Overview

### M1 Chip Overview

M1 is a high-performance, ultra-low-power SoC integrating an 8-core RISC-V CPU and SpacemiT AI compute capability. Key features:

- Integrates the SpacemiT X60™ RISC-V processor core, conforming to the RISC-V 64GCVB architecture and RVA22 standard.
- Extends 2 TOPS AI compute through RISC-V custom instructions, enabling CPU-AI fused compute supporting TensorFlow Lite, TensorFlow, and ONNX Runtime mainstream inference frameworks.
- Achieves ultra-low power through multi-domain power partitioning and multi-level power states.
- Supports a full-featured interface set for innovative applications and products.
- Compatible with mainstream operating systems for a wide range of application scenarios.
- Meets industrial-grade reliability standards.

### M1 Chip Block Diagram

![](static/UZOLbwx4ao3II9xW2sHcbScenH2.png)

### M1 MUSE Card Reference Design Block Diagram

#### Reference Design Block Diagram

The M1 MUSE Card system uses the M1 chip with a P1 PMIC + external DCDC power solution. DRAM is LPDDR4X. It integrates dual M.2 2242 M-KEY, USB 2.0 Type-A, USB 3.0 Type-A, TF Card, HDMI, MIPI DSI, MIPI CSI, Type-C, and RJ45 peripheral interfaces in a stable, production-ready design.

![](static/Qz1kbDpYhoyescxR24VcFNTVnBc.png)

#### Feature Overview

M1 MUSE Card includes the following features:

- TYPE-C: one USB 2.0 Device Type-C interface, compatible with system firmware flashing and PD3.0 12V/3A power supply.
- HDMI 1.4 OUT: one HDMI 1.4 Type-A output, up to 1920×1080@60Hz.
- MIPI DSI/TP: via a 31-pin connector, one 4-lane MIPI DSI signal for LCD, one I2C signal for CTP touchscreen. Display and touch can be implemented with the optional adapter board.
- MIPI CSI: via a 60-pin high-speed connector, two 4-lane MIPI CSI signals supporting 16 MP and 8 MP cameras. Custom adapter boards can be designed to match specific camera modules, enabling 4+4 or 4+2+2 configurations.
- 40-pin dual-row header: compatible with Raspberry Pi standard 40-pin header, supporting I2C, UART, SPI, JTAG, and GPIO debugging.
- TF card slot: supports high-speed TF cards.
- Ethernet: single RJ45 port, 10/100/1000M.
- PCIe 2.1 2-lane interface: two standard M.2 2242 M-KEY slots for PCIe device expansion.
- USB 2.0 Type-A: single channel for USB device expansion.
- USB 3.0 Type-A: single channel for USB device expansion.
- UART Debug: for reading log output; supports 3-pin single-row header (J25) to debug X60; pins 6, 8, 10 of the 40-pin header also support UART debug.
- JTAG: supports PRI JTAG via 40-pin header pins 7, 11, 13, 15. SEC JTAG debug is supported via optional TF card adapter board.
- System Key: Reset, Power On, Download (FEL) buttons.
- SWITCH: boot media selection (via resistor change).

#### Feature Interface Table

| Feature | Available |
| --- | --- |
| LPDDR4x | YES |
| SPI FLASH | YES |
| TYPE-C 12V Input | YES |
| HDMI 1.4 OUT | YES |
| MIPI DSI/TP | YES |
| MIPI CSI | YES |
| TF Card | YES |
| Gigabit Ethernet 10M/100M/1000M | YES |
| PCIe 2.0 2-lane Interface (2 ports) | YES |
| USB 2.0 Type-A | YES |
| USB 3.0 Type-A | YES |
| UART Debug (3-pin + 40-pin) | YES |
| JTAG (40-pin) | YES |
| System Key | YES |

## Hardware Description

### Board Photo

![](static/K8FjbwgGoogYiMx8muHc8rxJn1e.png)

### Power Block Diagram

![](static/VGW7btsj5oTOeUxvoTgcu2ROnRG.png)

### Boot Download Sel & JTAG Sel

SEC2 JTAG circuit: M1 SEC2 JTAG is multiplexed with MMC1 (TF CARD). Pull JTAG_SEL high and MMC1_CMD low to configure as SEC2 JTAG for X60 CPU debugging.

![](static/Yhlmb7VrZoSvVjxEfgrcXoxMnpc.png)

Boot Download Sel circuit: M1 supports boot media selection via strap pins. Strap pins default low; add pull-up resistors to override. MUSE Card is configured for NOR+SSD boot by default.

![](static/BRlnbk3NkofCTfx4Issc6F04n5e.png)

**Note:** Default boot order: TF card first → if no card detected → boot per configured strap pin setting.

**When booting from NOR+SSD flash, the SSD must be inserted in the slot shown below.**

![](static/NG8mbHObhoL2DFx3YkEc874HnGf.png)

### I2C Addresses

The board exposes many peripheral interfaces. When debugging I2C peripherals, be aware of I2C channel multiplexing. The diagram below shows I2C addresses and pull-up power rails for on-board devices to help avoid address conflicts and level mismatches.

![](static/MY3dbrL1oohVnxxQxW4cfN74n1b.png)

## Module Description

### Power Input

MUSE Card has one power input method: Type-C input via a PD3.0-compatible adapter, with input voltage defaulting to 12V. After the front-end buck converter, VCC5V0_SYS and VCC4V0 are generated to power the external DCDC and PMIC respectively, producing various supply voltages for the system. The M.2 slot 3.3V rail carries relatively high current and is derived directly from the adapter input via the buck converter.

![](static/HBL7bZSeCo734HxMIzmcJ7MrnOg.png)

### Memory

SPI Flash: 64 Mb, for fast boot support.

DDR: one 8/16 GB LPDDR4X chip.

EEPROM: stores board information.

![](static/HIWqbhJKfo294GxpDnZctHZ1npf.png)

### Button Inputs

![](static/ZTo2bwaocomk6Yx0DvHcBi1SnVd.png)

### MIPI CSI High-Speed Connector

MUSE Card does not target a specific camera module. The high-speed connector carries two groups of 4-lane signals. Design a custom adapter board matching the connector pinout to support your target module, achieving 4+4 or 4+2+2 camera combinations.

![](static/A52vbmplyoOK6DxdOtHc8ALon79.png)

60-pin high-speed connector pinout:

<table>
<tbody>
<tr>
<td>Pin</td>
<td>Signal</td>
<td>Signal</td>
<td>Pin</td>
</tr>
<tr><td>1</td><td>GND</td><td>CAM_MCLK2</td><td>60</td></tr>
<tr><td>2</td><td>MIPI_CSI_DN0</td><td>VCC5V0_SYS</td><td>59</td></tr>
<tr><td>3</td><td>MIPI_CSI_DP0</td><td>CAM_I2C7_SDA</td><td>58</td></tr>
<tr><td>4</td><td>GND</td><td>CAM_I2C7_SCL</td><td>57</td></tr>
<tr><td>5</td><td>MIPI_CSI1_DN1</td><td>CAMERA2_RST</td><td>56</td></tr>
<tr><td>6</td><td>MIPI_CSI1_DP1</td><td>CAMERA2_PDN</td><td>55</td></tr>
<tr><td>7</td><td>GND</td><td>CAM_MCLK1</td><td>54</td></tr>
<tr><td>8</td><td>MIPI_CSI1_DN2</td><td>GND</td><td>53</td></tr>
<tr><td>9</td><td>MIPI_CSI1_DP2</td><td>CAM_I2C1_SDA</td><td>52</td></tr>
<tr><td>10</td><td>GND</td><td>CAM_I2C1_SCL</td><td>51</td></tr>
<tr><td>11</td><td>MIPI_CSI1_DN3</td><td>GND</td><td>50</td></tr>
<tr><td>12</td><td>MIPI_CSI1_DP3</td><td>MIPI_CSI3_DN0</td><td>49</td></tr>
<tr><td>13</td><td>GND</td><td>MIPI_CSI3_DP0</td><td>48</td></tr>
<tr><td>14</td><td>MIPI_CSI1_CLKN</td><td>GND</td><td>47</td></tr>
<tr><td>15</td><td>MIPI_CSI1_CLKP</td><td>MIPI_CSI3_DN1</td><td>46</td></tr>
<tr><td>16</td><td>GND</td><td>MIPI_CSI3_DP1</td><td>45</td></tr>
<tr><td>17</td><td>CAMERA0_RST</td><td>GND</td><td>44</td></tr>
<tr><td>18</td><td>CAMERA0_PDN</td><td>MIPI_CSI3_DN2</td><td>43</td></tr>
<tr><td>19</td><td>GND</td><td>MIPI_CSI3_DP2</td><td>42</td></tr>
<tr><td>20</td><td>CAM_MCLK0</td><td>GND</td><td>41</td></tr>
<tr><td>21</td><td>GND</td><td>MIPI_CSI3_DN3</td><td>40</td></tr>
<tr><td>22</td><td>CAM_I2C0_SDA</td><td>MIPI_CSI3_DP3</td><td>39</td></tr>
<tr><td>23</td><td>CAM_I2C0_SCL</td><td>GND</td><td>38</td></tr>
<tr><td>24</td><td>GND</td><td>MIPI_CSI3_CLKN</td><td>37</td></tr>
<tr><td>25</td><td>GND</td><td>MIPI_CSI3_CLKP</td><td>36</td></tr>
<tr><td>26</td><td>CSI_DVDD12</td><td>GND</td><td>35</td></tr>
<tr><td>27</td><td>CSI_VCCI018</td><td>MIPI_CSI2_CLKN</td><td>34</td></tr>
<tr><td>28</td><td>CSI_AVDD28</td><td>MIPI_CSI2_CLKP</td><td>33</td></tr>
<tr><td>29</td><td>CSI_AFVCC28</td><td>GND</td><td>32</td></tr>
<tr><td>30</td><td>CAMERA1_PDN</td><td>CAMERA1_RST</td><td>31</td></tr>
</tbody>
</table>

### MIPI DSI Display Connector

The board supports a 1080P display (JL-M101N013-P12WU-M402632). Display connector part number: FH35C-31S-0.3SHW(50).

![](static/MBwTbSiIooIxkExujoOcBQhXnbh.png)

Display connector pinout:

<table>
<tbody>
<tr>
<td>Pin</td>
<td>Signal</td>
<td>Signal</td>
<td>Pin</td>
</tr>
<tr><td>1</td><td>MIPI_DSI1_LANE0_DN</td><td>MIPI_DSI1_LANE0_DP</td><td>2</td></tr>
<tr><td>3</td><td>GND</td><td>MIPI_DSI1_LANE1_DN</td><td>4</td></tr>
<tr><td>5</td><td>MIPI_DSI1_LANE1_DP</td><td>GND</td><td>6</td></tr>
<tr><td>7</td><td>MIPI_DSI1_CLK_N</td><td>MIPI_DSI1_CLK_P</td><td>8</td></tr>
<tr><td>9</td><td>GND</td><td>MIPI_DSI1_LANE2_DN</td><td>10</td></tr>
<tr><td>11</td><td>MIPI_DSI1_LANE2_DP</td><td>GND</td><td>12</td></tr>
<tr><td>13</td><td>MIPI_DSI1_LANE3_DN</td><td>MIPI_DSI1_LANE3_DP</td><td>14</td></tr>
<tr><td>15</td><td>GND</td><td>MIPI_LCD_ADC_1V8</td><td>16</td></tr>
<tr><td>17</td><td>LCD_PWR_EN_1V8</td><td>LCD_RST_1V8</td><td>18</td></tr>
<tr><td>19</td><td>LCD_BL_EN_1V8</td><td>LCD_BL_PWM_1V8</td><td>20</td></tr>
<tr><td>21</td><td>GND</td><td>TP_INT_1V8</td><td>22</td></tr>
<tr><td>23</td><td>TP_RST_1V8</td><td>AP_I2C6_SCL</td><td>24</td></tr>
<tr><td>25</td><td>AP_I2C6_SDA</td><td>LCD_VCC18</td><td>26</td></tr>
<tr><td>27</td><td>GND</td><td>GND</td><td>28</td></tr>
<tr><td>29</td><td>LCD_VCC5V0</td><td>LCD_VCC5V0</td><td>30</td></tr>
<tr><td>31</td><td>LCD_VCC5V0</td><td>GND</td><td>32</td></tr>
<tr><td>33</td><td>GND</td><td></td><td></td></tr>
</tbody>
</table>

![](static/KZe9bYtNJo9kHpxC6k7coxpgny5.png)

### Type-C Connector

The board's Type-C connector supports USB 2.0 Device with an integrated voltage-regulation chip that supports PD3.0 negotiation up to 12V for powering the MUSE Card.

![](static/TUWybEm3soHj55xnYzqc2sfAnZd.png)

### HDMI Output

One HDMI standard Type-A output, HDMI 1.4, up to 1080p@60fps.

![](static/PsVLbzNHSowi6nxstxzcap4Xnmb.png)

### USB Interfaces

One USB 2.0 Type-A and one USB 3.0 Type-A for connecting USB devices.

![](static/PExybY156oIlQ5xZNWTcyB2Fnjg.png)

### RJ45 Interface

Single Gigabit RJ45 Ethernet port.

![](static/L87MbZBsAoaj2ZxU2dGcJpwUntd.png)

### 40-Pin Header

The board supports a standard 40-pin dual-row header. **Bold** entries are the current default function; other functions require manual configuration.

<table>
<tbody>
<tr>
<td>Pin</td>
<td>Definition</td>
<td>Definition</td>
<td>Pin</td>
</tr>
<tr><td>1</td><td>VCC3V3_SYS</td><td>VCC5V0_OUT</td><td>2</td></tr>
<tr><td>3</td><td><strong>AP_I2C4_SDA_3V3</strong><br/>{GPIO[52] / R_SPI_RXD / R_UART1_RXD / R_PWM7}</td><td>VCC5V0_OUT</td><td>4</td></tr>
<tr><td>5</td><td><strong>AP_I2C4_SCL_3V3</strong><br/>{R_SPI_TXD / R_UART1_TXD / R_PWM6}</td><td>GND</td><td>6</td></tr>
<tr><td>7</td><td><strong>PRI_TDI</strong><br/>{GPIO70_3V3 / AP_I2C2_SCL_3V3 / UART5_TXD}</td><td><strong>R_UART0_TXD_3V3</strong><br/>{GPIO[47] / R_CAN_TX0 / R_PWM8 / AP_I2C3_SCL}</td><td>8</td></tr>
<tr><td>9</td><td>GND</td><td><strong>R_UART0_RXD_3V3</strong><br/>{GPIO[48] / R_CAN_RX0 / R_IR_RX / AP_I2C3_SDA / KP_MKOUT[2]}</td><td>10</td></tr>
<tr><td>11</td><td><strong>GPIO_71_3V3</strong><br/>{PRI_TMS / AP_I2C2_SDA_3V3 / UART5_RXD}</td><td><strong>GPIO74_3V3</strong><br/>{R_PWM9 / PCIe2_WAKEN}</td><td>12</td></tr>
<tr><td>13</td><td><strong>GPIO72_3V3</strong><br/>{PRI_TCK / UART9_TXD / UART5_CTS_N}</td><td>GND</td><td>14</td></tr>
<tr><td>15</td><td><strong>GPIO73_3V3</strong><br/>{PRI_TDO / UART9_RXD / UART5_RTS_N}</td><td><strong>GPIO_91_3V3</strong><br/>{MN_CLK2 / DSI_TE / R_I2C0_SCL}</td><td>16</td></tr>
<tr><td>17</td><td>VCC3V3_SYS</td><td><strong>GPIO_92_3V3</strong><br/>{MN_CLK / PWM7 / R_I2C0_SDA}</td><td>18</td></tr>
<tr><td>19</td><td><strong>SPI3_MOSI_3V3</strong><br/>{GPIO[77] / SPI2_MOSI / AP_I2C3_SCL / UART8_CTS_N / R_PWM0 / KP_MKOUT[2] / AP_CW[14]}</td><td>GND</td><td>20</td></tr>
<tr><td>21</td><td><strong>SPI3_MISO_3V3</strong><br/>{GPIO[78] / SPI2_MISO / AP_I2C3_SDA / UART8_RTS_N / R_PWM1 / KP_MKIN[3] / AP_CW[15]}</td><td><strong>GPIO_49_3V3</strong><br/>{R_SPI_SCLK / R_UART1_CTS_N / R_PWM4 / R_I2C0_SCL / KP_MKIN[3]}</td><td>22</td></tr>
<tr><td>23</td><td><strong>SPI3_SCLK_3V3</strong><br/>{GPIO[75] / SPI2_SCLK / CAN_TX0 / UART8_TXD / AP_I2C4_SCL / AP_CW[12]}</td><td><strong>SPI3_CS_3V3</strong><br/>{GPIO[76] / SPI2_CS / CAN_RX0 / UART8_RXD / AP_I2C4_SDA / AP_CW[13]}</td><td>24</td></tr>
<tr><td>25</td><td>GND</td><td><strong>GPIO_50_3V3</strong><br/>{R_SPI_FRM / R_UART1_RTS_N / R_PWM5 / R_I2C0_SDA / KP_MKOUT[3]}</td><td>26</td></tr>
<tr><td>27</td><td><strong>AP_I2C3_SDA_3V3</strong><br/>{GPIO[38] / GMAC1_TX_D2 / R_I2S3_SCLK / PWM8}</td><td><strong>AP_I2C3_SCL_3V3</strong><br/>{GPIO[39] / GMAC1_TX_D3 / R_I2S3_LRCK / PWM9}</td><td>28</td></tr>
<tr><td>29</td><td><strong>GPIO_29_3V3</strong><br/>{GMAC1_RXDV / UART1_TXD / PWM1 / PCIe0_PERSTN}</td><td>GND</td><td>30</td></tr>
<tr><td>31</td><td><strong>GPIO_30_3V3</strong><br/>{GMAC1_RX_D0 / UART1_RXD / PWM2 / PCIe0_WAKEN}</td><td><strong>GPIO_34_3V3</strong><br/>{GMAC1_RX_D3 / UART4_RXD / PWM4 / PCIe1_CLKREQN}</td><td>32</td></tr>
<tr><td>33</td><td><strong>GPIO_31_3V3</strong><br/>{GMAC1_RX_D1 / UART1_CTS_N / PCIe0_CLKREQN}</td><td>GND</td><td>34</td></tr>
<tr><td>35</td><td><strong>GPIO_32_3V3</strong><br/>{GMAC1_RX_CLK / UART1_RTS_N / MN_CLK / PCIe1_PERSTN}</td><td><strong>GPIO_35_3V3</strong><br/>{GMAC1_TX_D0 / UART4_CTS_N / PWM5 / PCIe2_PERSTN}</td><td>36</td></tr>
<tr><td>37</td><td><strong>GPIO_33_3V3</strong><br/>{GMAC1_RX_D2 / UART4_TXD / PWM3 / PCIe1_WAKEN}</td><td><strong>GPIO_46_3V3</strong><br/>{GMAC1_CLK_REF / PWM16}</td><td>38</td></tr>
<tr><td>39</td><td>GND</td><td><strong>GPIO_37_3V3</strong><br/>{GMAC1_TX / PWM7 / PCIe2_CLKREQN}</td><td>40</td></tr>
</tbody>
</table>

![](static/ViawbMuByoFJd4xoc2WcR8LWnXe.png)

### UART Debug Interface

3-pin single-row header supporting UART0 (GPIO68-TX, GPIO69-RX). Host-side pinout left to right: TX, RX, GND.

![](static/A85RbReKOolrQzxPB1acZEdtnae.png)

### TF Card Slot (No Eject Spring)

Supports TF cards for storage. Also supports a debug expansion card for UART0 or JTAG debugging.

![](static/FHL6boVaOoluyNxLkYacEDp1nOf.png)

### M.2 M-Key Interface

Dual M.2 2242 M-KEY slots for NVMe SSDs or other M.2 M-Key devices. Also supports a JMB582 expansion card for SATA conversion.

![](static/BVcxbXIbToHkiTxn1C8cLdeNnIc.png)

## Initial Setup

### Before You Begin

MUSE Card is a development board and requires external peripherals.

**Power Adapter**

MUSE Card is powered via USB PD3.0 Type-C. Use a PD3.0-compatible adapter with an output of at least 30W.

![](static/WS8XbVF1koGEnTxlBNQc9gDynmb.png)

**Keyboard & Mouse**

Connect a wired keyboard and mouse (or USB receiver) to any USB Type-A port, or connect wirelessly via Bluetooth.

![](static/MCjGb3htEo4K35xLSDmceYtvnIb.png)

**Display**

MUSE Card outputs video via HDMI or MIPI DSI. Connect a display with HDMI or MIPI DSI input.

Note: MIPI DSI does not support hot-plug. Connect the MIPI DSI cable to the display and MUSE Card before powering on.

![](static/JlcZbbxihomu2gxwkk0cfC27nvc.png)

**Audio**

MUSE Card supports HDMI audio. Set the audio output source to HDMI in the OS settings to play audio through the HDMI display.

**Network**

MUSE Card supports wired RJ45 Ethernet. Connect a network cable directly to the RJ45 port.

![](static/EtVlb1YK7oBck0xvXTkcQMJmnvh.png)

### Powering On

Connect all required peripherals and press the power button:

Connect the board to a display via a video cable, then connect keyboard and mouse. Finally, plug in the power cable — the board powers on automatically the first time. After a software shutdown, press the power button for 1 second to power on again. The red power LED lights up when the board is running.

![](static/HrKTbFhiVo2F6sxsZDVcYLAZn7b.png)

### First-Boot Setup

Your MUSE Card comes pre-installed with SpacemiT Bianbu Desktop OS and runs a setup wizard on first boot. You will need a display, keyboard, and mouse.

**System Language**:
Choose the system language. English and Chinese are shown by default; click the three dots at the bottom for more options.

![](static/C62rbTD84oUs0lxSd6wcpdhZnCg.png)

**Input Method**:
Configure your keyboard layout and input method.

![](static/H8qUbDL74oXF0KxkkS5c55vNnYb.png)

**Wi-Fi**:
Connect to a Wi-Fi network by selecting it from the list. If no suitable network is available, click Skip in the upper-left corner.

![](static/GebabRy1soHRFExqi7CcL4oRnJc.png)

**Location Services**:
Choose whether to enable location services. Enabling this improves convenience but may expose location data.

![](static/T1dUblRAdoQhLZxhOBRccA1Qnnz.png)

**Time Zone**:
Set your time zone. When connected to the internet, the system syncs the time automatically.

![](static/Q5PcbGF1AoYf6gxnOVacglTOnFe.png)

**Username and Password**:
Set your username and password. Remember your password.

![](static/REhUba9TeooKoCxkOpLc9Qfyn6g.png)

![](static/AfF7bNATFoLIVnxGZJDcYdTYnbf.png)

**Setup Complete**

Click "Start Using Bianbu" to enter the desktop.

![](static/B0TFb596NoR2cHxgsF5c7GCvnog.png)

## Flashing Firmware

### Entering Flash Mode

To enter flash mode from a powered-off state:

1. Hold the Flash (download) button without releasing.
2. Plug in the Type-C power cable to power on.
3. Release the Flash button.

If already powered on:

1. Hold the Flash (download) button without releasing.
2. Briefly press the Reset button.
3. Release the Flash button.

(For button locations, see the interface diagram in the Specifications section.)

![](static/CagMb8bMIoBVymxV32qcAbsOnVh.png)

Connect MUSE Card's Type-C port to the host computer via USB and flash using the SpacemiT official flashing tool Titan or the `fastboot` command.

![](static/VT1gb0Rhaox9NyxkXjEcA6VAnRf.png)

### Firmware Download and Installation

#### Bianbu

**About Bianbu**:
Bianbu is an operating system deeply optimized by SpacemiT for RISC-V processors. MUSE Card supports both Bianbu Desktop and Bianbu NAS editions.

**Bianbu website**:
[Bianbu](https://www.spacemit.com/community/document/info?lang=zh&nodepath=software/SDK/bianbu/root_overview.md)

**Bianbu Desktop / NAS firmware download**:
[Index of /image/k1/version/bianbu](https://archive.spacemit.com/image/k1/version/bianbu/)

Firmware packages with "NAS" in the name are Bianbu NAS editions.

**Bianbu installation and upgrade guide**:
[Bianbu User Guide](https://www.spacemit.com/community/document/info?lang=zh&nodepath=software/SDK/bianbu/user_guide)

## Serial Debug

### Connecting the Interface

Connect a USB-to-UART TTL adapter from the host computer to the TX, RX, and GND pins of the MUSE Card debug header:

![](static/AkuNb4lrWoZSK8x4vvYcrbp0nEc.png)

### Windows Debug

Using MobaXterm as an example:

First, connect the serial hardware and confirm the COM port is visible in Windows Device Manager:

![](static/CnbxboUC9ouBwKxXQhFcu7BYnhg.png)

Open MobaXterm, go to Sessions > New Session, select Serial, choose the COM port identified above, set **Speed to 115200**, then click OK to enter the terminal.

![](static/Fsu8b7VnKoeDrMxR2ajcttT8nbf.png)

![](static/UG38b8Wu7oDr28xKbxbc5n5vnHh.png)

## Safety Notes

M1 MUSE Card is intended for lab or engineering environments. Before handling, read the following:

1. Never hot-plug the display connector, CSI connectors, or expansion boards under any circumstances.
2. Before unpacking or installing the board, take appropriate ESD precautions to prevent damage to hardware.
3. Hold the board by its edges; do not touch exposed metal parts to avoid ESD damage to components.
4. Place the board on a dry, flat surface away from heat sources, electromagnetic interference, radiation sources, and EMI-sensitive equipment such as medical devices.
