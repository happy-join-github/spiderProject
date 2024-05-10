#导入库
import os
import time

import requests
from pyquery import PyQuery as pq
import threading
from PIL import Image
import pillow_avif

url = 'https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&wq=%E6%89%8B%E6%9C%BA&pvid=8858151673f941e9b1a4d2c7214b2b52&czLogin=1'
headers = {
    'authority': 'search.jd.com',
    'method': 'GET',
    'path': '/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&wq=%E6%89%8B%E6%9C%BA&pvid=8858151673f941e9b1a4d2c7214b2b52',
    'scheme': 'https',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'max-age=0',
    # 'Cookie': '__jdu=17134327358151142091467; shshshfpa=06e7c656-8c97-574f-9331-cc5457841b6d-1713432738; shshshfpx=06e7c656-8c97-574f-9331-cc5457841b6d-1713432738; areaId=5; ipLoc-djd=5-142-0-0; PCSYCityID=CN_130000_130100_0; _pst=jd_yncUvJJTUmtn; unick=jd_yncUvJJTUmtn; pin=jd_yncUvJJTUmtn; _tp=kDlYz%2Bhs0F9sT2RgVcvDKg%3D%3D; unpl=JF8EAKlnNSttXE1XAhwAEkcTQ1QGW1sJQ0QAazQDAQoMHlUEHgFMEUN7XlVdWBRKEx9uYxRXXVNKUQ4bBysVEUtcVVZtC0oVAmlgA1JYXntkNRgCKxMgS1tUXFgKSBEBa24FUF1YTlcEEwIeFRZ7XGReVQ97JzNqZwRUXF9KVAcdMhoiEktcVVxcDE8TAl8sa1UQWE1UBx4AGBQST1RUWl0IThQCZ2cAU1toSmQG; __jdv=76161171|ntp.msn.cn|t_2030767747_|jingfen|5726638d298c4709b25b7dfed0042f2b|1714914254925; mba_muid=17134327358151142091467; mba_sid=17149142676752770521399392613.1; wlfstk_smdl=tm6nt0ypbutfhui0dk0iusplvjq6cem5; TrackID=1QQXWVmDM6SLv0T21CSRTBSCnGDwtrLobko-L_CMHm-YGftUGP3RTvLhwqvmOQSHQQZ2XyfV9iUFJD0xaqUeIYulT4do0L_NX8VacqjpDUw-uolh9kXd1D2n8ClHFX5l-; thor=FD11AA8FCF9442851B767037D6758A620AF569C1F01AFDC5493C2FB04987F67B7118432C58D37074A945436374D23E2CD3A7FF6BE62AF5DC88A912F44A56C8E1473219B413413F024BE59E5370E75C7EDAC632471D99F5564B8E107E4A64CC4FA45FF54B2025EACC77D7B0806801F5B10EE06F19E612271958F50589ACFB22E4B3FB7BB8261639CED7BCFAD396AA8E3FD555E75B0A0BA105F88EEE85460589E2; flash=2_9PvpWpao61cMBaI7nQdvWKkqwKEdULrqq6NJnQzP5Y4vW27iEJ_ISa2vw8J1go14g1j6onLaAhGsOrVy2R-ZI-6RDCJzR9n_1_ukO3yo69FOXXLSQgkPDQt_y50EkIstWiN3jKtELrbcT-TknWJnHZAib8ufDs2l_iGBK10Fszj*; pinId=-NQO5b7I_mUJ172OysSKag; ceshi3.com=000; jsavif=1; jsavif=1; shshshfpb=BApXc98rTS-pAEWhGftC5-yH4pSPsQqq3BlECIBdq9xJ1Mh3TPYC2; __jda=143920055.17134327358151142091467.1713432735.1714742304.1714914255.4; __jdc=143920055; rkv=1.0; qrsc=3; avif=1; 3AB9D23F7A4B3CSS=jdd03V52UUM3UAUV3HDC6OCG2NOKPHY6YKHOTFJQNRA5YSUFJSNLY5R42MIEF4X6SCAXVIYVFOWWWLDVYBVSFJYQXYWTXTEAAAAMPJDPFTTYAAAAADRLKN6SKUPMXYAX; _gia_d=1; xapieid=jdd03V52UUM3UAUV3HDC6OCG2NOKPHY6YKHOTFJQNRA5YSUFJSNLY5R42MIEF4X6SCAXVIYVFOWWWLDVYBVSFJYQXYWTXTEAAAAMPJDPFTTYAAAAADRLKN6SKUPMXYAX; __jdb=143920055.8.17134327358151142091467|4.1714914255; 3AB9D23F7A4B3C9B=V52UUM3UAUV3HDC6OCG2NOKPHY6YKHOTFJQNRA5YSUFJSNLY5R42MIEF4X6SCAXVIYVFOWWWLDVYBVSFJYQXYWTXTE',
    'Priority': 'u=0, i',
    'Referer': 'https://www.jd.com/',
    'Sec-Ch-Ua': '"Chromium";v="124", "Microsoft Edge";v="124", "Not-A.Brand";v="99"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'
}
cookies = {'__jdu': '17134327358151142091467', ' shshshfpa': '06e7c656-8c97-574f-9331-cc5457841b6d-1713432738', ' shshshfpx': '06e7c656-8c97-574f-9331-cc5457841b6d-1713432738', ' areaId': '5', ' ipLoc-djd': '5-142-0-0', ' PCSYCityID': 'CN_130000_130100_0', ' _pst': 'jd_yncUvJJTUmtn', ' unick': 'jd_yncUvJJTUmtn', ' pin': 'jd_yncUvJJTUmtn', ' _tp': 'kDlYz%2Bhs0F9sT2RgVcvDKg%3D%3D', ' unpl': 'JF8EAKlnNSttXE1XAhwAEkcTQ1QGW1sJQ0QAazQDAQoMHlUEHgFMEUN7XlVdWBRKEx9uYxRXXVNKUQ4bBysVEUtcVVZtC0oVAmlgA1JYXntkNRgCKxMgS1tUXFgKSBEBa24FUF1YTlcEEwIeFRZ7XGReVQ97JzNqZwRUXF9KVAcdMhoiEktcVVxcDE8TAl8sa1UQWE1UBx4AGBQST1RUWl0IThQCZ2cAU1toSmQG', ' __jdv': '76161171|ntp.msn.cn|t_2030767747_|jingfen|5726638d298c4709b25b7dfed0042f2b|1714914254925', ' mba_muid': '17134327358151142091467', ' mba_sid': '17149142676752770521399392613.1', ' wlfstk_smdl': 'tm6nt0ypbutfhui0dk0iusplvjq6cem5', ' TrackID': '1QQXWVmDM6SLv0T21CSRTBSCnGDwtrLobko-L_CMHm-YGftUGP3RTvLhwqvmOQSHQQZ2XyfV9iUFJD0xaqUeIYulT4do0L_NX8VacqjpDUw-uolh9kXd1D2n8ClHFX5l-', ' thor': 'FD11AA8FCF9442851B767037D6758A620AF569C1F01AFDC5493C2FB04987F67B7118432C58D37074A945436374D23E2CD3A7FF6BE62AF5DC88A912F44A56C8E1473219B413413F024BE59E5370E75C7EDAC632471D99F5564B8E107E4A64CC4FA45FF54B2025EACC77D7B0806801F5B10EE06F19E612271958F50589ACFB22E4B3FB7BB8261639CED7BCFAD396AA8E3FD555E75B0A0BA105F88EEE85460589E2', ' flash': '2_9PvpWpao61cMBaI7nQdvWKkqwKEdULrqq6NJnQzP5Y4vW27iEJ_ISa2vw8J1go14g1j6onLaAhGsOrVy2R-ZI-6RDCJzR9n_1_ukO3yo69FOXXLSQgkPDQt_y50EkIstWiN3jKtELrbcT-TknWJnHZAib8ufDs2l_iGBK10Fszj*', ' pinId': '-NQO5b7I_mUJ172OysSKag', ' ceshi3.com': '000', ' jsavif': '1', ' shshshfpb': 'BApXc98rTS-pAEWhGftC5-yH4pSPsQqq3BlECIBdq9xJ1Mh3TPYC2', ' __jda': '143920055.17134327358151142091467.1713432735.1714742304.1714914255.4', ' __jdc': '143920055', ' rkv': '1.0', ' qrsc': '3', ' avif': '1', ' 3AB9D23F7A4B3CSS': 'jdd03V52UUM3UAUV3HDC6OCG2NOKPHY6YKHOTFJQNRA5YSUFJSNLY5R42MIEF4X6SCAXVIYVFOWWWLDVYBVSFJYQXYWTXTEAAAAMPJDPFTTYAAAAADRLKN6SKUPMXYAX', ' _gia_d': '1', ' xapieid': 'jdd03V52UUM3UAUV3HDC6OCG2NOKPHY6YKHOTFJQNRA5YSUFJSNLY5R42MIEF4X6SCAXVIYVFOWWWLDVYBVSFJYQXYWTXTEAAAAMPJDPFTTYAAAAADRLKN6SKUPMXYAX', ' __jdb': '143920055.8.17134327358151142091467|4.1714914255', ' 3AB9D23F7A4B3C9B': 'V52UUM3UAUV3HDC6OCG2NOKPHY6YKHOTFJQNRA5YSUFJSNLY5R42MIEF4X6SCAXVIYVFOWWWLDVYBVSFJYQXYWTXTE'}


