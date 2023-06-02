import builtins
import os
import random
import re
import time
import uuid
import pandas as pd
import pymysql
import requests
from bs4 import BeautifulSoup


class Music163_Spider():

    def __init__(self):
        self.connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='123.com',
                                     db='spider_datas',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

        self.Total_list=['华语','欧美','日语','韩语','粤语','风格','流行','摇滚','民谣','电子','舞曲','说唱','轻音乐','爵士','乡村',
            'R&B/Soul','古典','民族','英伦','金属','朋克','蓝调','雷鬼','世界音乐','拉丁','New,Age','古风','后摇','Bossa,Nova']

        self.headers = {

            'Connection': 'keep-alive',
            'Cookie': 'MUSIC_A_T=1510837813641; MUSIC_R_T=1510837879814; nts_mail_user=doucx2020@163.com:-1:1; _ntes_nnid=1c7503456cec149f273482216191cabf,1662520701747; _ntes_nuid=1c7503456cec149f273482216191cabf; WNMCID=bdunkz.1662520702045.01.0; WEVNSM=1.0.0; WM_TID=u0rj0pAqpc5BQBAAVBOFD1dj%2FzHKZ%2F1n; NMTID=00O5LW3ptaHzoXIbUKInGtQ1NMq4DYAAAGD3soVWA; NTES_P_UTID=ojIIA4uvH5XIjcq0gje2GwcgfFzHYQgc|1678181326; P_INFO=doucx2020@163.com|1678181326|1|mail163|00&99|sic&1676947341&mail163#jis&320100#10#0#0|&0||doucx2020@163.com; sDeviceId=YD-Lg7zn5EKr7VFU1QUQQORKGLTEMBNO7Qx; ntes_utid=tid._.%252BCaNPOwEETlAAxUVUUfEgQqyj%252FVt1xTZ._.0; _iuqxldmzr_=32; JSESSIONID-WYYY=R2gNIslltkUssv1prTgPZMRzGi0t8ng8oYtRpFnH%2B0SGazftrY%2B%2F%2B1zO77j9cKRTYpc%5CozHlj3%2FtxAlbv4pZmi5CPZqdvVcvOIyRf%2BGQJ4CZVUfMX94O%2F0T1qzdgCsyJ1r%2BG6TT%2FPmYi0D%5CJns6R9dMcC6%5CRGIyA4%5CX7f%2F2i6ex%2Fgil5%3A1685628401824; WM_NI=xp%2FDQcct351rlaU%2ByJgSz6ytIMZrmBlj0KtjsyL5pbDEhgH57gq7qvlhkcWyRMQMIluH%2BPuULFOzTSuj0xHx63hcA2G5Lw1RZjfjG7IRaDnY5dPOvEfGxiKd3PQzs%2FzSNXI%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed0b140a1b4a085d553f38e8ea6c44a979b9e87d86185ebfaa9ca49a9898fd7eb2af0fea7c3b92abcb0e1a5d469a1acfdd6b47ab0bf9bccfc42a58db6d7fc808b939693f04ab0b600acf762b1a784d6f36a889ba888cb3ff5b9bfd8f47eb0b8a584d67392939faecc68b798e5b1f85f909a819bd759b7b60099cb74f6eda884c43a85eb8498b45a9ab6aa8bc63d8b8eafa5ed53f7bca0b0f54fa699b88aca70f1909f9bf225ba8d82b9cc37e2a3; __snaker__id=caz9LoCQ0BJyaUuH; gdxidpyhxdE=en%2BQKWpr%5C7%5CH8w9E1T6PolGT6eCJ%2F8GGmwV%5CCaNqr1P3U%2FhUdBt4bZz37DPsYiHJP7SAPEfiz7pdeU3610fNwyXow%5Crg%2Bu5QELKzN6Gclx2avP7zAWLUPYbexIUerNb3YwTMhEZ%2F5o6e%5C%5CgRbAV6lU9MGlYcqM1%2BLG6jTIURem%2Bptqqr%3A1685627509606; YD00000558929251%3AWM_NI=qgjrmzhLs%2Fa6%2Fp2Ejvy4dEOB9hz0AqF1DkKmiIPff4nV8hPdEk77cHXiolU7zCsyQmMo5k3qGDeAgv1A%2Fa%2Btsj3qvedgRAP6B3OwOvjw6UnAriESyLqa1C%2FIxog1OsUWQ1k%3D; YD00000558929251%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee94c86ea3f0b6b7b1508d9e8ea7c15e929a8bb0d46898b1e5a4d344aef59ed9e62af0fea7c3b92ab3b9a693f072ac94bdd0e43eedb0fea6e97ebbecaca6ce4afbb8b6d1c47b86ef8c8cca67ab97a087e540ae8af889d37087b5f9d8e2449cb7a18dd83dba9dbd9ad4678fb1fb8cb27b859caba2e67ef39fe182aa80b1b6fd92f56fa8b99ea2d33e82ed8198ce7eaaa9fab6ed4bb2b78bb4fc48b3bfffa4ae43bcb1a9d2ce7997899fd2ea37e2a3; YD00000558929251%3AWM_TID=clO6tivR0apABFFFRVLUkS5qCPSj6V4x; __remember_me=true; MUSIC_U=006CD20E51F6949561BEEEBBE036583B92631982FBE00D2B36819DCBA8CDC72C92039C913606D1017A7FD4F590398BD81EDE39571605A0CD4CFA2FF1ED0BC145DD9315B2C6E30BF037A63D4C33ADFC35E191AB7EFD1AC999428BBEC4AEFF5BC1741BD9BE6702231A5C83DEA22228F3AECD4A463D0803ADFD60B21BACFFA76D3747763E33B8484ED22CA2363D6F2EC97D0849120F4C2A4A5273F337FE25E9F52EE6E0999BBAEA27D6EDF154803866C6AB2611123937140D5145AFF4501E98501DEBE7A01437DE4F2237D791BDEB87609E67180588BA386EF432C6AE830651CD9DB15E6BAD6F392EA9504EA1DDB13A9494091BE0BEA117E2E12981E99059720E616816484B3CBC4F46B8C21058CC6F962CCE68A88FAE74C43CC4478FD26A9DE4A8695D79A7954DA3669CFC3256D643B2EC7E6AFD9346FC1EB24D61A458D4D4046AC3D55B001CB8CB1B38D37D133F493DF7459EA2170A911A3C746013E3EE36B35D52; __csrf=408cf3f916a7a73b70187f1878ccd4a0; ntes_kaola_ad=1',

            'Referer': 'https://music.163.com/',

            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
        }

    def CreateUUid(self):
        my_uuid = uuid.uuid1()
        id = builtins.str(my_uuid)
        return id

    def get_data_of_music_tag(self):
        """获取歌单索引页的信息"""


        print("正在获取歌单标签索引页的信息...")

        # 输出进度条
        t = 60
        start = time.perf_counter()

        for i in range(t + 1):
            finsh = "▓" * i
            need_do = "-" * (t - i)
            progress = (i / t) * 100
            dur = time.perf_counter() - start

            print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(progress, finsh, need_do, dur), end="",flush=True)

            time.sleep(0.02)

        for item in self.Total_list:
            # print('\r', i, end='', flush=True)

            time.sleep(2)

            url = f'https://music.163.com/discover/playlist/?cat={item}&order=hot&limit=35'
            response = requests.get(url=url, headers=self.headers)
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')

            # 获取包含歌单详情页网址的标签
            ids = soup.select('.dec a')

            for j in range(len(ids)):

                # 标签
                tag =item
                # 获取歌单详情页地址
                url = ids[j]['href']

                # 输出歌单索引页信息
                # print('\r',tag, url, end='', flush=True)
                id = self.CreateUUid()
                # 将索引页写入CSV文件中
                with open('music_data/album_list.csv', 'a+', encoding='utf-8-sig') as f:
                    f.write(id + ',' + tag + ',' + url + '\n')

                # 插入数据库
                # 写入数据库
                # print(item)
            ms.insert_tag(self.CreateUUid(),item)

        print("\n 已获取歌单索引页的信息，保存至 music_data/album_list.csv")

        # print("\n已获取歌单索引页的信息，保存至 music_data/music_list.csv")

    def get_data_of_ablum_detail(self):
        """获取歌单详情页的信息"""
        df = pd.read_csv('./music_data/album_list.csv', header=None, names=['id','tag','url','z','g'])

        print("正在获取专辑详情页的信息...")

        # 输出进度条
        t = 60
        start = time.perf_counter()

        for i in range(t + 1):
            finsh = "▓" * i
            need_do = "-" * (t - i)
            progress = (i / t) * 100
            dur = time.perf_counter() - start

            print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(progress, finsh, need_do, dur), end="",flush=True)

            time.sleep(0.02)

        url_len = len(df['url'])
        for i in range(url_len):
            time.sleep(1)

            url = 'https://music.163.com' + df['url'][i]
            response = requests.get(url=url, headers=self.headers)
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            print('\n', url)
            # 获取歌单标题
            title = soup.select('h2')[0].get_text().replace(',', '，')
            # 解析图片连接
            img_src_big = soup.select('.u-cover-dj img')[0]['data-src']
            if '?' in img_src_big:
                img_src = img_src_big.split("?")[0]
            else:
                img_src = img_src_big
            # 获取标签
            tag = df['tag'][i]
            tag_id = df['id'][i]
            print(tag_id)

            # 获取歌单介绍
            if soup.select('#album-desc-more'):
                text = soup.select('#album-desc-more')[0].get_text().replace('\n', '').replace(',', '，')
            else:
                text = '无'
            # 作者
            author = soup.select('.name a')[0].get_text()

            # 获取歌单收藏量
            # collection = soup.select('#content-operation i')[1].get_text().replace('(', '').replace(')', '')

            # 歌单播放量
            play = soup.select('.s-fc6')[0].get_text()

            # 歌单内歌曲数
            songs = soup.select('#playlist-track-count')[0].get_text()

            # 歌单评论数
            comments = soup.select('#cnt_comment_count')[0].get_text()

            # 输出歌单详情页信息

            print('\r', title, tag_id, tag, text, author, comments, songs, play, end='', flush=True)
            uuid = self.CreateUUid()
            # 将详情页信息写入CSV文件中
            with open('./music_data/music_album.csv', 'a+', encoding='utf-8-sig') as f:
                f.write(uuid + ',' + title + ',' + tag_id + ',' + text + ',' + img_src + ',' + author + ','
                        + comments + ',' + songs + ',' + play + '\n')
            # 写入数据库
            ms.insert_album(self.CreateUUid(),title ,tag_id, text, img_src , author, comments,songs ,play)

            # 获取歌单内歌曲名称
            li = soup.select('.f-hide li a')
            playtime_li = soup.select('.s-fc3 .u-dur')
            #autuor_li = soup.select('td .text')

            for j in range(len(li)):

                #aut = autuor_li[j * 2].get_text()
                aut=''
                pt = 1
                if type(pt) != 'int':
                    pt=1
                else:
                    pt = playtime_li[j].get_text()
                print('\n tagid,title,piaytime,autuor,src \n' ,tag_id, li[j].get_text(), pt, aut, li[j]['href'] ,end='', flush=True)
                self.get_data_of_music_detail(tag_id, li[j].get_text(), pt, aut, li[j]['href'])

            print("\n已获取专辑详情页的信息，本地保存至 music_data/music_album.csv")

    def get_data_of_music_detail(self, tag, title, playtime, autuor, music_src):

        print("\n正在获取歌曲详情页的信息...")
        url = 'https://music.163.com' + music_src
        response = requests.get(url=url, headers=self.headers)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        lyric_dev = soup.select('#lyric-content')

        lyric = lyric_dev[0].get_text()
        lyric=str(lyric)

        composer = 'None'
        try:
            composer = re.findall(r'曲：(.*)', lyric)[0]
        except Exception as e:
            # 打印错误日志
            print('internal error : ', str(e))
            time.sleep(2)

        # 查询MySQL数据
        # tag_id = MusicToSql.Search_date(tag,'tag')

        # 评论量 cnt_comment_count
        cnt_comment = soup.select('#cnt_comment_count')[0].get_text()
        # 图像
        pic_src = soup.select('.u-cover img')[0]['src']
        # 输出歌单详情页信息
        print('\r', title, playtime, autuor, music_src, composer, lyric, tag, cnt_comment, pic_src, end='', flush=True)

        with open('./music_data/music_detail.csv', 'a+', encoding='utf-8-sig') as f:
            f.write(title + ',' + str(playtime) + ',' + autuor + ',' + '' + ',' + music_src + ',' + title + ',' + composer +',' + lyric + ',' + tag + ',' + cnt_comment + ',' + pic_src + '\n')
        cnt_comment = random.randint(100,5000)
        # 写入数据库
        ms.insert_music(self.CreateUUid(),title,playtime,autuor,0,music_src,title,composer,lyric,tag,cnt_comment,pic_src)
    def del_csv(self):
        try:
            os.remove('./music_data/music_detail.csv')
            os.remove('./music_data/music_album.csv')
            os.remove('./music_data/album_list.csv')
        except Exception as e:
            print(e)

