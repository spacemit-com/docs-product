sidebar_position: 1

# K3 CoM260 Kit 简介

**[PDF 版本](https://cdn-resource.spacemit.com/file/product/K3/K3-CoM260_brief_zh.pdf)**

**全球首款RVA23标准的RISC-V AI CPU开发平台**

**RISC-V 加速端侧AI智能体构想变为现实**

SpacemiT K3-CoM260 开发者套件提供高达 60 TOPS 的通用 AI 算力，可流畅运行300 亿（30B）参数规模的大模型（如 30B-A3B 模型），为开发者、学生及创客群体提供了极致便捷且用户友好的开发平台。
开发者套件含一块 K3-CoM260 32GB 核心模组和一块通用参考载板，后者可兼容所有 K3-CoM260 系列模组，提供最便捷的端侧AI智能体开发案例。
K3-CoM260 32GB 模组集成 8 核 X100™ 通用CPU + 8 核 A100™ AI CPU，提供 130 KDMIPS 的通用计算能力和60TOPS通用AI算力，实测推理速度超过 10Tokens/秒 @30B，支持多路并发 AI 应用流水线与高性能推理任务；载板提供丰富的接口资源，硬件完美兼容Jetson Orin Nano。
SpacemiT K3-CoM260 开发者套件全面支持各类 AI 算法与模型部署，遵循标准 CPU 编程范式，提供 AI 与系统软件、开发者工具链，实现 AI 算法的“零成本迁移”。我们可进一步提供定制化软件开发服务，并协助集成摄像头、传感器、载板设计及整机工程化服务，加速您的产品落地。
SpacemiT K3-CoM260 开发者套件作为全球第一款支持RVA23标准的 RISC-V 架构的紧凑型边缘计算平台，适用于 AI 一体机、服务机器人及其他端侧推理自主智能体。

## 特性

- **K3-CoM260 开发套件包含：**
  - K3-CoM260 核心模组（含散热片）及参考载板
  - 直流电源适配器
  - 快速入门指南

- **K3-CoM260 32GB 核心模组**
  - 8 核 X100™ 64 位 RISC-V CPU
    - 四发射乱序12级流水
    - 符合RVA23标准
    - 共享8MB L2 Cache
  - 8 核 A100™ 64 位 AI CPU
    - 提供60 TOPS 通用AI算力
    - 1024bit RVV1.0并行计算长度
    - 共享2MB L2 +3MB TCM
  - 32GB 64 位 LPDDR5 内存 6400MT/s
  - 支持外接 NVMe 存储设备

- **参考载板**
  - 2 x MIPI CSI-1.1 22 针摄像头连接器
  - 2 x M.2 Key M, M.2 Key E
  - 4 x USB 3.0 Type-A
  - USB Type-C（支持 UFP 设备模式）
  - 千兆以太网口
  - DisplayPort 显示接口
  - 40-pin 针扩展排针
  - MIPI DSI 30 针连接器
  - 直流电源接口

## 产品规格

**K3-CoM260 32GB 模组**

|模块 | 描述 |
|------|------|
| 芯片 | SpacemiT K3 RISC-V AI 芯片 |
| CPU | 8 核 X100™ 64 位 RISC-V CPU，主频 2.4GHz<br>- 2 Clusters x 4 Cores/Cluster，每个 Cluster 拥有 4MB L2 共享缓存，并可跨 Cluster 访问<br>- 每个 X100 核具有 64KB I-Cache、64KB D-Cache<br>- 支持 RVA23 profile 标准<br>- 支持 RVV1.0，VLEN：256bit |
| AI 性能 | 8 核 A100™ AI 核心，提供 60 TOPS AI 算力<br>- 2 Clusters x 4 Cores/Cluster，每个 Cluster 内拥有 1MB L2 共享缓存和 1.5MB 专用加速缓存（TCM），并可跨 Cluster 访问<br>- 每个 A100 核具有 32KB I-Cache、32KB D-Cache<br>- 支持 RVV1.0，VLEN：1024bit |
| GPU | 集成 3D-GPU，支持 Vulkan、OpenCL、OpenGLES |
| 内存 | 8GB/16GB/32GB 64 位 LPDDR5、6400MT/s |
| 存储 | 支持内部 UFS、SD 卡插槽及外置 NVMe |
| 视频编码 | 4K60（H.264/H.265） |
| 视频解码 | 1 x 4K120 (H.264/H.265/VP9)<br>2 x 4K60 (H.264/H.265/VP9)<br>8 x 1080p60 (H.264/H.265/VP9)<br>16 x 1080p30 (H.264/H.265/VP9) |
| 功耗 | 18W–25W |

> 支持的功能列表请参阅最新版 SpacemiT K3 Datasheet 中的“软件特性”章节。

**参考载板**

|模块 | 描述 |
|------|------|
| 摄像头接口 | 2 x MIPI CSI-1.1 22 针摄像头连接器 |
| PCIe 接口 | M.2 Key M 插槽（支持 PCIe Gen3 ×4）<br>M.2 Key M 插槽（支持 PCIe Gen3 ×1）<br>M.2 Key E 插槽 |
| USB 接口 | USB Type-A 接口：4 × USB 3.0<br>USB Type-C 接口（支持 UFP 模式） |
| 网络接口 | 1 x 千兆以太网接口 |
| 显示接口 | 1 x DP 1.2 接口<br>1 x MIPI DSI-1.2 30 针显示屏连接器 |
| 其他 I/O 接口 | 40 针扩展接口（支持 UART、SPI、I2S、I2C、GPIO）<br>12 针按钮接口<br>4 针风扇接口<br>直流电源接口 |
| 机械尺寸 | 103mm x 90.5mm x 34.77mm<br>(高度包含脚垫、载板、模块及散热方案) |


## 合作与采购咨询

- **商务微信**：SpacemiT1102
- **商务电话**：+86 189 6649 8607
- **商务邮箱**：[business@spacemit.com](mailto:business@spacemit.com)