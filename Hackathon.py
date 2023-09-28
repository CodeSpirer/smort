import mysql.connector as mc
import time

pname = "Sendhil"
pdept = "Cardiology"
pdoc  = "Blessy Mathew"
ctime = time.ctime()[11:-8]
#ctime = "14:30"


def appoint(pname, pdept, pdoc, ctime):
    
    conn = mc.connect(user="root", password="root",
                      host="localhost", database="hospital")
    cur = conn.cursor()

    sql = "SELECT * FROM doctors"

    cur.execute(sql)

    doctors = cur.fetchall()
    
    L = []
    for i in doctors:
        L.append(list(i))

    
    def schedule(dept, doc):
        conn = mc.connect(user="root", password="root",
                          host="localhost", database="hospital")
        cur = conn.cursor()
        vals = (pname, dept, doc)
        sql = "INSERT INTO patients(name, dept, doctor) VALUES(%s, %s, %s)"
        cur.execute(sql, vals)
        conn.commit()
        cur.close()
        conn.close()

    doc_avail = True
    dept_avail = True
    general_avail = True

    for i in L:
        if i[1] == pdoc: 
            if str(i[4]) > ctime and i[5] > 0:
                print("Your Appointment with Dr.", i[1], "(", i[2], ")", "is scheduled.")
                schedule(i[2], i[1])
                doc_avail = True
            else:
                doc_avail = False

    if not doc_avail:
        for i in L:
            if i[2] == pdept:
                if str(i[4]) > ctime and i[5] > 0:
                    print("Your Appointment with Dr.", i[1], "(", i[2], ")", "is scheduled.")
                    schedule(i[2], i[1])
                    dept_avail = True
                else:
                    dept_avail = False

    if not dept_avail:
        for i in L:
            if i[2] == 'General':
                if str(i[4]) > ctime and i[5] > 0:
                    print("Your Appointment with Dr.", i[1], "(", i[2], ")", "is scheduled.")
                    schedule(i[2], i[1])
                    general_avail = True
                else:
                    general_avail = False

    if not general_avail:
        print("Doctor Not Available Today")


appoint(pname, pdept, pdoc, ctime)
