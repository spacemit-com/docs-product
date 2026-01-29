sidebar_position: 1

# K3 CoM260 Kit Brief

**[PDF Version](https://cdn-resource.spacemit.com/file/%E8%8A%AF%E7%89%87/K3/K3-CoM260_EN_0126.pdf)**

**The World’s 1st RISC-V AI CPU Platform Compliant with the RVA23 Standard**

**Turn Your RISC-V Edge-AI Agent Ideas Into Reality**

The SpacemiT K3-CoM260 delivers up to 60 TOPS of general-purpose AI compute and can smoothly run 30-billion-parameter (30B) large models, such as the 30B-A3B series. It offers highly accessible, user-friendly development environment for developers, students, and makers.
The developer kit includes a K3-CoM260 32GB core module and a universal reference carrier board. The carrier board is fully compatible with  K3-CoM260 series and provides ready-to-use demos for edge AI agent development.
The K3-CoM260 32GB module integrates 8x100™ general-purpose CPU cores and 8x A100™ AI CPU cores, delivering 130 KDMIPS of general compute and 60 TOPS of general AI compute. Real-world testing shows inference performance is greater than 10 Tokens/S@30B. It supports multi-pipeline concurrent AI workloads and high-performance inference tasks. And the included carrier board offers a wide range of I/O interfaces while remaining hardware-compatible with NVIDIA Jetson Orin Nano to simplify hardware migration.
The SpacemiT K3-CoM260 Developer Kit supports deployment of a broad set of AI algorithms and model types. It follows a standard CPU programming model and provides system software, AI runtime, and a complete developer toolchain, enabling zero-effort migration of existing AI workloads.
SpacemiT also provides custom software development services, along with support for camera and sensor integration, carrier-board design, and full system engineering to accelerate productization.
As the world’s first compact edge-computing platform based on the RISC-V architecture with full RVA23 support, the SpacemiT K3-CoM260 Developer Kit is ideal for AI edge devices, service robots, and a wide range of autonomous on-device AI agent applications.

## Key Features

- **K3-CoM260-Kit Includes:**
  - K3-CoM260 Module with heatsink and reference carrier board
  - DC power supply
  - Quick Start Guide

- **K3-CoM260 32GB Core Module**
  - 8 x X100™ 64-bit RISC-V CPU cores
    - 4-issue out-of-order pipeline, 12 stages
    - Compliant with the RVA23 specification
    - Shared 8 MB L2 cache
  - 8 x A100™ 64-bit AI CPU cores
    - 60 TOPS general-purpose AI compute
    - 1024-bit RVV 1.0 vector processing width
    - Shared 2 MB L2 + 3 MB TCM
  - 32 GB 64-bit LPDDR5, 6400 MT/s
  - Support for external NVMe storage devices

- **Reference Carrier Board**
  - 2 x MIPI CSI-1.1 (22-pin) camera connectors
  - 2 x M.2 Key M, M.2 Key E
  - 4 x USB 3.0 Type-A
  - USB Type-C for UFP 
  - Gigabit Ethernet port
  - DisplayPort 
  - 40-pin expansion header
  - MIPI DSI (30-pin) connector
  - DC power input

## Specification

**K3-CoM260 32GB Moudle**

|Module | Description |
|------|------|
| Chip | SpacemiT K3 RISC-V AI CPU |
| CPU | 8 x X100™ 64-bit RISC-V CPU cores, 2.4 GHz<br>- 2 clusters x 4 cores per cluster, each cluster includes 4 MB shared L2 cache, with cross-cluster access<br>- Each X100 core includes 64 KB I-cache and 64 KB D-cache<br>- Compliant with the RVA23 profile<br>- Supports RVV 1.0, VLEN: 256 bits |
| AI Performance | 8 x A100™ AI CPU cores, delivering 60 TOPS<br>- 2 clusters x 4 cores per cluster, each cluster includes 1 MB shared L2 cache and 1.5 MB TCM (Tightly Coupled Memory), with cross-cluster access<br>- Each A100 core includes 32 KB I-cache and 32 KB D-cache<br>- Supports RVV 1.0, VLEN: 1024 bits |
| GPU | Integrated 3D GPU, with support for Vulkan, OpenCL, and OpenGL ES |
| Memory | 8GB/16GB/32GB 64-bit LPDDR5, 6400MT/s |
| Storage | Supports internal UFS, SD card slot, and external NVMe |
| Video Encoding | 4K60 (H.264/H.265) |
| Video Decoding | 1x 4K120 (H.264/H.265/VP9)<br>2x 4K60 (H.264/H.265/VP9)<br>8x 1080p60 (H.264/H.265/VP9)<br>16x 1080p30 (H.264/H.265/VP9) |
| Power Consumption | 18W–25W |

> Refer to the Software Features section of the latest SpacemiT K3 Datasheet for a list of supported features.

**Reference Carrier Board**

|Module | Description |
|------|------|
| Camera | 2 x MIPI CSI-1.1, 22-pin camera connectors |
| PCIe   | M.2 Key M slot (PCIe Gen3 ×4)<br>M.2 Key M slot (PCIe Gen3 ×1)<br>M.2 Key E slot |
| USB    | 4 x USB 3.0 Type-A<br>1 x USB Type-C (UFP device mode supported) |
| Networking | 1 x GbE connector |
| Display | 1 x DP 1.2 connector<br>1 x MIPI DSI-1.2 30-pin display connector |
| Other I/O | 40-pin expansion header (UART, SPI, I2S, I2C, GPIO)<br>12-pin button header<br>4-pin fan header<br>DC power jack |
| Mechanical | 103mm x 90.5mm x 34.77mm<br>(Height includes feet, carrier board, module, and thermal solution) |

## Business Cooperation & Purchase

- **WeChat (Business)**: SpacemiT1102
- **Phone**: +86 189 6649 8607
- **Email**: [business@spacemit.com](mailto:business@spacemit.com)