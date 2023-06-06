import requests
from bs4 import BeautifulSoup
import js2py

def Music_datail_Parse():
    url = 'https://music.163.com/song?id=1915894370'

    headers = {

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
def Music_playlist_Parse():
    # url = 'https://music.163.com/song?id=28059417'
    url = 'https://music.163.com/song?id=67857'
    # url = 'https://music.163.com/song?id=1915894842'
    play_url = 'https://music.163.com/discover/playlist'
    headers = {

                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
    try:
        response = requests.get(url=play_url, headers=headers, verify=False)
        print(response.status_code)
    except Exception as e:
        # print(response.status_code)
        print('ERROR:', e)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    # print(html)
    play_list = soup.select('.bd a')[2:]

    print(len(play_list))
    print(play_list)


if __name__ == '__main__':
    request_Post()
    # Music_datail_Parse()