res = requests.get(url,headers=headers,cookies=cookies)
html = res.text
doc = pq(html)
imlist = doc("img[width='220'][height='220']")


img_url ={}
for im in imlist.items():
    if im.attr('src') is not None:
        imurl = 'https:'+im.attr('src')
    else:
        imurl = 'https:'+im.attr('data-lazy-img')
    key = imurl.split('/')[-1]
    img_url[key] = imurl


def download(title,url):
    time.sleep(0.5)
    response = requests.get(url,headers=headers,cookies=cookies)
    with open(f'img/{title}','wb') as f:
        f.write(response.content)
    # 图片格式转换
    # 需要下载pillow 和 pillow-avif-plugin
    # 命令
    # pip install pillow
    # pip install pillow-avif-plugin
    image = Image.open(f'img/{title}')
    image = image.convert("RGB")
    output_path = f"convertImg/{title.replace('avif', '')}"
    image.save(output_path, "JPEG")



# 创建下载目录
if os.path.exists('img') is None:
    os.mkdir('img')
# 创建转换目录
if os.path.exists('convertImg') is None:
    os.mkdir('convertImg')

lst = []
for i in range(3):
    for key,val in img_url.items():
        th = threading.Thread(target=download,args=(key,val))
        th.start()
        print(f"正在下载{key.replace('avif','')}")
        lst.append(th)

for th in lst:
    th.join()
print('下载完成')
try:
    os.remove('img')
except PermissionError as e:
    print('你没有删除img的权限，请手动删除img文件夹')


