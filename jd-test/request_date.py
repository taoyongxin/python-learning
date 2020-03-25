import requests

url = "https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=s%27j&page={0}&s=61&click=0"

payload = "{\n\t\"page\":\"1\",\n\t\"count\":\"5\"\n}"
headers = {
    'Host': 'search.jd.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': 'http://search.jd.com/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': 'shshshfpa=125420aa-635d-3a97-784f-7d7efcd3dcd9-1582349075; shshshfpb=dRivTGns4w1BeFiQblIQ3bQ%3D%3D; __jdu=15823490758391314323603; areaId=12; ipLoc-djd=12-978-0-0; PCSYCityID=CN_320000_320400_0; unpl=V2_ZzNtbUdQS0J1WBFUfx9dB2IEEwoSBRMTd1tOASxJDgxjAkIIclRCFnQUR1ZnGlgUZwcZX0JcQxBFCEdkeB5fA2AFEFlBZxVLK14bADlNDEY1WnwHBAJfF3ILQFJ8HlQMZAEUbXJUQyV1CXZUfxBfB2ILE1tGXkEddQpGUXkaXgJmASJtRWdzJXwAQVJ%2fGmwEVwIiHxYLSh1zCUNXNhlYDGQBF1VDUUccdwBGVnscXgZlBBNfclZzFg%3d%3d; __jdv=76161171|google-search|t_262767352_googlesearch|cpc|kwd-362776698237_0_469f1af15703460faca73b9dfac850ad|1585121474062; __jda=122270672.15823490758391314323603.1582349076.1584865705.1585121474.3; __jdc=122270672; 3AB9D23F7A4B3C9B=DDMBE62FFANBNNRDYCYNZDAO2OUDRHKWHQAEIB2TQ4LTNNYFBVDM75JHD67WMHROMZQXCRKTUGDETNUPY43OPQICA4; xtest=1839.cf6b6759; __jdb=122270672.5.15823490758391314323603|3.1585121474; shshshfp=b77807034bdb6dc21b04f6cb53a93ada; shshshsID=030e5e59191b02d3317cd592b2cca05c_2_1585121747994; qrsc=1; rkv=V0500',
    'Content-Type': 'application/json'
}


def get_data(page=0):
    realURL = url.format(page)
    response = requests.get(realURL, headers=headers, data=payload)
    return response.text.encode("utf8")
    # return brotli.decompress(response.content)


if __name__ == "__main__":
    body = get_data()
    print(body)
