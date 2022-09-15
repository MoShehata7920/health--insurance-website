from flask import Flask, render_template, request, redirect, url_for
from coree import add_hospital_core, add_new_customer_core, add_dependent_core
from hospitals_on_plane import hospitals_on_plane
from list_of_customers import get_list_of_customers
from veiw_claims import get_all_claims, get_uresolved_claims
from get_claim_details import get_claim_details
from mark_claim import mark_claim
from get_customer_id import get_customer_id
from core.db.db import db
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("main.html")




@app.route("/add_hospital")
def add_hospital():
    return render_template("add_hospital.html")

@app.route("/submit_add_new_hospital", methods = ['GET','POST'])
def submit_add_new_hospital():
    dirt_list = [request.form.get('basic'), request.form.get('premium'), request.form.get('golden')]
    clean_list = []
    for plane in dirt_list:
        if plane is not None:
            clean_list.append(plane)
    adding = add_hospital_core(request.form['name'], request.form['phone'], request.form['address'],
    request.form['email'], request.form['website'], *clean_list )
    return redirect(url_for('home'))

@app.route("/add_customer")
def add_customer():
    return render_template("add_customer.html")

@app.route("/submit_add_new_customer", methods = ['GET','POST'])
def submit_add_new_customer():
    print(request.form.get('gender'))
    add_new_customer_core(request.form['ssn'],request.form['name'], request.form['birth_date'], request.form.get('gender'),
     request.form['income'], request.form['address'], request.form['phone'], request.form['has_chronic_dis'], request.form['tall'], request.form['weight'], request.form['email'], request.form.get('plane') )
    return redirect(url_for('home'))

@app.route("/file_claim")
def file_claim():
    data = db('select H_id,H_name from hospital')
    return render_template("file_claim.html", data=data)

@app.route("/submit_file_claim", methods = ['GET','POST'])
def submit_file_claim():
    amount = request.form.get('amount')
    date =request.form.get('date')
    ssn = request.form.get('ssn')
    description= request.form.get('description')
    dependant = request.form.get('dependant')
    hospital= request.form.get('hospital')

    # if(dependant !=0 or dependant!="" or dependant !=None):
    #     return(dependant)
    # else:
    #     return ("fuck")

    # return("succefull submit")

   # query in mysql to save the request
    id = get_customer_id(ssn)
    db(f'''INSERT INTO insurance_claim (amount, date, description, mainly_for,hospital)  
                                VALUES({amount},"{date}","{description}",{id},{hospital});''')
    print("done")
    return render_template("successful.html", redirect = url_for('home'))

@app.route("/add_depndant")
def add_depndant():
    return render_template("add_depndant.html")

@app.route("/submit_add_new_dependent", methods = ['GET','POST'])
def submit_add_new_dependent():
    adding = add_dependent_core(request.form['ssn'],request.form['name'], request.form['birth_date'],request.form.get('plane'))
    if(adding == "successfuly"):
        return render_template("successful.html", redirect = url_for('home'))
    else:
        return "there is error please try again"


@app.route("/show_hospitals_<plane>")
def show_hospitals(plane):
    data = hospitals_on_plane(plane)
    return render_template("hospitals_on_planes.html", data = data, plane = plane)


@app.route("/view_customer")
def view_customer():
    data = get_list_of_customers()
    planes = {1: "Basic", 2:"Permium", 3: "Golden"}
    gender = {'M':"Male", 'F': "Female"}
    dis = {1:True, 0:False}
    my_list =[]
    for t in data:
        my_list.append(list(t))
    for x in my_list:
        x[12] = planes[x[12]]
        x[4] = gender[x[4]]
        x[8] = dis[x[8]]
    return render_template("view_customer.html", data = my_list)
   
@app.route("/view_all_claims")
def view_all_claims():
    
    data = get_all_claims()
    return render_template("view_claims.html", data = data)

@app.route("/view_unresolved_claims")
def view_unresolved_claims():
    data = get_uresolved_claims()
    return render_template("view_claims.html", data = data)

@app.route("/view_claims_<IC_id>")
def view_s_claims(IC_id):
    data = get_claim_details(IC_id)
    for s in data:
        data[0] = str(data[0])
    print(data)
    return render_template("view_s_claims.html", data = data)

@app.route("/accept_claim_<IC_id>")
def accept_claim(IC_id):
    data = mark_claim(True,IC_id)
    return redirect(url_for('view_all_claims'))

@app.route("/refuse_claim_<IC_id>")
def refuse_claim(IC_id):
    data = mark_claim(False,IC_id)
    return redirect(url_for('view_all_claims'))
if __name__ == "__main__":
    app.run(debug=True)
