'''
第一轮design：
面试官应该是中东小哥但听口音是美国长大，题目是design一个音乐播放器比如spotify，问题比较open，
我问了他需要哪些功能，他说playlist, pause, shuffle, next song, previous song之类的，具体记不太清了。
因为是design，所以我就用python写了一个media_player class，顺便假设了一些api可以用，代码并不用runnable，
只要大概框架正确就行了。这一轮应该是面的最顺利的了，小哥非常友好，最后跟他聊了一些uber工作的经历等等。

第三轮 讨论project+system design，设计music player
1. design music player，问了很多networking的东西，TCP/IP, HTTP, Security之类的
The design is in photos. Check about network related stuff.
'''
import random
import heapq
import collections
def playSong(song_id):
def PauseSong():
class User(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.playlist = []
        self.currentsong = 0
        self.history = []
        self.state = 'idle'
        self.totallistened = 0

    def AddToPlayList(self, song_id):
        self.playlist.append(song_id)

    def PlayPlaylist(self):
        self.state = 'active'
        for i in range(len(self.playlist)):
            self.currentsong = i
            PlaySong(self.playlist[i])
            self.totallistened += 1
            self.history.append(self.playlist[i])
        self.state = 'done'

    def ShufflePlayList(self):
        # use Knuth algorithm
        for i in range(len(self.playlist)-1, -1, -1):
            temp = random.randint(0, i+1)
            self.playlist[i], self.playlist[temp] = self.playlist[temp], self.playlist[i]

    def ResetPlaylist(self):
        self.playlist = []

    def PlayNextSong(self):
        PauseSong()
        if currentsong != len(self.playlist)-1:
            self.currentsong += 1
            PlaySong(self.playlist[self.currentsong])
        self.state = 'done'

    def PlayPreviousSong(self):
        PauseSong()
        if not self.currentsong:
            self.currentsong -= 1
            PlaySong(self.playlist[self.currentsong])
        self.state = 'done'


class Song(object):
    def __init__(self, id, name, composer, category):
        self.id = id
        self.name = name
        self.composer = composer
        self.category = category
        self.totalplayedtime = 0

class media_player(object):
    def __init__(self):
        self.users = []
        self.songs = []
        self.playhistory = {}
        self.totaluser = 0
        self.totalsong = 0
        self.heap = []
        self.top10list = []
        self.playedFrequency = colections.defaultdict(list)

    def RegisterUser(self):
        new_user = User(self.totaluser, 'Alice')
        self.users.append(new_user)
        self.totaluser += 1

    def AddNewSong(self):
        new_song = Song(self.totalsong, 'Jump', 'Justin Bieber', 'hip-pop')
        self.song.append(new_song)
        self.totalsong += 1

    def GeneratePlayListforUser(self, user_id):
        # assume a playlist has 10 songs
        lists = [random.randint(0, self.totalsong) for i in range(10)]
        User(user_id).AddToPlayList(lists)

    def UserPlayPlaylist(self, user_id):
        prev = User(user_id).history
        while User(user_id).state != 'done':
            User(user_id).PlayPlaylist(User(user_id).playlist)
        curr = User(user_id).history
        diff = curr[len(prev):]
        for each in diff:
            self.playhistory[each] = self.playhistory.get(each, 0) + 1
            self.playedFrequency[self.playhistory[each]].append(each)
            self.playedFrequency[self.playhistory[each]-1].remove(each)

    def GetTop10Songs(self):
        self.top10list = sorted(self.playedFrequency, reverse = True)[0:10].values()
