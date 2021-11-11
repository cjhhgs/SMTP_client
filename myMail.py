
class mailMessage():
    Subject = ''
    MainText = ""
    def __init__(self,Subject,Maintext):
        self.Subject = Subject
        self.MainText = Maintext

class myMail():
    From = ''
    Pass = ''
    User = ''
    To = ['']
    Message = mailMessage
    def __init__(self,From,Pass,User,To,Subject,MainText):
        self.From = From
        self.Pass = Pass
        self.User = User
        self.To = To
        message = mailMessage(Subject,MainText)
        self.Message = message
    
