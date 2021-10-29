
class mailMessage():
    Subject = ''
    MainText = ""
    def __init__(self,Subject,Maintext):
        self.Subject = Subject
        self.MainText = Maintext

class myMail():
    From = ''
    Pass = ''
    To = ['']
    Message = mailMessage
    def __init__(self,From,Pass,To,Subject,MainText):
        self.From = From
        self.Pass = Pass
        self.To = To
        message = mailMessage(Subject,MainText)
        self.Message = message
    
