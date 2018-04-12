'''
design quora
第一轮：国人大哥系统设计，问如何设计stackoverflow。重点在于设计如何在后段存储answer，用什么metric对answer进行排序，如何处理最新添加的answer。
'''
# useful link: http://highscalability.com/stack-overflow-architecture
# ideas: scenario: roughly everyday 10000 new questions posted, everyday 100000 questions answer, every day 5000000 reviews
# Write QPS: 1. Read QPS: 100. NoSQL is enough. Mostly read intensive, a little bit write intensive workload.
# service: somebody posted a question, other can answer, or vote for/against some answer. Should count the votes for every answer, return the answer based on votes desending order
# search for some question, edit some answer for some question, some other like most hot topic today, this month, this year....Share by other platform...
# DB design, a user table, a question table, an answer table.
# User table: user_id, account, password, createdAt, rating
# Question table: question_id, owner_id, content, createdAt
# Answer table: answer_id, question_id, vote_for_number, vote_against_number, last_modified_time, record_of_edited
# OOD part, how to store the information, similar to LC 432 for efficiency
import collections
class User(object):
    def __init__(self, id, name):
        self.user_id = id
        self.rating = 0
        self.name = name
        self.questions = collections.defaultdict(list)
        self.questionTotal = 0
        self.answers = collections.defaultdict(list)
        self.answerTotal = 0

    def UserAskQuestion(self, question):
        if not question:
            return
        self.questions[self.questionTotal].append(question)
        self.questionTotal += 1

    def AnswerQuestion(self, answer):
        self.answers[self.answerTotal].append(answer)
        self.answerTotal += 1

class StackOverFlow(object):
    def __init__(self):
        self.user_table = {}
        self.name_id = {}
        self.question_table = {}
        self.answer_table = {}
        self.total_user = 0
        self.total_question = 0
        self.total_answer = 0
        self.DoubleLL = {}
        self.question_answer = collections.defaultdict(list)
        self.answer_question = {}
        self.answer_user = {}
        self.question_user = {}
        self.voting_record = set()

    def RegisterUser(self, name):
        newUser = User(self.total_user, name)
        self.user_table[self.total_user] = newUser
        self.name_id[name] = self.total_user
        self.total_user += 1

    def SomebodyAskQuestion(self, name, question):
        user_id = self.name_id[name]
        if user_id not in self.user_table:
            return
        self.user_table[user_id].UserAskQuestion(question)
        self.question_table[self.total_question] = question
        #self.DoubleLL[self.total_question] = QuestionAnswer(question)
        self.question_answer[self.total_question] = []
        self.question_user[self.total_question] = user_id
        self.total_question += 1

    def SomebodyAnswerQuestion(self, name, question_id, answer):
        user_id = self.name_id[name]
        if user_id not in self.user_table or question_id not in self.question_table:
            return
        self.user_table[user_id].AnswerQuestion(answer)
        self.answer_table[self.total_answer] = answer
        self.question_answer[question_id].append(self.total_answer)
        self.answer_question[self.total_answer] = question_id
        self.answer_user[self.total_answer] = user_id
        self.total_answer += 1
        #self.DoubleLL[question_id].inc(answer)

    def SomebodyVoteForSomeAnswer(self, name, answer_id):
        user_id = self.name_id[name]
        if user_id not in self.user_table or answer_id not in self.answer_table:
            return
        # prevent somebody keeps voting
        if (name, answer_id) in self.voting_record:
            return
        # prevent somebody votes for him/herself
        if user_id == self.answer_user[answer_id]:
            return
        question_id = self.answer_question[answer_id]
        #self.DoubleLL[question_id].inc(self.answer_table[answer_id])
        self.user_table[self.answer_user[answer_id]].rating += 1
        self.voting_record.add((name, answer_id))

    def SomebodyVoteAgainstSomeAnswer(self, name, answer_id):
        user_id = self.name_id[name]
        if user_id not in self.user_table or answer_id not in self.answer_table:
            return
        # prevent somebody keeps voting
        if (name, answer_id) in self.voting_record:
            return
        # prevent somebody votes for him/herself
        if user_id == self.answer_user[answer_id]:
            return
        question_id = self.answer_question[answer_id]
        #self.DoubleLL[question_id].inc(self.answer_table[answer_id])
        self.user_table[self.answer_user[answer_id]].rating -= 1
        self.voting_record.add((name, answer_id))


app = StackOverFlow()
app.RegisterUser('Alice')
app.RegisterUser('Bob')
app.RegisterUser('Mike')
app.SomebodyAskQuestion('Bob', 'Why is Uber interview so hard?')
app.SomebodyAskQuestion('Mike', 'When can I graduate?')
app.SomebodyAskQuestion('Alice', 'Why is ECE so shit?')
app.SomebodyAskQuestion('Alice', 'When can I get an offer?')
#print app.name_id
#print app.question_table
#print app.user_table[app.name_id['Alice']].questions
app.SomebodyAnswerQuestion('Bob', 0, 'Because Uber is No.1 startup.')
app.SomebodyAnswerQuestion('Bob', 1, 'Sometime during the summer.')
app.SomebodyAnswerQuestion('Alice', 0, 'Because they feel good about themselves.')
app.SomebodyAnswerQuestion('Alice', 3, 'When you get, you get.')
app.SomebodyAnswerQuestion('Alice', 1, 'After you are done with all this.')
app.SomebodyAnswerQuestion('Alice', 2, 'Because they do not care about others.')
app.SomebodyAnswerQuestion('Mike', 2, 'Because they do not care about retired professors.')
#print app.answer_table
#print app.answer_question
#print app.question_answer
#print app.user_table[app.name_id['Alice']].answers
app.SomebodyVoteForSomeAnswer('Bob', 3)
app.SomebodyVoteForSomeAnswer('Bob', 3)
app.SomebodyVoteForSomeAnswer('Bob', 3)
print app.user_table[app.name_id['Alice']].rating
app.SomebodyVoteForSomeAnswer('Mike', 3)
app.SomebodyVoteForSomeAnswer('Alice', 3)
print app.user_table[app.name_id['Alice']].rating





class Node(object):
    def __init__(self, count):
        self.count = 0
        self.prev = None
        self.next = None
