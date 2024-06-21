from cs50 import SQL
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
db = SQL("sqlite:///follow.db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/evangelist", methods=["GET", "POST"])
def evangelist():
    
    if request.method == "POST":
            
        #get and validate inputs
        name = request.form.get("name")
        age = request.form.get("age")
        gender = request.form.get("gender")

        print(name, age, gender)

        if not name:
            return "enter a valid name"
        if not age:
            return "enter an age"
        if not gender:
            return "select a gender"
        
        #recording the input
        result = db.execute("""INSERT INTO "evangelists"("name", "age", "gender")
                             VALUES (?, ?, ?)""", name, age, gender)
        
        return redirect("/evangelist_list")

    else:

        return render_template("evangelist.html")

@app.route("/evangelist_list")
def evangelist_list():
    
    result = db.execute("SELECT * FROM evangelists")
    return render_template("evangelist_list.html", result=result)

@app.route("/single_evangelist_work")
def single_evangelist_work():

    #get evangelist id and contacts list
    evangelist_id = request.args.get("id")
    contacts = db.execute(""" SELECT "name", "age", "gender", "address", "last_contacted"
                              FROM "contacts"
                              WHERE "id" IN(
                                SELECT "contact_id" FROM "follow"
                                WHERE "evangelist_id" = ?
                              )
               """,evangelist_id
    )
    evangelist_name = db.execute("""SELECT "name" FROM "evangelists" WHERE "id" = ?""",evangelist_id)[0]["name"]
    print(evangelist_name)
    return render_template("single_evangelist_work.html", contacts = contacts, evangelist_name = evangelist_name)


@app.route("/new_work", methods=["GET", "POST"])
def new_work():

    if request.method == "POST":
        
        #list to hold our values
        work_list = []
        
        #get evangelist_id
        evangelist_id = request.form.get("evangelist_id")

        #loop to get all the data till end
        i = 0 #a counter variable               
        while True:

            if f'name_{i}' in request.form:
            
                currdict = {}
                currdict["name"] = request.form.get(f'name_{i}')
                currdict["age"] = request.form.get(f'age_{i}')
                currdict["address"] = request.form.get(f'address_{i}')
                currdict["gender"] = request.form.get(f'gender_{i}')

                #validate user input

                if not evangelist_id:
                    return "please choose and evangelist to continue"

                for _ in currdict.keys():
                    if not currdict[_]:
                        return "all the fields should be filled"

                i += 1

                work_list.append(currdict)
            else :
                break


        #insert the data to database
        for row in work_list:
            db.execute("INSERT INTO contacts (name, age, address, gender) VALUES (?,?,?,?)",
                       row["name"], row["age"], row["address"],row["gender"])

            contact_id = db.execute(""" SELECT "seq" FROM "sqlite_sequence" WHERE "name" = 'contacts'""")[0]["seq"]
            result = db.execute(""" INSERT INTO "follow" ("evangelist_id", "contact_id") VALUES (?,?)""", evangelist_id, contact_id)
            print(result)
        return redirect("/evangelist_list")

    else:
        
        #get the evangelist names and ids
        evangelists = db.execute(""" SELECT "id","name" FROM "evangelists" """)
        return render_template("new_work.html", evangelists=evangelists)

@app.route("/current_status")
def current_status():
    
    #query to get all the important details
    rows =db.execute( """   SELECT "ename", "name" AS "cname", "age" AS "cage", "address", "last_contacted", "cid"
                            FROM "contacts" JOIN
	                            (SELECT "evangelists"."id" AS "eid", "evangelists"."name" AS "ename", "contact_id" AS "cid"
	                            FROM "evangelists" JOIN "follow"
            	                ON "evangelists"."id" = "follow"."evangelist_id") AS "t1"
                            ON "contacts"."id" = "t1"."cid" 
          """
    )
    
    return render_template("current_status.html", rows=rows)

