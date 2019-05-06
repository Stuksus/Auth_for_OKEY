import requests
import urllib.parse
import random
headers={"Host": "www.okeydostavka.ru", "Origin": "https://www.okeydostavka.ru", "Referer": "ttps://www.okeydostavka.ru/webapp/wcs/stores/servlet/AjaxLogonForm?catalogId=12051&myAcctMain=1&langId=-20&storeId=10151", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.28 Safari/537.36 OPR/59.0.3199.0 (Edition developer)"}

def password(lenght):
    pas=''
    for i in range(lenght+1):
        pas+=random.choice(list('1234567890abcdefghigklmnopqrstuvyxwz'))
    return pas

def regestration(paramsMass,jsonTrue=0):#registration on the site

    url = 'https://www.okeydostavka.ru/wcs/resources/mobihub021/store/13154/loyalty/profile/profile'
    if jsonTrue==0:#create request with massive processing
         data = {
            "profile": {"firstName": paramsMass[0], "lastName": paramsMass[1], "email": paramsMass[2], "phone": str(paramsMass[3]),
                        "birthday": paramsMass[4], "middleName": paramsMass[5], "genderCode": paramsMass[6],
                        "password": paramsMass[7], "allowPersonalDataProcessing": "true", "allowEmail": "true",
                        "allowSms": "true"}}
    else:#create request with JSON processing
        data = {
            "profile": {"firstName": paramsMass['firstName'], "lastName": paramsMass['lastName'], "email": paramsMass['email'],
                        "phone": str(paramsMass['phone']),
                        "birthday": paramsMass['birthday'], "middleName": paramsMass['middleName'], "genderCode": paramsMass['genderCode'],
                        "password": paramsMass['password'], "allowPersonalDataProcessing": "true", "allowEmail": "true",
                        "allowSms": "true"}}

    res = requests.post(url, json=data, headers=headers)#send final request

def SecretKey(email):#get secret key(loginId) for logon
    emailUrl= urllib.parse.quote(email)#encode input string to URL-encription
    urlForLoginId = 'https://www.okeydostavka.ru/wcs/resources/mobihub021/store/10151/loyalty/profile/login?card=&email='+emailUrl+'&phone='#create request
    res=requests.get(urlForLoginId, headers=headers)#send final request
    loginId=str(res.text[12:-2])#get loginId fron response
    return loginId

def Session(loginKey,passw):#create session for authorization
    session = requests.Session()
    urlForLogon = 'https://www.okeydostavka.ru/webapp/wcs/stores/servlet/Logon'
    resTwo = session.post(urlForLogon,
                          {"storeId": "10151", "catalogId": "12051", "URL": "Fmsk", "reLogonURL": "LogonForm%3Ferror",
                           "errorViewName": "LogonForm", "logonId": loginKey, "logonPassword": str(passw)}, headers=headers) #возможно будет ошибка из за несоответсвия пароля
    return session

def confirmPhone(session, phoneNumber):
    url = 'https://www.okeydostavka.ru/wcs/resources/mobihub021/store/13154/loyalty/profile/profile'
    data = {"profile": {"phone":str(phoneNumber), "phoneUnconfirmed": "79039999999"}}
    res = session.put(url, json=data, headers=headers)
    # if res.text['nextActions'][0]=="CONFIRM_PHONE":
    #     return True
    # else:
    #     return False

def deleteAccount(session, emailTrue=0):
    if emailTrue==0:
        channel="S"
    else:
        channel="E"
    urlDel="https://www.okeydostavka.ru/wcs/resources/mobihub021/store/13154/loyalty/profile/block"
    dataDel={"confirmChannel":str(channel)}
    delRes=session.post(urlDel, json=dataDel, headers=headers)

def confirmCode(code, session, emailTrue=0):
    urlForConfirm="https://www.okeydostavka.ru/wcs/resources/mobihub021/store/13154/loyalty/profile/confirm"
    if emailTrue==0:
        channel="S"
    else:
        channel="E"
    dataForConfirm={"channel":str(channel),"code":int(code)}
    confirmSend=session.post(urlForConfirm, json=dataForConfirm, headers=headers)

