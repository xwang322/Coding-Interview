'''
设计类似 password recovery, http://www.1point3acres.com/bbs/thread-304325-1-1.html
useful link: https://softwareengineering.stackexchange.com/questions/15360/forgot-password-how-to-handle-this
https://stackoverflow.com/questions/1102781/best-way-for-a-forgot-password-implementation
ideas: a user table (user_id (int), account (string), password (string), createdAt(timestamp), ValidOrNot (bool), Secruity_Question(string), Secruity_Answer(string))
reset table(request_id (int), user_id (int), request_time(timestamp), state)
basic scenario: when a user forgot his password, hit "reset password" button, the system changes the user table his validity to false
then in the reset table, create a record for him, also generate a temp password for him.
How to generate? use a-z, A-Z, 0-9 total 62 to generate a 8 length string, send to his/her email
Before that, ask for verification of his email, account and secruity question answer, confirm with the database, if all correct, send him the temp password to his email
And set a time limit, every time the user hit the link and reset, change the request_time if less than say 24 hours, give him access, if he types the correct temp password.
Change the user table validity to True and suggests him to change the password. Temp will not be valid for more than 24 hours.
'''
#sendToEmail is defined outside, should be able to call directly, I guess
import datetime
import time
import string
import sys
def sendToEmail(email, contents):
    '''
    call some APIs to send to 'email' an email with 'contents'
    '''

class User(object):
    def __init__(self, account, email, password, validity, question, answer):
        self.account = account
        self.email = email
        self.password = password
        self.validity = True
        self.creation = datetime.datetime.now()
        self.question = question
        self.answer = answer

class UberTable(object):
    def __init__(self):
        self.users = {}
        self.id = 0

    def AddNewUser(self, user):
        # input user must be a User class
        self.users[self.id] = user
        self.id += 1

class ResetPassword(object):
    def __init__(self, owner_id):
        self.owner = owner_id
        self.creation = datetime.datetime.now()
        self.state = 'Not Sent'
        self.senttime = None
        # lock the user access, how do I able to access UserTable inside ResetPassword class
        UserTable[self.owner].validity = False

    def SecruityQuestion(self):
        return UserTable[self.owner].question

    def checkValidity(self, account, email, answer):
        if account == UserTable[self.owner].account and email == UserTable[self.owner].email and answer == UserTable[self.owner].answer:
            return True
        return False

    def SendTheRequest(self):
        if self.checkValidity:
            choices = string.ascii_letters + string.digits
            temp = ''.join(random.choice(choices) for i in range(8))
            self.temppassword = temp
            self.state = 'Sent'
            message = 'Your temp password is %s', temp
            sendToEmail(self.UerTable[self.owner].email, message)
            self.senttime = datetime.datetime.now()
        else:
            return 'Not Correct Answer'

    def ResetPassword(self):
        print 'Please Reset your new password:'
        newpassword = sys.stdin
        currenttime = datetime.datetime.now()
        if currenttime - self.senttime < datetime.timedelta(hours=24):
            UserTable[self.owner].validity = True
            UserTable[self.owner].password = newpassword
            self.state = 'Finished'
        else:
            self.state = 'Expired'
            return 'Temp Password expired, please request one more'
