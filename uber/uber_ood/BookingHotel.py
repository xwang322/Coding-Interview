'''
旅馆预订系统，写程序，烙印，要自己设计几个类，和预定，删除，和给出一天，返回空房树，不难，
但很多不确定的，烙印也不给力，想他确认，他就说你看怎么好。
'''
# not enough time to prepare, but share some thoughts
class User {
    int user_id;
    string user_name;
    set booking_history = set(time)
    set checkedin_history = set(time);
    string state {'checked_in','ckecked_out','idle'}
}
class Room {
    int floor_level;
    int room_id;
    string size;
    hashmap root_reverse_time = {time: user_id};
    hashmap room_checkin_time = {time: user_id};
    string root_current_state = {'taken','empty'} [0, 1]
}

class Hotel{
    def __init__(self):
        self.rooms = Room()
        self.large = []
        self.small = []
        self.medium = []
        # assign a heap for fast search

    def UserBookRoom(self, user_id, size, time):
        FindIfAvaiable(size, time)
        # change corresponding room and user class instance

    def FindIfAvailable(self, size, time):
        # check if every room in corresponding array has time in the corresponding reverse dictionary

    def UserCancelRoom(self, user_id, size):
        # check if it is in record, if so, change corresponding state

}
