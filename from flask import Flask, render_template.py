from flask import Flask, render_template, request, redirect

app = Flask(__name__)  

todo_liste = ["Aufgabe 1", "Aufgabe 2"]

@app.route("/add/<todo>")
def add(todo):
  todo_liste.append(todo)
  return "Das To Do " + todo + " ist hinzugefügt."

@app.route("/") 
def home():
  return render_template("home.html", todos = todo_liste)

@app.route("/add")
def add2():
  aufgabe = request.args["todo"]
  todo_liste.append(aufgabe)
  return redirect("/")

@app.route("/remove/<todo>") 
def remove(todo):
  if todo not in todo_liste:
    return "Das ToDo " + todo + " ist nicht verfügbar."
  else:
    todo_liste.remove(todo)
    return redirect("/")

app.run()      