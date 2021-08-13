import requests
from urllib.parse import urlparse, urljoin, quote
from bs4 import BeautifulSoup
import re
from params import params 


headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
           "Referer": "http://challenge01.root-me.org/web-serveur/ch34/?action=login",
           "Accept-Encoding": "gzip, deflate",
           "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,fr;q=0.7"}


DBMS_ERRORS = {
    "": ("ERROR:  syntax error at or near", ),
    "MySQL": ("SQL syntax.*MySQL", "Warning.*mysql_.*", "valid MySQL result", "MySqlClient\."),
    "PostgreSQL": ("PostgreSQL.*ERRO", "Warning.*\Wpg_.*", "valid PostgreSQL result", "Npgsql\."),
    "Microsoft SQL Serve": ("Driver.* SQL[\-\_\ ]*Serve", "OLE DB.* SQL Serve", "(\W|\A)SQL Server.*Drive", "Warning.*mssql_.*", "(\W|\A)SQL Server.*[0-9a-fA-F]{8}", "(?s)Exception.*\WSystem\.Data\.SqlClient\.", "(?s)Exception.*\WRoadhouse\.Cms\."),
    "Microsoft Access": ("Microsoft Access Drive", "JET Database Engine", "Access Database Engine"),
    "Oracle": ("\bORA-[0-9][0-9][0-9][0-9]", "Oracle erro", "Oracle.*Drive", "Warning.*\Woci_.*", "Warning.*\Wora_.*"),
    "IBM DB2": ("CLI Driver.*DB2", "DB2 SQL erro", "\bdb2_\w+\("),
    "SQLite": ("SQLite/JDBCDrive", "SQLite.Exception", "System.Data.SQLite.SQLiteException", "Warning.*sqlite_.*", "Warning.*SQLite3::", "\[SQLITE_ERROR\]"),
    "Sybase": ("(?i)Warning.*sybase.*", "Sybase message", "Sybase.*Server message.*"),
}


def quote_test(url, param, method='GET', cookies={}):
    if method.upper() == "GET":
        code = requests.get(url, cookies=cookies, headers=headers).status_code
        if code != 200:
            print(f"[-] \" {url} \"  : ", code)
            return -1
        r = requests.get(url, params={param: "'"},
                         cookies=cookies, headers=headers)
        if r.status_code != 200:
            return (True, '')
        for db in DBMS_ERRORS:
            for error in DBMS_ERRORS[db]:
                if db != '':
                    x = re.search(error, r.text)
                else:
                    x = error in r.text
                if x:
                    return (True, db)
        return (False, '')
    if method.upper() == "POST":
        code = requests.post(url, cookies=cookies, headers=headers).status_code
        if code != 200:
            print(f"[-] \" {url} \"  : ", code)
            return -1
        r = requests.post(url, params={param: "'"},
                          cookies=cookies, headers=headers)
        if r.status_code != 200:
            return (True, '')
        for db in DBMS_ERRORS:
            for error in DBMS_ERRORS[db]:
                if db != '':
                    x = re.search(error, r.text)
                else:
                    x = error in r.text
                if x:
                    return (True, db)
        return (False, '')


def Boolean_conditions_Test(url, param, method='GET', cookies={}):
    if method.upper() == "GET":
        r1 = requests.get(
            url, params={param: "'+or+1=1--"}, cookies=cookies, headers=headers)
        r2 = requests.get(
            url, params={param: "'+or+1=2--"}, cookies=cookies, headers=headers)
        if (r1.status_code, r2.status_code) != (200, 200):
            return False
        if (len(r1.text) != len(r2.text)):
            return True
        return False
    if method.upper() == "POST":
        r1 = requests.post(
            url, params={param: "'+or+1=1--"}, cookies=cookies, headers=headers)
        r2 = requests.post(
            url, params={param: "'+or+1=2--"}, cookies=cookies, headers=headers)
        if (r1.status_code, r2.status_code) != (200, 200):
            return False
        if (len(r1.text) != len(r2.text)):
            return True
        return False


def SQLi(url, cookies={}):
    ret = {}
    paramss = params(url)
    GET=paramss["get"]
    for i in GET:
        path = GET[i]
        P=i
        if type(P) == type(tuple()):
            for j in P:
            	ret[urljoin(url, path)+"?"+j+"="] = Boolean_conditions_Test(urljoin(url, path), j, 'GET', cookies) or  quote_test(urljoin(url, path), j, 'GET', cookies)
        else:
            ret[urljoin(url, path)+"?"+P +"="] = quote_test(urljoin(url, path), P, 'GET', cookies)
            ret[urljoin(url, path)+"?"+P+"="] = ret[urljoin(url, path)+"?"+P+"="] or Boolean_conditions_Test(urljoin(url, path), P, 'GET', cookies)
    POST=paramss["post"]        
    for i in POST:
        path = POST[i]
        P=i
        if type(P) == type(tuple()):
            for j in P:
            	ret[urljoin(url, path)+"?"+j+"="] = Boolean_conditions_Test(urljoin(url, path), j, 'POST', cookies) or  quote_test(urljoin(url, path), j, 'POST', cookies)
        else:
            ret[urljoin(url, path)+"?"+P +"="] = quote_test(urljoin(url, path), P, 'POST', cookies)
            ret[urljoin(url, path)+"?"+P+"="] = ret[urljoin(url, path)+"?"+P+"="] or Boolean_conditions_Test(urljoin(url, path), P, 'POST', cookies)
    return ret