class MusicToSql(Music163_Spider):
    def __init__(self):
        super().__init__()

    def dis_connect(self):
        self.connection.close()

    # 清库
    def truncate_all(self):
        with self.connection.cursor() as cursor:
            sql = "truncate table tag"
            cursor.execute(sql, ())
            sql = "truncate table album"
            cursor.execute(sql, ())
            sql = "truncate table music"
            cursor.execute(sql, ())

            self.connection.commit()

    def insert_album(self, album_id, title, tagid, introduction, polt, author, commentcount, musics, playvolume):
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO `album` (id,title,tagid,introduction,polt,author,commentcount,musics,playvolume) " \
                  "VALUES (%s, %s,%s,%s,%s, %s,%s,%s,%s)"

            cursor.execute(sql, (
                album_id, title, tagid, introduction, polt, author, commentcount, musics, playvolume))
            self.connection.commit()

    ## 保存tag标签


    def insert_tag(self, artist_id, artist_name):
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO `tag` (`id`, `title`) VALUES (%s, %s)"
            cursor.execute(sql, (artist_id, artist_name))
            self.connection.commit()

    # 保存音乐
    def insert_music(self, music_id, title, playtime, singer, playvolume, audiorul, name, composer, lyrics, tagid,
                     commentvolume, plot):
        with self.connection.cursor() as cursor:

            sql = "INSERT INTO `music` (`id`, `title`, `playtime`,`singer`,`playvolume`,`audiorul`,`name`,`composer`,`lyrics`,`tagid`,`commentvolume`,`plot`) " \
                  " VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s)"
            cursor.execute(sql, (music_id, title, playtime, singer, playvolume, audiorul, name, composer, lyrics, tagid, commentvolume, plot))
            self.connection.commit()
    # 查询数据库

    def Search_date(self, con, tablename):
        with self.connection.cursor() as cursor:
            sql = "SELECT id FROM `%s` where `title`=%s "
            cursor.execute(sql, (con, tablename))
            return cursor.fetchone()


if __name__ == '__main__':
    wy = Music163_Spider()
    ms = MusicToSql()
    ms.truncate_all()
    wy.del_csv()
    wy.get_data_of_music_tag()
    wy.get_data_of_ablum_detail()

