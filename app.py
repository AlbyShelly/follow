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
        print(result)

        return redirect("/evangelist_list")

    else:

        return render_template("evangelist.html")

@app.route("/evangelist_list")
def evangelist_list():
    
    result = db.execute("SELECT * FROM evangelists")

    return render_template("evangelist_list.html", result=result)

@app.route("/single_evangelist_work")
def single_evangelist_work():
    return request.args.get("id")


@app.route("/new_work", methods=["GET", "POST"])
def new_work():

    if request.method == "POST":
        
        #list to hold our values
        work_list = []
        
        #loop to get all the data till end
        i = 0 #a counter variable                
        while True:

            if f'name_{i}' in request.form:
            
                currdict = {}
                currdict[f'name_{i}'] = request.form.get(f'name_{i}')
                currdict[f'age_{i}'] = request.form.get(f'age_{i}')
                currdict[f'address_{i}'] = request.form.get(f'address_{i}')

                #validate user input
                for _ in currdict.keys():
                    if not currdict[_]:
                        return "all the fields should be filled"

                i += 1

                print(currdict)
            else :
                break

        return "logged to terminal"

    else:
        
        #get the evangelist names and ids
        evangelists = db.execute(""" SELECT "id","name" FROM "evangelists" """)
        print(evangelists)
        return render_template("new_work.html", evangelists=evangelists)
