import json
import re

import pandas as pd

# df = pd.read_csv('music_data/album_list.csv', header=None, names=['id', 'tag', 'url', 'z','a'])
# print(df)
import requests
from bs4 import BeautifulSoup
import js2py
import execjs
import jsonpath

def Music_datail_Parse():
    url = 'https://music.163.com/song?id=1915894370'
    # url = 'https://music.163.com/song?id=67857'
    # url = 'https://music.163.com/song?id=1915894842'
    headers = {
                # 'Cookie':'nts_mail_user=doucx2020@163.com:-1:1; _ntes_nuid=1c7503456cec149f273482216191cabf; _ntes_nnid=1c7503456cec149f273482216191cabf,1662520701747; WNMCID=bdunkz.1662520702045.01.0; WEVNSM=1.0.0; WM_TID=u0rj0pAqpc5BQBAAVBOFD1dj%2FzHKZ%2F1n; NMTID=00O5LW3ptaHzoXIbUKInGtQ1NMq4DYAAAGD3soVWA; NTES_P_UTID=ojIIA4uvH5XIjcq0gje2GwcgfFzHYQgc|1678181326; P_INFO=doucx2020@163.com|1678181326|1|mail163|00&99|sic&1676947341&mail163#jis&320100#10#0#0|&0||doucx2020@163.com; sDeviceId=YD-Lg7zn5EKr7VFU1QUQQORKGLTEMBNO7Qx; ntes_utid=tid._.%252BCaNPOwEETlAAxUVUUfEgQqyj%252FVt1xTZ._.0; _iuqxldmzr_=32; __snaker__id=caz9LoCQ0BJyaUuH; gdxidpyhxdE=en%2BQKWpr%5C7%5CH8w9E1T6PolGT6eCJ%2F8GGmwV%5CCaNqr1P3U%2FhUdBt4bZz37DPsYiHJP7SAPEfiz7pdeU3610fNwyXow%5Crg%2Bu5QELKzN6Gclx2avP7zAWLUPYbexIUerNb3YwTMhEZ%2F5o6e%5C%5CgRbAV6lU9MGlYcqM1%2BLG6jTIURem%2Bptqqr%3A1685627509606; YD00000558929251%3AWM_NI=qgjrmzhLs%2Fa6%2Fp2Ejvy4dEOB9hz0AqF1DkKmiIPff4nV8hPdEk77cHXiolU7zCsyQmMo5k3qGDeAgv1A%2Fa%2Btsj3qvedgRAP6B3OwOvjw6UnAriESyLqa1C%2FIxog1OsUWQ1k%3D; YD00000558929251%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee94c86ea3f0b6b7b1508d9e8ea7c15e929a8bb0d46898b1e5a4d344aef59ed9e62af0fea7c3b92ab3b9a693f072ac94bdd0e43eedb0fea6e97ebbecaca6ce4afbb8b6d1c47b86ef8c8cca67ab97a087e540ae8af889d37087b5f9d8e2449cb7a18dd83dba9dbd9ad4678fb1fb8cb27b859caba2e67ef39fe182aa80b1b6fd92f56fa8b99ea2d33e82ed8198ce7eaaa9fab6ed4bb2b78bb4fc48b3bfffa4ae43bcb1a9d2ce7997899fd2ea37e2a3; YD00000558929251%3AWM_TID=clO6tivR0apABFFFRVLUkS5qCPSj6V4x; __remember_me=true; MUSIC_U=006CD20E51F6949561BEEEBBE036583B92631982FBE00D2B36819DCBA8CDC72C92039C913606D1017A7FD4F590398BD81EDE39571605A0CD4CFA2FF1ED0BC145DD9315B2C6E30BF037A63D4C33ADFC35E191AB7EFD1AC999428BBEC4AEFF5BC1741BD9BE6702231A5C83DEA22228F3AECD4A463D0803ADFD60B21BACFFA76D3747763E33B8484ED22CA2363D6F2EC97D0849120F4C2A4A5273F337FE25E9F52EE6E0999BBAEA27D6EDF154803866C6AB2611123937140D5145AFF4501E98501DEBE7A01437DE4F2237D791BDEB87609E67180588BA386EF432C6AE830651CD9DB15E6BAD6F392EA9504EA1DDB13A9494091BE0BEA117E2E12981E99059720E616816484B3CBC4F46B8C21058CC6F962CCE68A88FAE74C43CC4478FD26A9DE4A8695D79A7954DA3669CFC3256D643B2EC7E6AFD9346FC1EB24D61A458D4D4046AC3D55B001CB8CB1B38D37D133F493DF7459EA2170A911A3C746013E3EE36B35D52; __csrf=408cf3f916a7a73b70187f1878ccd4a0; ntes_kaola_ad=1; timing_user_id=time_3cXB7uvKxo; JSESSIONID-WYYY=%2FXjZ4wCDgJx%5C9euFcv00A3%2FnD2T3tiwYyijK0VZ7mjJ2SpuFEdBMoVEE0A5iChUEENyrlYPDejDNI7Ifw9SpS6%2FFj9IKXCJ2IJao2XsJ4K%2BXJiKSpCJF%5CGAcyc3ZvJh2Y9N7D0%2B%2FdYUPJT%5CmYFpPaacV8VkeJ4FqAZcBjb7oogIF%5C838%3A1685775628218; WM_NI=RkokCQ2xfPmavu03r1i1HYEIKANUj%2FyzSaMTys5P1%2FKhFZpirO8EvbdvQZ5hNZ9%2BEnSFWwqXJ5weRIzdYAxgg2SbjW9aMug232BCrcHOkUTXSl6yxwSAfVOPSpwUWzbYVXo%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed8d74b93a98889d372f3b48fb2c44e829f9ab1d56485aafaccf633a98cfca9ce2af0fea7c3b92a92b5a18cc25bf2a8aab1f06bb6ab00d4f13babef88bac843899f82b6e925bba69d82d060bbadfbb1b42589b88abbf363b291f8a6f56aa8aa9fbbb8648e86f7ccc866919a9998f4548aebb986d143babc97a2fb6da5ee9d83e95dfbbf8396e63af1ee8ea4f1698c91a5b6d75491b4fa9afb7d919faab7ce5c91b0b9b6d672a2879ab9ee37e2a3',
                # 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                # 'Origin':'https://music.163.com/',

                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
    try:
        response = requests.get(url=url, headers=headers)
        print(response.status_code)
    except Exception as e:
        # print(response.status_code)
        print('ERROR:', e)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    # print(html)
    autuor = soup.select('.s-fc4 span')[0].get_text()
    print(autuor)
    # aut_li = re.findall('data-res-author="(.*?)"',html)
    # print(aut_li[0])
    VIP_li = soup.select('.u-icn-98')
    print(VIP_li)

def MusucJSBlowUP(id):
    # 创建js执行环境，返回一个上下文对象
    content = js2py.EvalJs()
    # 执行js代码
    content.execute(open('./Music163.js', 'r', encoding='utf-8').read())

    # res = content.Get_encKey(id)
    res = content.Get_mv_encKey(id)
    return res


def request_Post():
    headers = {
        'Cookie':'nts_mail_user=doucx2020@163.com:-1:1; _ntes_nnid=1c7503456cec149f273482216191cabf,1662520701747; _ntes_nuid=1c7503456cec149f273482216191cabf; WNMCID=bdunkz.1662520702045.01.0; WEVNSM=1.0.0; WM_TID=u0rj0pAqpc5BQBAAVBOFD1dj%2FzHKZ%2F1n; NMTID=00O5LW3ptaHzoXIbUKInGtQ1NMq4DYAAAGD3soVWA; NTES_P_UTID=ojIIA4uvH5XIjcq0gje2GwcgfFzHYQgc|1678181326; P_INFO=doucx2020@163.com|1678181326|1|mail163|00&99|sic&1676947341&mail163#jis&320100#10#0#0|&0||doucx2020@163.com; sDeviceId=YD-Lg7zn5EKr7VFU1QUQQORKGLTEMBNO7Qx; ntes_utid=tid._.%252BCaNPOwEETlAAxUVUUfEgQqyj%252FVt1xTZ._.0; _iuqxldmzr_=32; __snaker__id=caz9LoCQ0BJyaUuH; YD00000558929251%3AWM_TID=clO6tivR0apABFFFRVLUkS5qCPSj6V4x; ntes_kaola_ad=1; timing_user_id=time_3cXB7uvKxo; WM_NI=OrgOzwEEnQlzSmQTuBCMxdo5%2FEy2o4oALC4lHDieRfeZ2fI2DIQ78%2BholJvDAQVfd6IzvNnHvsMz4qgoScLVM%2FYrQPZIm%2FQJLP55N2wZeLt4UXk4jP4hAkCYeGGBkLJnNzY%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee91d13d8ea9baaed33aaeeb8fb2d14a868e9a83d13c8b9e00a4aa70f6b5ac82d32af0fea7c3b92a8daea9b0f97d879ba2b2ef7291b39fb5f84a8193b885ee3fed9bb7d3ee40ad9f84a4b7688c9ca786d16ea786fe87cc3a88979fd8bb21acb1a4abf550838f9a87e73e8ba6baafed44b6ad839bb77ba5b19d84cf5e8ff19793d45c9a97a3d0d4429090fbd6cd3ab586abadf7409788a5d5e95cf8b88f8cc253a79989a3ea488ab2829bdc37e2a3; YD00000558929251%3AWM_NI=ghAwzY8G3U%2FMBJHOzBYQE6MtgfeqdxRPUiaoOqN96NCZCyWdHbQaaaM%2BJUx9Ctcl6eg%2BrnXGr6LbefVSL%2FFV9Y7IvMY4kmh0VLgXulvhxq%2BTCnzYND1EQmyfXsgQrfh1QXE%3D; YD00000558929251%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eea8f54bb7a9bfd1b25aa7b08fa6d14a868b8a82d87d8e9ea88bd94b989481acfb2af0fea7c3b92aa5b88f98f953fc99fdb6ae47829688b0f94a9b8f8bd7d080a5baab92e77492909b8ae4658daf82dab54681868d9ad6708cbe9f82e46b8ff586b6fb3381acad8db56fa5f5be8fdb4db2ea8483e86e968d84d0c55efb87f9aaf5479beca58eeb3c9694a9b9f868b6b8b892aa6081b2b6bacd50f39b9f8efc6e9cada9b2f16eacef9fb9c837e2a3; __csrf=808875af829766a4f2826d221ee3d74a; __remember_me=true; MUSIC_U=00635BF21FB2F651D04DB9826A14E717233D9AE14BF8F74EB3158B6779B96DA8749E20D278DBB5EE2DD76B6BA6D81ED89A7E14344799DF281D315F7B75B1C4B0849C87B67A1B09754C8B14036D877A31024FECF1B31FA8D504469364D3F77B7A4F14FAC184F063849A8CD3147CF9E659E3F76378C2E7DEC35CBE57DDDDBA75D28818BE686027E714F643B19E983B8BEC007333409D83DEE5CD7417A1D9A6457EC8F56990FAC3D74547B380D7DE427D7E105CFA47A68A01126F679D5C3C8C6333AA9FCFEC8058930FEA525AB72F9C52065590899A4582DE510D78E0688B55ED7872E15BCEC1D340A07CC6AFFAB7F2AD58F4013BEFA3F174F2BD7B176AB3EE7E49A96E8164C720BE780C75F3EB3E568D57DDBA59DA25BACA105A74161E74010E43E573A884DA639CEB3F173C19D7D5252893E2B1BF252028731BF1DB78717A7CD63E97544230C96E796975A3FEAB11C3BAF76B3BB9D1A316483616CD5FD27CF36450; gdxidpyhxdE=%2FK5K5dxklNbvYqEyUaiLtAGcaGorRxYgkceOO49dvoHISn%2FeKhyUpbT3pv0u6KsV%2F%5C743KgPf0StigVgubdoOZ%2FuZKe0p2OCqNDOT%5CZwwRY%2BueJtRCdD%2Bqomgb%2Fecd1BlBMq0TLcm6cIQVy58fL25P8p2%2FMPek2ygJPgnn%2BwWTte82M2%3A1685854528271; playerid=79226044; JSESSIONID-WYYY=f4RO2P3fdyeAF9qXmdp3t4g4xSefrd0l4xnuTRegU2JdONB40RYfizmSqxlO9qyWqdAKyJIfrKFkUsy6qeueI7tVVOpktDoz%2BNAcT%2B8%5C7ZbOuBKocdENi9R3PmGblhneSd%2BYjVRrvjJfrZSAg1t%2FQzpihwqOyHJlKjB5p5iRwO8niJir%3A1685861630008',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }
    url_song = "https://music.163.com/weapi/song/enhance/player/url/v1?"
    mv_url = 'https://music.163.com/weapi/song/enhance/play/mv/url'
              # 'https://music.163.com/weapi/song/enhance/play/mv/url'
    # ids = "67857"
    ids = '186025'
    params_dic=MusucJSBlowUP(ids)
    key_params = {
        'params':params_dic['encText'],
        'encSecKey':params_dic['encSecKey']
    }
    print(key_params)
    # params_json = json.loads(key_params)
    response = requests.post(url=mv_url, headers=headers,params=key_params)
    print(response.status_code)
    print(response.content.decode())
    music_json_data = response.json()
    print(music_json_data)
    # song_url = music_json_data['data'][0]['url']
    # print('url：',song_url)
    # song_time = music_json_data['data'][0]['time']
    # print('时长：',song_time)
    # song_type = music_json_data['data'][0]['type']
    # print('后缀名：',song_type)


if __name__ == '__main__':
    request_Post()
    # Music_datail_Parse()
