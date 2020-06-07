import datetime

def strftime(t, fmt):
    if type(t) is datetime.datetime:
        return t.strftime(fmt)
    else:
        return datetime.datetime.fromtimestamp(t).strftime(fmt)