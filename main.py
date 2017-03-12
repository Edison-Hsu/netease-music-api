# -*- coding: utf-8 -*-

import falcon
import json

from api import NetEase
 
class NeteaseMusicSearch:
    def on_get(self, req, resp):
        query = req.get_param('q', True)
        limit = req.get_param_as_int('limit') or 60
        offset = req.get_param_as_int('offset') or 0
        ne = NetEase()
        # 搜索单曲(1)，歌手(100)，专辑(10)，歌单(1000)，用户(1002) *(type)*
        resp.body = json.dumps(ne.search(query, 1, offset, 'true', limit))

 
class NeteaseMusicUrl:
    def on_get(self, req, resp):
        song_id = req.get_param('id', True)
        ne = NetEase()
        resp.body = json.dumps(ne.songs_detail_new_api([song_id]))


class NeteaseMusicLyric:
    def on_get(self, req, resp):
        song_id = req.get_param('id', True)
        ne = NetEase()
        resp.body = json.dumps(ne.song_lyric(song_id))


class NeteaseMusicDetails:
    def on_get(self, req, resp):
        song_id = req.get_param('id', True)
        ne = NetEase()
        resp.body = json.dumps(ne.songs_detail([song_id]))


api = falcon.API()
api.add_route('/songs/search', NeteaseMusicSearch())
api.add_route('/songs/details', NeteaseMusicDetails())
api.add_route('/songs/details/url', NeteaseMusicUrl())
api.add_route('/songs/details/lyric', NeteaseMusicLyric())
