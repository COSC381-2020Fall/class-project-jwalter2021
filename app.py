from flask import Flask, render_template, request, jsonify
import query_on_whoosh
import config
import math
import sqlite3
import smtplib

# turn this file (app.py) into a web app
app = Flask(__name__)
#app.config.update(dict(JSONIFY_PRETTYPRINT_REGULAR=True))

# I want to build an app that has a route that listens to /
@app.route("/")
def handle_slash():
    requested_name = request.args.get("name")
    return render_template("index.html", user_name=requested_name)    

@app.route("/query", strict_slashes=False)
def handle_query():
    query_term = request.args.get("q")
    page_index = int(request.args.get("p"))
    return jsonify({"query_term": query_term, "search_results": query_on_whoosh.query(query_term, current_page=page_index)})

@app.route("/query_view", strict_slashes=False)
def handle_query_view():

    query_term = request.args.get("q")
    if not query_term:
        query_term = ""

    page_index_arg = request.args.get("p")
    if not page_index_arg:
        page_index_arg = "1"

    if query_term != "":
        conn = sqlite3.connect('history.db')
        c = conn.cursor()
        c.execute("SELECT status FROM settings WHERE id=(SELECT MAX(ID) FROM settings);")
        checkbox = c.fetchone()
        if checkbox[0] == "enabled":
            c.execute("INSERT INTO search_terms (topic, term, search_time) VALUES ('Montessori', ?, datetime(strftime('%s','now'),'unixepoch'));", (query_term,))
        conn.commit()
        conn.close()

        page_index = int(page_index_arg)
        query_results = query_on_whoosh.query(query_term, current_page=page_index)
        search_results = query_results[0]
        results_cnt = int(query_results[1])
        page_cnt = math.ceil(results_cnt / 10)
        return render_template("query.html", results = search_results, page_cnt=page_cnt, query_term=query_term)

    else: 
        return render_template("query.html", page_cnt=0)

@app.route("/about", strict_slashes=False)
def handle_about():
    return render_template("about.html")

@app.route("/success", strict_slashes=False)
def handle_request():
    new_data = request.args.get("new_data")
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("j.rogalski3260@gmail.com", config.gmail_password)
    message = "Subject: {}\n\n{}".format("Request to add new data", "request to add: " + new_data)
    server.sendmail("j.rogalski3260@gmail.com", "j.rogalski3260@gmail.com", message)
    return render_template("success.html", new_data=new_data)

@app.route("/history", strict_slashes=False)
def handle_history():
    conn = sqlite3.connect('history.db')
    c = conn.cursor()
    c.execute("SELECT id, topic, term, search_time FROM search_terms ORDER BY search_time DESC;")
    rows = c.fetchall()
    conn.close()
    return render_template("history.html", history_list=rows)

@app.route("/remove_history", strict_slashes=False)
def handle_deletion():
    delRec = request.args.get("q")
    if not delRec:
        delRec = "1"
    conn = sqlite3.connect('history.db')
    c = conn.cursor()
    c.execute("DELETE FROM search_terms WHERE id = ?;", (delRec,))
    conn.commit()
    conn.close()
    return render_template("remove_history.html", delRec=delRec)

@app.route("/settings", strict_slashes=False)
def settings():
    return render_template("settings.html")

@app.route("/save_settings", strict_slashes=False)
def save_settings():
    checkbox = request.args.get('history')
    if checkbox == "on":
        checkbox = "enabled"
    else: checkbox = "disabled"
    conn = sqlite3.connect('history.db')
    c = conn.cursor()
    c.execute("INSERT INTO settings (status) VALUES (?);", (checkbox,))
    conn.commit()
    conn.close()
    return render_template("save_settings.html", value=checkbox)
