from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


task_list = []

def add_task(task):
    task_list.append(task)

def get_tasks():
    return task_list


@app.route("/" , methods = ["GET"])
def get_task_route():
    return render_template("index2.html" , task_list = get_tasks())


@app.route("/add_task", methods=["POST"])
def add_task_route():
    task = request.form.get("task")
    if task:
        add_task(task)
    return redirect(url_for("get_task_route"))



if __name__ == "__main__":
    app.run(debug=True)