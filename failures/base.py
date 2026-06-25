import datetime
import inspect


class FailureBase(Exception):

    def __init__(self, code: int, message: str):
        # lineno, funcname, filename of err location, recur till not by init
        for frame in inspect.stack():
            if frame.function == "__init__": break
            self.filename = frame.filename
            self.lineno = frame.lineno
            self.funcname = frame.function

        nowtime = datetime.datetime.now()
        self.message = message
        self.code = code
        self.epoch = int(nowtime.timestamp())
        self.local_time = nowtime.strftime("%Y-%m-%d %H:%M:%S")
        
        super().__init__(f"[{self.epoch}] {self.filename::self.funcname::self.lineno} => {self.code} {self.message}")


    def __str__(self):
        return f"DateTime: {{self.epoch : self.local_time}}, Code: {self.code}, Message: {self.message}"
        

