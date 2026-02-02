sidebar_position: 1

# K3 Pico-ITX 简介

**[PDF 版本](https://cdn-resource.spacemit.com/file/%E7%94%9F%E6%80%81%E4%BA%A7%E5%93%81/K3%20Pico-ITX%282.5%27%27%20AI%20SBC%29ZH_0202.pdf)**

MUSE Pico 为60TOPS算力的单板计算机，8计算核和8智算核统一内存架构，板载UFS高速硬盘和万兆网络光通讯接口，充分释放算力性能，提高科学计算、人工智能等应用处理效率。MUSE Pico为2.5" Pico-ITX plus尺寸，满足各行业紧凑型场景应用。单板支持双M.2扩展槽位，具备实时运动控制和系统管理接口。凭借其丰富的接口扩展性与工业架构式设计，可支持行业解决方案提供商开展快速评估与系统集成工作，推动产品商业化落地进程。

## 特性

- 符合RVA23标准的8核处理器K3，60TOPS通用AI算力，支持IME扩展和完整虚拟化
- 计算核和智算核统一内存架构，支持300亿参数模型部署
- 板载UFS本地存储，比行业板载EMMC提升3.4倍速率
- M.2 B-KEY和M-KEY双扩展槽位，其中M-KEY采用4lane PCIE GEN3，可扩展全链路NVMe SSD
- 板载万兆PCIE以太网，支持10G-BASE-R光纤接口，实现低延迟、高吞吐的数据传输，支持集群化部署
- 全功能typeC接口，支持65W PD协议供电和4K DP显示，仅需一根线缆，即刻点亮算力
- 板载行业应用高清屏幕EDP接口，支持屏显产品系统集成
- 实时核RT24直出的柔性扩展IO插槽，支持ethercat、CAN-FD等接口，满足微秒级运动控制和机器人等应用
- MUSE系列架构设计，冷热分层，最佳CPU算力性能释放

## 产品规格

|模块 | 描述 |
|------|------|
| 处理器 | 处理SpacemiT K3，8核，2.4GHz，融合60TOPS AI算力，符合RVA23标准，支持IME向量扩展和完整虚拟化器 |
| 显示   | DP Type-C接口，最高支持4K 3840x2160分辨率，60Hz刷新率<br>40PIN EDP接口，最高支持2.5K 2560x1600分辨率，90Hz刷新率 |
| 内存   | 双通道 2x32bit LPDDR5，6400MT/s速率，可选16GB/32GB容量 |
| 本地存储 | UFS2.2，可选128GB/256GB容量 |
| 存储扩展 | M.2 M-Key连接器，可装配2280尺寸NVMe SSD，PCIe GEN3 X4信号链路 |
| 高速扩展 | M.2 B-Key连接器，可装配2242/3042尺寸扩展卡，PCIe GEN3 X2及USB信号* |
| 实时扩展 | FPC连接器，支持ethercat、5路CAN-FD、SPI、I2C和UART等实时信号扩展 |
| 无线通讯 | 板载PCIe WIFI6BT5.2模组，符合802.11a/b/g/n/ac/ax标准，双天线双频率 |
| 有线网络 | 支持一路以太网，RJ45接口，1000M/100M自适应速率 |
| 光纤网络 | 支持万兆以太网，SFP+接口，支持10G BASE-R和10G BASE-X，支持QinQ，MSI-X，WOL等网络特性 |
| 音频接口 | 板载CODEC电路，支持音频输入输出板内接口 |
| USB接口 | 2路USB3.2GEN1 Type-C 接口，其中一路为全功能，一路为OTG;<br>4路USB2.0 Type-A HOST接口; |
| 调试接口 | 支持UART和JTAG接口，附带3个侧边按键，用于开关机，复位和固件烧写升级 |
| 管理系统 | 板载EC管理系统，支持电源管理、智能散热策略和系统状态管理，板内支持I2C/UART/GPIO扩展接口 |
| 外观形态 | 100mm x 86mm，单板计算机Pico-ITX plus尺寸，约为2.5寸硬盘大小 |
| 操作系统 | 预装Bianbu 3.0，支持Ubuntu26.04、OpenHarmony6.0、OpenKylin、Deepin、Fedora等操作系统 |
| 电源输入 | 支持双Type-C 口 USB-PD协议，额定输入65W功率，板上ATX 2PIN电源输入端支持12V@7A供电 |
| 可靠性   | 单板形态外设接口ESD可防护接触±4kV，空气±8kV；整机形态ESD可防护接触±6kV，空气±12kV<br>满足CCC、CE、FCC等电磁兼容认证标准，可选消费级-20℃～70℃或工业级-40℃～85℃ |
| 时钟     | 板载RTC时钟电源接口，支持安装电池，满足G3状态供电 |
| 结构     | 可选配单板或配带风冷风扇的散热器套装 <br>可选配单板或自研全金属工业机箱<br>可选配实时扩展板、触摸屏或工业接线端子多种配置 |

> ***注：** M.2 B-Key连接器安装 PCIe 设备时, B-Ke 的 2lane-PCIe 与 M-Key 复用, M.2M-Key 插槽为 PCIe GEN3X2 信号链路

## 框图

![](./static/pico_bd.png)

## 可选配部件

| 类别       | 名称             | 描述       | 与主板的接口         |
|------------|------------------|---------------|----------------------|
| 外设部件   | 固态硬盘         | 980 NVMe™ M.2 固态硬盘, PCIe Gen 3.0 x4, <br>NVMe 1.4, 顺序读取高达 3,500 MB/s, 顺序写入达 3,000 MB/s       | M.2 M-KEY 2280       |
| 外设部件   | 固态硬盘         | B+M NVMe SSD 128GB       | M.2 B-KEY 2242       |
| 外设部件   | 4G 模组           | EM05     | M.2 B-KEY 3042       |
| 外设部件   | SATA 扩展卡       | PCIE 转 5x SATA 接口       | M.2 M-KEY 2280       |
| 外设部件   | 扩展坞           | 扩展坞 Type-C 转 HD 高清 4K 投屏 PD 充电 usb3.0 平板笔记本 3 合 1   | 全功能 Type-C  |
| 外设部件   | 超清屏           | 16 寸 2.5K 90Hz 2560 x 1600 LCD    | EDP 40PIN            |
| 外设部件   | 实时控制扩展板   | 19V 输入，5 路 CAN-FD，EtherCAT，RS232 和 RS485 等 IO，工业级隔离防护   | FPC     |
| 结构配件   | 嵌入风扇式散热器 | 自研铝制      | FAN   |
| 结构配件   | 金属机箱         | 120 x 120 x48mm 自研金属机箱   | BTN   |

## 合作与采购咨询

- **商务微信**：SpacemiT1102
- **商务电话**：+86 189 6649 8607
- **商务邮箱**：[business@spacemit.com](mailto:business@spacemit.com)