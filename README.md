# CRT-API
### crt.sh批量扫描导出工具

##### 用法：python3 CRT.py -h

```
PS E:\Desktop\Code\Python\CRT> python3 .\CRT.py -h
usage: CRT.py [-h] [-u U] [-f F] [-o O]

Li NiuBi

options:
  -h, --help  show this help message and exit
  -u U        指定一级域名 (default: None)
  -f F        从文件读取域名 (default: None)
  -o O        输出到文件,默认不输出 (default: -)
```

##### python3 CRT.py -u ddos.li

```
PS E:\Desktop\Code\Python\crt> python3 .\CRT.py -u ddos.li
beta.ddos.li
tools.ddos.li
sni.cloudflaressl.com
```

##### python3 CRT.py -f url.txt

##### python3 CRT.py -f url.txt -o 结果.txt

