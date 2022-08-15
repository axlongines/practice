import xmlrpc.client
import functools


SERVER = "localhost"
PORT = 8069
DB_NAME = "practice"
USER = "admin"
PASSWORD = "admin"

ROOT = 'http://%s:%d/xmlrpc/' % (SERVER, PORT)
uid = xmlrpc.client.ServerProxy(ROOT + 'common').login(DB_NAME, USER, PASSWORD)
sock = functools.partial(xmlrpc.client.ServerProxy(ROOT + 'object').execute, DB_NAME, uid, PASSWORD)

model = "open.academy.session"
method = "search_read"
domain = []

list_session_before = sock(model,method,domain,["name","number_seats"])
print("BEFORE TO ADD")
for session in list_session_before:
    print("The name of the session is %s with the number of seats available is %r"%(session["name"],session["number_seats"]))

args = {
    'name':'sesion desde api',
    'number_seats':'111',
    'course_id':'2', 
}
new_session = sock(model,"create",args)

list_session_after = sock(model,method,domain,["name","number_seats"])
print("AFTER TO ADD")
for session in list_session_after:
   print("The name of the session is %s with the number of seats available is %r"%(session["name"],session["number_seats"]))