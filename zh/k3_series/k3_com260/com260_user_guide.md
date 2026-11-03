---
sidebar_position: 3
---

# K3 CoM260 开发套件用户使用指南

## PDF 版本下载

点击下载 **[K3 CoM260 开发套件用户使用指南 (PDF)](https://cdn-resource.spacemit.com/file/product/K3/k3_com260_ug_zh.pdf)**

## 版本

| 版本 | 日期   | 说明 |
|----------|------------|----------|
| V2.1     | 2026.11.03 | 1. 第 2 章产品规格表按核心模组与参考载板重新整理 <br> 2. 修正 RTC 电压范围为 1.85 V ~ 5.5 V <br> 3. 补充 DP 接口使用说明 <br> 4. 统一电源适配器规格描述 |
| V2.0     | 2026.03.19 | 1. 互换UART0 RX与TX的位置 <br> 2. CAM0 调整为 MIPI CSI1 2Lane|
| V1.0     | 2025.11.24 | 首版     |

## 1. 产品简介

### 1.1 概述

本文档主要介绍 **K3 CoM260** 搭配 **K3 CoM260 开发套件** 的基本功能、硬件特性、多功能硬件配置及软件调试操作使用方法，旨在帮助调试人员更快、更准确地使用 K3 CoM260，熟悉 K3 CoM260 模组开发应用方案。

### 1.2 产品版本

本产品对应的产品版本如下：

| 产品名称 | 产品版本 |
| --- | --- |
| K3 CoM260 | K3-CoM260_P1_LP5315B_32X2_v03_20260312 |

## 2. 产品规格

|模块 | 描述 |
|:------|:------|
| 芯片 | SpacemiT K3 RISC-V AI 芯片 |
| CPU | 8 核 X100™ 64 位 RISC-V CPU<br>- 2 Clusters x 4 Cores/Cluster，每个 Cluster 拥有 4MB L2 共享缓存，并可跨 Cluster 访问<br>- 每个 X100 核具有 64KB I-Cache、64KB D-Cache<br>- 支持 RVA23 profile 标准<br>- 支持 RVV1.0，VLEN：256bit |
| AI 性能 | 8 核 A100™ AI 核心，提供 60 TOPS AI 算力<br>- 2 Clusters x 4 Cores/Cluster，每个 Cluster 内拥有 1MB L2 共享缓存和 1.5MB 专用加速缓存（TCM），并可跨 Cluster 访问<br>- 每个 A100 核具有 32KB I-Cache、32KB D-Cache<br>- 支持 RVV1.0，VLEN：1024bit |
| 硬件安全引擎 | 支持国际通用密码算法及中国商用密码算法 <br> - 哈希算法：SHA1 / SHA224 / SHA256、SM3 <br> - 对称加密算法：AES-128/192/256、SM4 <br> - 非对称加密算法：RSA-1024/2048/4096、ECC-128/256/512、SM2 |
| 安全系统方案 | 支持基于 HW-RoT 的 Secure Boot <br> 支持 RISC-V 架构（PMP/IOPMP 隔离机制）的 TEE 可信计算 <br> 支持 OP-TEE 安全操作系统 |
| GPU | 集成 3D-GPU，支持 Vulkan、OpenCL、OpenGLES |
| 内存 | 8GB/16GB/32GB 64 位 LPDDR5、6400MT/s |
| 存储 | 支持内部 UFS、SD 卡插槽及外置 NVMe |
| 视频编码 | 4K60（H.264/H.265） |
| 视频解码 | 1 x 4K120 (H.264/H.265/VP9)<br>2 x 4K60 (H.264/H.265/VP9)<br>8 x 1080p60 (H.264/H.265/VP9)<br>16 x 1080p30 (H.264/H.265/VP9) |
| 功耗 | 18W ~ 35W |

**参考载板**

|模块 | 描述 |
|:------|:------|
| 摄像头接口 | 2 x MIPI CSI-1.1 22 针摄像头连接器 |
| PCIe 接口 | M.2 Key M 插槽（支持 PCIe Gen3 ×4）<br>M.2 Key M 插槽（支持 PCIe Gen3 ×1）<br>M.2 Key E 插槽 |
| USB 接口 | USB Type-A 接口：4 × USB 3.0<br>USB Type-C 接口 |
| 网络接口 | 1 x 千兆以太网接口 |
| 显示接口 | 1 x DP 1.2 接口<br>1 x MIPI DSI-1.2 30 针显示屏连接器 |
| 其他 I/O 接口 | 40 针扩展接口（支持 UART、SPI、I2S、I2C、GPIO）<br>12 针按钮接口<br>4 针风扇接口<br>直流电源接口 |
| 机械尺寸 | 103mm x 90.5mm x 35mm (高度包含脚垫、载板、模块及散热方案) |

## 3. 系统概述

### 3.1 K3 芯片概述

K3 是进迭时空推出的新一代高性能 RISC-V AI CPU 芯片，具有以下特点：

- 8 个高性能计算大核 X100，最大主频 2.4 GHz，130K DMIPS 算力，单核 Specint2006 > 9.0/GHz  
- 60 TOPS AI 算力  
- 集成多套高速扩展接口：8 lanes PCIe、4 套 USB 3.0、4 套 GMAC 等

### 3.2 K3 芯片框图

![K3 芯片框图](./static/k3-com260_block_diagram.png)

### 3.3 K3 CoM260 参考方案框图

#### 3.3.1 参考方案框图

K3 CoM260 系统方案具备以下特性：

- 基于 K3 芯片构建；
- 采用 P1 PMIC + 外挂 DC-DC 的供电方案；
- DRAM 采用 2 × LPDDR5 与 UFS2.2；
- 外设接口包括：
  - 7 lanes PCIe 3.0  
  - 3 套 USB 3.0  
  - 1 套 GMAC
  - TF Card 等接口  
  
整体方案稳定可靠，具备量产应用能力。

参考方案框图如下：
![K3 CoM260 参考方案框图](./static/com260_solution00.png)

#### 3.3.2 功能概述

K3 CoM260 开发套件提供以下功能：

- **Type-C**：1 路 USB 3.0 Type-C UFP 接口，系统固件升级通道  
- **DP**：1 路 DP 1.2 Type-A 接口，最大支持 3840 × 2160 @ 60fps 输出  
- **MIPI DSI**：1 个 30 Pin FPC 连接器，1 路 2 Lane MIPI DSI 信号支持 LCD 屏，1 路 I2C 信号支持 CTP 屏  
- **MIPI CSI**：2 个 22 Pin FPC 连接器，2 路 MIPI CSI 信号可支持 2 个摄像头  
- **40 Pin 双排插针**：兼容树莓派标准 40 Pin 双排插针，支持 I2C、UART、SPI、I2S 和 GPIO 调试  
- **SD-Card**：支持高速 TF 卡  
- **PCIe Wi-Fi**：1 个 M.2 E-Key 连接器，模组型号为 RTL8852BE，外置 SMA 天线，支持无线上网功能  
- **Ethernet**：1 路 RJ45 连接器，自适应 10/100/1000M 以太网  
- **PCIe 3.0**：2 个 M.2 M-Key 连接器，可接入 2280、2230 SSD  
- **USB 3.0 Type-A**：2 个 USB 3.0 Type-A Dual 连接器，用于扩展 USB 设备  
- **12 Pin 按钮排针**：用于连接 LED、UART Debug、ACOK、开关机、复位按钮  
- **FAN**：1 个 4 Pin 风扇连接器，可连接 4 线可调速风扇  
- **CAN**：1 个 4 Pin 排针，集成 CAN 收发器，可连接 CAN 设备  
- **RTC**：1 个 2 Pin 线对板连接器，支持 1.85 V ~ 5.5 V 电压输入

#### 3.3.3 功能接口

| 功能                     | 可用（是/否）     |
|--------------------------|--------------|
| 2×LPDDR5 (4GB/8GB/16GB) | 是           |
| UFS (128GB)              | 是           |
| SPI FLASH                | 是           |
| DC Jack                  | 是           |
| DP 1.2 OUT               | 是           |
| MIPI DSI                 | 是           |
| MIPI CSI                 | 是           |
| SD-Card                  | 是           |
| Wi-Fi & BT               | 是           |
| Gbe                      | 是           |
| 2 × M.2 M-KEY            | 是           |
| 2 × USB 3.0 Type-A Dual  | 是           |
| 40 Pin                   | 是           |
| 12 Pin                   | 是           |
| FAN                      | 是           |
| CAN                      | 否   |
| RTC                      | 否   |

## 4. 硬件介绍

### 4.1 实物图

![K3 CoM260 开发套件实物图](./static/com260-kit_00.png)

### 4.2 电源框图

![电源框图 1](./static/power00.png)  
![电源框图 2](./static/power01.png)

### 4.3 Boot Download Sel & JTAG Sel

Boot Download Sel 与 JTAG Sel 示意图如下。

![Boot Download Sel 与 JTAG Sel 示意图](./static/debug.png)

### 4.4 I2C 地址

K3 CoM260 预留了丰富的外围接口。在调试 I2C 外设时，可能涉及 I2C 通道复用。下图列出了 K3 CoM260 开发套件对应的 I2C 地址及上拉电源配置，以避免地址冲突和电平不匹配。

![I2C 地址与上拉电源示意图](./static/i2c.png)

## 5. 模块简述

### 5.1 电源输入

K3 CoM260 开发套件仅提供 DCIN 一种电源输入方式，板载 DC Jack 接口规格为外径 6.3 mm、内径 2.5 mm，需搭配支持 19 V/2.37 A 或 12 V/5 A 输出的 DC Jack 电源适配器。

### 5.2 存储器

K3 CoM260 模组集成了以下 4 类存储器：

1. **UFS2.2**：模组板载 UFS 存储，默认容量为 128 GB。  
2. **SPI Flash**：板载 SPI Flash。  
3. **DDR**：采用 2 颗 LPDDR5 芯片，单颗容量可选 4 GB / 8 GB / 16 GB，对应模组总容量为 8 GB / 16 GB / 32 GB。  
4. **EEPROM**：用于存储板卡信息。

### 5.3 按键输入

K3 CoM260 开发套件提供多功能按键接口，包括电源按键、复位按键和下载按键。

![按键接口示意图](./static/Input_keys.png)

| Pin | 信号名称         | Function             |
|-----|------------------|----------------------|
| 1   | PC_LED-          | LED 负极             |
| 2   | PC_LED+          | LED 正极             |
| 3   | UART0_RXD        | DEBUG UART RX        |
| 4   | UART0_TXD        | DEBUG UART TX        |
| 5   | BMCU_ACOK        | 设置为按键开机       |
| 6   | AUTO_ON_DIS      | 与 BMCU_ACOK 短接，设置为按键开机   |
| 7   | GND              | 电源地               |
| 8   | PMIC_RST_OUTn    | 复位                 |
| 9   | Gnd              | 电源地               |
| 10  | FORCE_RECOVERY   | Download             |
| 11  | Gnd              | 电源地               |
| 12  | SLEEP/WAKE       | 开机/关机            |

### 5.4 MIPI CSI 高速连接器

K3-CoM260 不限定支持特定型号的摄像头模组。其高速连接器提供两组 4 Lane MIPI CSI 信号，并可通过模组上的电阻配置灵活选择不同的链路组合模式。

默认配置下，
- CAM0 支持 2 lanes
- CAM1 支持 2+2 lanes 或 4 lanes

![MIPI CSI 高速连接器示意图](./static/MIPI_CSI.png)

**22 Pin 高速连接器接口线序如下：**

**CAM0**

| Pin | 信号名称          |
|-----|-------------------|
| 1   | VDD_3V3_SYS       |
| 2   | I2C4_SDA           |
| 3   | I2C4_SCL           |
| 4   | GND               |
| 5   | CLK_CAMCK         |
| 6   | CAM_PWDN          |
| 7   | GND               |
| 8   | MIPI_CSI0_DP1     |
| 9   | MIPI_CSI0_DN1     |
| 10  | GND               |
| 11  | MIPI_CSI0_DP0     |
| 12  | MIPI_CSI0_DN0     |
| 13  | GND               |
| 14  | MIPI_CSI1_CLKP    |
| 15  | MIPI_CSI1_CLKN    |
| 16  | GND               |
| 17  | MIPI_CSI1_DP1     |
| 18  | MIPI_CSI1_DN1     |
| 19  | GND               |
| 20  | MIPI_CSI1_DP0     |
| 21  | MIPI_CSI1_DN0     |
| 22  | GND               |

**CAM1**

| Pin | 信号名称         |
|-----|------------------|
| 1   | VDD_3V3_SYS      |
| 2   | I2C4_SDA         |
| 3   | I2C4_SCL         |
| 4   | GND              |
| 5   | CLK_CAMCK        |
| 6   | CAM_PWDN         |
| 7   | GND              |
| 8   | MIPI_CSI3_DP1    |
| 9   | MIPI_CSI3_DN1    |
| 10  | GND              |
| 11  | MIPI_CSI3_DP0    |
| 12  | MIPI_CSI3_DN0    |
| 13  | GND              |
| 14  | MIPI_CSI2_CLKP   |
| 15  | MIPI_CSI2_CLKN   |
| 16  | GND              |
| 17  | MIPI_CSI2_DP1    |
| 18  | MIPI_CSI2_DN1    |
| 19  | GND              |
| 20  | MIPI_CSI2_DP0    |
| 21  | MIPI_CSI2_DN0    |
| 22  | GND              |

### 5.5 MIPI DSI 屏连接器

K3 CoM260 支持树莓派 4.3 英寸电容触摸显示屏。

![MIPI DSI 屏连接器示意图](./static/MIPI_DSI.png)

**屏接口线序如下：**

| Pin | 信号名称             | 信号名称             | Pin |
|-----|----------------------|----------------------|-----|
| 1   | GND                  | GND                  | 2   |
| 3   | MIPI_DSI1_LANE1_DN   | MIPI_DSI1_LANE1_DN   | 4   |
| 5   | MIPI_DSI1_LANE1_DP   | MIPI_DSI1_LANE1_DP   | 6   |
| 7   | GND                  | GND                  | 8   |
| 9   | MIPI_DSI1_CLK_N      | MIPI_DSI1_CLK_N      | 10  |
| 11  | MIPI_DSI1_CLK_P      | MIPI_DSI1_CLK_P      | 12  |
| 13  | GND                  | GND                  | 14  |
| 15  | MIPI_DSI1_LANE0_DN   | MIPI_DSI1_LANE0_DN   | 16  |
| 17  | MIPI_DSI1_LANE0_DP   | MIPI_DSI1_LANE0_DP   | 18  |
| 19  | GND                  | GND                  | 20  |
| 21  | I2C3_SCL             | I2C3_SCL             | 22  |
| 23  | I2C3_SDA             | I2C3_SDA             | 24  |
| 25  | GND                  | GND                  | 26  |
| 27  | LCD_VCC33            | LCD_VCC33            | 28  |
| 29  | LCD_VCC33            | LCD_VCC33            | 30  |

### 5.6 Type-C 连接器

K3 CoM260 开发套件的 Type-C 连接器仅支持 OTG 模式，不支持对内供电。

![Type-C 连接器示意图](./static/Type-C.png)

### 5.7 DP 输出接口

K3 CoM260 开发套件支持 1 路 DP Type-A 输出接口，最高支持 DP 1.2，最大支持 3840 × 2160 @ 60fps 视频输出。

![DP 输出接口示意图](./static/DP.png)

DP 显示使用说明：
- K3 CoM260 开发套件仅支持 DP 显示输出（不支持 HDMI），请使用 DP 线缆连接支持 DP 输入的显示器，方可正常点亮屏幕。
- 如需连接 HDMI 显示器，请选用主动式 DP 转 HDMI 转换器（内置 DP 转 HDMI 转换芯片）；被动式 DP 转 HDMI 转接线无转换芯片，无法使用。参考链接：[DP 转 HDMI 主动式转换器](https://item.jd.com/100026235280.html)

> 注意：其他开发平台随附的 DP 转 HDMI 线缆多为被动式，内部无协议转换芯片，与本套件的 DP 接口配合使用时无法正常出图。请勿直接复用其他平台随附的显示线缆，请按上述要求自行选配主动式转换器。

### 5.8 USB 接口

K3 CoM260 开发套件提供 4 路 USB 3.0 Type-A 接口，便于连接各类 USB 外设。

![USB 接口示意图](./static/USB.png)

### 5.9 RJ45 接口

K3 CoM260 开发套件支持 1 个 RJ45 千兆网接口。

![RJ45 接口示意图](./static/RJ45.png)

### 5.10 Wi-Fi/BT 模组

K3 CoM260 开发套件支持接入 M.2 2230 E-Key 模组，可实现无线网络和蓝牙功能。

![Wi-Fi/BT 模组示意图](./static/BT.png)

### 5.11 40 Pin 接口

K3 CoM260 开发套件提供 40 Pin 双排插针接口，线序如下：

![40 Pin 接口线序图](./static/40Pin.png)  

> 注：IO Function 可根据需求自行配置。

| Pin | 信号名称          | 信号名称          | Pin |
|-----|-------------------|-------------------|-----|
| 1   | VDD_3V3_SYS       | VDD_5V_GPIO       | 2   |
| 3   | I2C3_SDA          | VDD_5V_GPIO       | 4   |
| 5   | I2C3_SCL          | GND               | 6   |
| 7   | GPIO09            | UART1_TXD_LS      | 8   |
| 9   | GND               | UART1_RXD_LS      | 10  |
| 11  | UART1_RTS_LS      | I2S0_SCLK_LS      | 12  |
| 13  | R-SPI0_SCK_LS     | GND               | 14  |
| 15  | GPIO12_LS         | R-SPI0_CS1_LS     | 16  |
| 17  | VDD_3V3_SYS       | R-SPI0_CS_LS      | 18  |
| 19  | SPI0_MOSI_LS      | GND               | 20  |
| 21  | SPI0_MISO_LS      | R-SPI0_MISO_LS    | 22  |
| 23  | SPI0_SCK_LS       | SPI0_CS0_LS       | 24  |
| 25  | GND               | SPI0_CS1_LS       | 26  |
| 27  | I2C0_SDA          | I2C0_SCL          | 28  |
| 29  | GPIO01_LS         | GND               | 30  |
| 31  | GPIO11_LS         | GPIO07_LS         | 32  |
| 33  | GPIO13_LS         | GND               | 34  |
| 35  | I2S0_LRCK_LS      | UART1_CTS_LS      | 36  |
| 37  | R-SPI0_MOSI_LS    | I2S0_SDIN_LS      | 38  |
| 39  | GND               | I2S0_SDOUT_LS     | 40  |

### 5.12 TF-Card 接口

K3 CoM260 支持 TF 卡接入，便于扩展存储设备。同时支持 Debug 扩展卡，用于 JTAG 调试。

![TF-Card 接口示意图](./static/TF-Card.png)

### 5.13 M.2 M-Key 接口

K3 CoM260 开发套件提供 2 × M.2 M-Key 接口，分别支持 2280（图中较长 SSD）和 2230（图中较短 SSD）规格的 NVMe SSD，便于接入 SSD 及其他 M.2 M-Key 设备。

![M.2 M-Key 接口示意图](./static/M2_M-Key.png)

### 5.14 CAN FD 接口

K3 CoM260 开发套件板载 CAN 收发器，可直接连接 CAN 设备。

![CAN FD 接口示意图](./static/can_fd.png)

## 6. 初次设置

### 6.1 使用前准备

#### 6.1.1 电源适配器

K3 CoM260 开发套件采用 DCIN 供电，需搭配输出规格为 19 V/2.37 A 或 12 V/5 A 的 DC Jack 电源适配器，接口及适配器详细要求参见 [5.1 电源输入](#51-电源输入)。

#### 6.1.2 键盘和鼠标

您可以使用 K3 CoM260 开发套件上的任一 USB-A 端口连接有线键盘、鼠标或 USB 接收器，也可以通过蓝牙方式连接键盘和鼠标。

当 USB 3.0 设备与使用 2.4GHz 无线接收器的键鼠同时接入相邻的 USB 3.0 接口时，键鼠可能会出现输入卡顿或延迟。这是由于 USB 3.0 高速传输可能对 2.4GHz 无线信号产生干扰，属于较为常见的物理现象。

如果您遇到此类情况，建议使用 USB 延长线将无线接收器引出，使其远离 USB 3.0 设备，以降低信号干扰并提升无线连接的稳定性。

#### 6.1.3 显示器

K3 CoM260 需配合外接显示器输出画面。产品支持 DP 和 MIPI DSI 视频接口，因此可连接一种或同时连接两种对应接口的显示器。  

> **注意**：若需通过 MIPI DSI 接口输出画面，请务必在开机前完成显示器与 K3 CoM260 之间的视频线连接。K3 CoM260 的 MIPI DSI 接口 **不支持热插拔**。

#### 6.1.4 网络连接

K3 CoM260 支持有线 RJ45 网络连接，您可以直接接入网线。  
同时，K3 CoM260 也支持 Wi-Fi 和蓝牙无线连接；如需增强信号，可安装外接天线。

### 6.2 开始启动

请按以下步骤完成设备上电前的连接：

- 使用视频线将设备连接至显示器，并接入键盘和鼠标。
- 最后连接电源线并上电开机。
  - 首次通电：设备自动开机。
  - 软件关机后：需短按电源按钮以重新开机。

设备启动后：

- K3 CoM260 开发套件上的红色电源指示灯将点亮；
- K3 CoM260 模组的散热风扇开始运转。

### 6.3 首次启动时配置您的 K3-CoM260

K3 CoM260 出厂时预装进迭时空 Bianbu 操作系统。设备首次启动时将自动运行配置向导，您需要通过显示器、键盘和鼠标完成相关配置。

详细配置说明请参考 [LXQt 首次启动与会话](https://spacemit.com/community/document/info?lang=zh&nodepath=software/SDK/bianbu/user_guide/LXQt/initial_setup_and_sessions.md)。

## 7. 刷机

### 7.1 进入刷机模式

进入刷机模式前，请准备两个按键，分别用于短接 FC_REC 与 GND、SYS_RST 与 GND。

1. **设备处于断电状态时**
   1. 按住 FC_REC 按键不松开。
   2. 接入电源适配器，为设备上电。
   3. 松开 FC_REC 按键。
   4. 使用 Type-C 数据线连接开发板 Type-C 接口与上位机电脑。
   5. 使用进迭时空刷机工具 Titan 或执行 `fastboot` 命令进行烧录。
2. **设备已上电并处于开机状态时**
   1. 按住 FC_REC 按键不松开。
   2. 短按 RST 按键。
   3. 松开 FC_REC 按键。
   4. 使用 Type-C 数据线连接开发板 Type-C 接口与上位机电脑。
   5. 使用进迭时空刷机工具 Titan 或执行 `fastboot` 命令进行烧录。

![进入刷机模式按键连接示意图](./static/Input_keys.png)

刷机流程请参考 [刷机工具使用手册](https://www.spacemit.com/community/document/info?lang=zh&nodepath=tools/user_guide/flasher_user_guide.md)。

### 7.2 固件下载和安装

**Bianbu** 是进迭时空面向 RISC-V 架构处理器深度优化的操作系统。

点击 [K3 Bianbu](https://spacemit.com/community/resources-download/Images%20Collects/K3/Bianbu) 获取安装包。

## 8. 串口调试

### 8.1 接口连接

请将上位机通过 USB 转 TTL 设备与 K3-CoM260 载板 12 Pin 接口的 TX、RX、GND 正确连接。接口信号如下图所示：

![串口接口连接示意图](./static/serial.png)

### 8.2 Windows 调试

以下以 MobaXterm 为例说明操作步骤：

请先正确连接硬件串口，并在 Windows 设备管理器的“端口”中确认系统已识别对应的 COM 口（如图所示）。
![Windows 设备管理器串口识别示意图](./static/port.png)

1. 打开 MobaXterm 软件，依次选择 **Sessions → New Session**。  

   ![MobaXterm 新建串口会话示意图](./static/mobaxterm.png)
  
2. 在弹出的对话框中，选择 **Serial**。  

3. 在 **Serial port** 下拉菜单中，选择已识别的 COM 口。  

4. 将 **Speed** 设置为 **115200**。  

5. 点击 **OK**，进入串口日志输出页面。

## 9. 注意事项

K3 CoM260 适用于实验室或工程环境。开始操作前，请仔细阅读以下注意事项：

1. 任何情况下不可对屏幕接口、CSI 接口及扩展板进行热插拔操作。  
2. 拆封包装和安装前，为避免静电释放（ESD）对开发板硬件造成损伤，请采取必要的防静电措施。  
3. 拿取开发板时，请握持板边，避免触碰板上的外露金属部分，以免静电损坏板上元器件。  
4. 请将开发板放置于干燥、平整的表面，并确保其远离热源、电磁干扰源、辐射源以及电磁辐射敏感设备（如医疗设备）等。
