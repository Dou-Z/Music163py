import builtins
import os
import re
import sys
import time
import uuid
from requests_html import HTMLSession
session = HTMLSession()
import js2py
import pandas as pd
import pymysql
import requests
from bs4 import BeautifulSoup
from requests.packages import urllib3
urllib3.disable_warnings()

class Music163_Spider():

    def __init__(self):
        self.connection = pymysql.connect(host='localhost',
                                     user='root',
                                     # password='123.com',
                                     password='123456',
                                     # db='spider_datas',
                                     db='py_datas',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)


        self.headers = {
            'Cookie':'NMTID=00O3a4ZoDuzwx0P4EUsp6uzy--ZcXoAAAGIcP7waw; _iuqxldmzr_=32; _ntes_nnid=4c3ab427a469e6f1b503b1c373d8ce34,1685522937909; _ntes_nuid=4c3ab427a469e6f1b503b1c373d8ce34; WEVNSM=1.0.0; WNMCID=orzren.1685522948475.01.0; ntes_utid=tid._.6gxihj1h3opEE0FVBVLFxXtQqutJPdBh._.0; sDeviceId=YD-Nm82uPIHd2BBA1ABFRLAKGOAm%2FZy82Ry; WM_TID=BQnmoFizfmNBFAAQQULB0StQq7oY09mu; JSESSIONID-WYYY=fAMqKxItplXktP1RHBnU7%2FsVk2S6u%2B09UsaRlArjGhBNHSmTGRcUTjDX207%5C8M7wwUlkf1VGbkjOezory8%2FVeQ2U5Shqzpkc9SfCCY%2FmiPEZoEMb5m924NNpzhQVrHOJIWCXUF32f2D0Y12E53WfTufPU%2BV5hOBMZuIEdFt9XJcNsKJT%3A1686116426871; WM_NI=IJhVDzLUZpeTi4E0PBuwA5s6T7V0gb%2F9ioYfyRpSAd9v0Oy4E39983mcNRXXA1D7ww0%2FnuhI8C%2Fp2yo1rEwc1%2F8p36EuSENN308vVKVseaZpGaf3GEjcDPYvMIjc74xNOWQ%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee84f43fad9bfda8f87eb7b08ba2d14a939f8facc1618f86a4aec43e979be199e42af0fea7c3b92a8b96a8b7c772908b9691e860abec8bd1d34ab7a98fd6f23e98e99ad1e66aede7a790dc6ebb8ec0b4c470fbaa00b0fc4087edf7dabb39afbd82b3db5483ef8cd8f67df4f1a296eb43fc9de191b173adefbea6f669f3f1f891b23e87ab9da6cd46f1f0f897d54196adab82d97c85bfaad4c64faabd8cb1dc7e8f97a684b640bc9281b8d437e2a3',

            'Referer': 'https://music.163.com/',

            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
        }
        self.create_folder('.\music_data')

    def CreateUUid(self):
        my_uuid = uuid.uuid1()
        id = builtins.str(my_uuid)
        return id

    def create_folder(self,folder_path):
        """
        如果文件夹不存在，则创建文件夹
        """
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    def session_get_playlist(self):
        play_url = 'https://music.163.com/discover/playlist'

        response = session.get(url=play_url, headers=self.headers, verify=False)

        # All_classify_href = response.html.xpath('//a[@class="s-fc1 "]/@href')
        all_classify_name = response.html.xpath('//a[@class="s-fc1 "]/text()')

        return all_classify_name

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

        Total_tag = self.session_get_playlist()

        for item in Total_tag:

            time.sleep(2)

            url = f'https://music.163.com/discover/playlist/?cat={item}&order=hot&limit=35'
            response = requests.get(url=url, headers=self.headers, verify=False)
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
                print('\r',tag, url, end='', flush=True)
                id = self.CreateUUid()
                # 将索引页写入CSV文件中
                with open('music_data/album_list.csv', 'a+', encoding='utf-8-sig') as f:
                    f.write(id + ',' + tag + ',' + url + '\n')
                if j >= 1:
                    break

                # 插入数据库
                ms.insert_tag(self.CreateUUid(),item,url)

        print("\n 已获取歌单标签页的信息，保存至 music_data/album_list.csv")


    def get_data_of_ablum_detail(self):
        """获取歌单详情页的信息"""
        df = pd.read_csv('./music_data/album_list.csv', header=None, names=['id','tag','url','nan1','nan2'])

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
            response = requests.get(url=url, headers=self.headers, verify=False)
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


            # 获取歌单介绍
            if soup.select('#album-desc-more'):
                text = soup.select('#album-desc-more')[0].get_text().replace('\n', '').replace(',', '，')
            else:
                text = '无'
            # 作者
            author = soup.select('.name a')[0].get_text()

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

            for j in range(len(li)):
                if 'id=' in li[j]['href']:
                    id_li= li[j]['href'].split('=')
                    music_id = id_li[1]
                    self.get_data_of_music_detail(tag_id, li[j].get_text(), music_id)
                else:
                    continue

            print("\n已获取专辑详情页的信息，本地保存至 music_data/music_album.csv")
            # break

    def get_data_of_music_detail(self, tag, title, music_id):

        print(f"\r正在获取 = {music_id} = 歌曲详情页的信息...", end='', flush=True)
        url = 'https://music.163.com/#/song?id=' + music_id
        try:
            response = requests.get(url=url, headers=self.headers, verify=False)
        except Exception as e:
            # print(response.status_code)
            print(url,'ERROR:',e)
            return 0
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        # 图像地址

        pic_src = re.findall('property="og:image" content="(.*?)"',html)[0]
        # print(pic_src)
        # 歌手
        aut_li = soup.select('.des span')
        if len(aut_li) > 0:

            autuor = soup.select('.s-fc4 span')[0]['title']
        else:
            autuor = ""

        # 是否要VIP
        VIP_li = soup.select('.u-icn-98')
        print("\nVIP:",VIP_li)
        if len(VIP_li) >= 0:
            vip_flag = 1
            song_url = 'VIP歌曲'
            song_time = 0
            song_type = 'VIP歌曲'
        else:
            vip_flag = 0
            # 获取歌曲链接及其他信息
            music_json= self.Music_Post(music_id)

            song_url = music_json['data'][0]['url']
            print('url：', song_url)
            song_time = music_json['data'][0]['time']
            print('时长：', song_time)
            song_type = music_json['data'][0]['type']
            print('后缀名：', song_type)
            # 判断是否有MV

        mv_if = re.findall('title="播放mv" href="(.*?)"', html)
        mv_href = '无MV'
        if len(mv_if) > 0:
            # 有MV，获取MVid
            mv_id = mv_if[0].split('=')[1]
            mv_href = self.Mv_Spider_post(mv_id)


        composer = title

        # 评论量 cnt_comment_count
        cnt_comment = self.get_comment_cnt(music_id)

        # 输出歌单详情页信息
        print('\r', title, song_time, autuor, song_url, composer, tag, cnt_comment, pic_src, end='', flush=True)

        with open('./music_data/music_detail.csv', 'a+', encoding='utf-8-sig') as f:
            f.write(title+',' + str(vip_flag)+ ',' + str(song_time) + ',' + autuor + ',' + mv_href + ',' + str(song_url) + ','+song_type+',' + title + ',' + composer  + ',' + tag + ',' + str(cnt_comment) + ',' + pic_src + '\n')

        # 写入数据库
        ms.insert_music(self.CreateUUid(),title,song_time,autuor,vip_flag,song_url,mv_href,composer,song_type,tag,cnt_comment,pic_src)

    def MusucJSBlowUP(self,id):
        # 创建js执行环境，返回一个上下文对象
        content = js2py.EvalJs()
        # 执行js代码
        content.execute(open('./Music163.js', 'r', encoding='utf-8').read())
        funcName = sys._getframe().f_back.f_code.co_name
        if funcName == 'Music_Post':
            # 获取歌曲的encSecKey
            res = content.Get_encKey(id)
        elif funcName=='Mv_Spider_post':
            # 获取MV的encSecKey
            res = content.Get_mv_encKey(id)
        elif funcName=='get_comment_cnt':
            # 获取comment的encSecKey
            res = content.Get_comment_encKey(id)
        return res

    def Music_Post(self,music_id):

        url_t = "https://music.163.com/weapi/song/enhance/player/url/v1?"

        params_dic = self.MusucJSBlowUP(music_id)
        key_params = {
            'params': params_dic['encText'],
            'encSecKey': params_dic['encSecKey']
        }
        # params_json = json.loads(key_params)
        response = requests.post(url=url_t, headers=self.headers, params=key_params, verify=False)
        # print(response.status_code)
        # print(response.json())
        return response.json()

    def Mv_Spider_post(self,ids):

        mv_url = 'https://music.163.com/weapi/song/enhance/play/mv/url'
        # ids = '5736067'
        params_dic = self.MusucJSBlowUP(ids)
        key_params = {
            'params': params_dic['encText'],
            'encSecKey': params_dic['encSecKey'],
        }
        response = requests.post(url=mv_url, headers=self.headers, params=key_params, verify=False)
        print(response.status_code)
        MV_json_data = response.json()

        mv_url = MV_json_data['data']['url']
        print('url：', mv_url)
        return mv_url

    def get_comment_cnt(self,ids):
        comment_url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token=b47c7b14bf8c72ada65f9ef86f77ec23'
        params_dic = self.MusucJSBlowUP(ids)
        key_params = {
            'params': params_dic['encText'],
            'encSecKey': params_dic['encSecKey'],
        }

        response = requests.post(url=comment_url, headers=self.headers, params=key_params, verify=False)
        # print(response.status_code)
        comment_json_data = response.json()
        totalCount = comment_json_data['data']['totalCount']
        print('totalCount：', totalCount)
        return totalCount


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


    def insert_tag(self, artist_id, artist_name,url):
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO `tag` (`id`, `title`,`link`) VALUES (%s, %s,%s)"
            cursor.execute(sql, (artist_id, artist_name,url))
            self.connection.commit()

    # 保存音乐
    def insert_music(self, music_id, title, playtime, singer, playvolume, audiorul, name, composer, lyrics, tagid,
                     commentvolume, plot):
        with self.connection.cursor() as cursor:

            sql = "INSERT INTO `music` (`id`, `title`, `playtime`,`singer`,`Vip`,`audiorul`,`mv`,`composer`,`song_type`,`tagid`,`commentvolume`,`plot`) " \
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
    ms.dis_connect()
    print('DONE！！！')
