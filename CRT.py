import argparse
import requests
import warnings

def Search(url, out):
    result = []
    warnings.filterwarnings("ignore")
    try:
        re = requests.get(url="https://crt.sh/?q=%s&output=json&exclude=expired" % url, verify=False).json()
        for i in re:
            result.append(i['common_name'])
        result = list(set(result))
        for i in result:
            print(i)
        if out != "-":
            with open(str(out), mode='a') as filename:
                for i in result:
                    filename.write(str(i) + '\n')
    except:
        print("连接API服务器失败")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                     description='Li NiuBi')
    parser.add_argument('-u', type=str, help='指定一级域名')
    parser.add_argument('-f', type=str, help='从文件读取域名')
    parser.add_argument('-o', type=str, help='输出到文件,默认不输出', default="-", required=False)
    args = parser.parse_args()
    if not args.u and not args.f:
        print("usage: CRT.py [-h] -u U OR -f F [-o O]")
    if args.u:
        Search(url=args.u, out=args.o)
    elif args.f:
        try:
            with open(str(args.f), 'r') as f:
                for line in f:
                    Search(url=line.strip('\n'), out=args.o)
        except:
            print("无法打开域名列表")