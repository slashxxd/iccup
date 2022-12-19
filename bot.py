import requests
import threading
head = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
"cookie": "threads_read=a%3A23%3A%7Bi%3A1601892%3Bi%3A1671386673%3Bi%3A1603575%3Bi%3A1671386653%3Bi%3A1598491%3Bi%3A1671384293%3Bi%3A1603170%3Bi%3A1671387209%3Bi%3A1603744%3Bi%3A1671387180%3Bi%3A1603685%3Bi%3A1671378844%3Bi%3A1603767%3Bi%3A1671374836%3Bi%3A1603821%3Bi%3A1671374761%3Bi%3A1603372%3Bi%3A1671373652%3Bi%3A1603656%3Bi%3A1671270083%3Bi%3A1602448%3Bi%3A1671270016%3Bi%3A1603436%3Bi%3A1671216113%3Bi%3A1603691%3Bi%3A1671206918%3Bi%3A1603595%3Bi%3A1671206578%3Bi%3A1603501%3Bi%3A1671198086%3Bi%3A1603413%3Bi%3A1671197890%3Bi%3A1603647%3Bi%3A1671174518%3Bi%3A1602469%3Bi%3A1671128893%3Bi%3A1497630%3Bi%3A1671128891%3Bi%3A1603013%3Bi%3A1671113658%3Bi%3A1602442%3Bi%3A1671109508%3Bi%3A1602355%3Bi%3A1671097082%3Bi%3A1603159%3Bi%3A1671097077%3B%7D; forums_read=a%3A3%3A%7Bi%3A1033%3Ba%3A2%3A%7Bs%3A4%3A%22time%22%3Bs%3A10%3A%221671027760%22%3Bs%3A4%3A%22read%22%3Bb%3A1%3B%7Di%3A743%3Ba%3A2%3A%7Bs%3A4%3A%22time%22%3Bs%3A10%3A%221671206621%22%3Bs%3A4%3A%22read%22%3Bb%3A1%3B%7Di%3A701%3Ba%3A2%3A%7Bs%3A4%3A%22time%22%3Bi%3A1670178822%3Bs%3A4%3A%22read%22%3Bb%3A0%3B%7D%7D; media=screen; _ga=GA1.2.268213764.1665660534; _ym_uid=1665660539114445962; _ym_d=1665660539; newlang7=1; _gid=GA1.2.775531604.1671362115; _ym_isad=2; _ym_visorc=b; SID=68t71afna3vdb92aivr7t6bb97; _gat=1; last_session_new=b923254398e32014068ec126f428e6d1; last_session=cdc3a4fa75f27ad6a430a6791c280380",}

def r1():
    while True:
        requests.get("https://iccup.com/community/thread/1603767.html", headers=head)

def r2():
    while True:
        requests.get("https://iccup.com/community/thread/1603767.html", headers=head)

def r3():
    while True:
        requests.get("https://iccup.com/community/thread/1603767.html", headers=head)

def r4():
    while True:
        requests.get("https://iccup.com/community/thread/1603767.html", headers=head)

if __name__ == '__main__':
    t_1 = threading.Thread(target=r1)
    t_2 = threading.Thread(target=r2)
    t_3 = threading.Thread(target=r3)
    t_4 = threading.Thread(target=r4)
    t_1.start()
    t_2.start()
    t_3.start()
    t_4.start()