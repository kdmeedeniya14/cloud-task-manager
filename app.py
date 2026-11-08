from flask import Flask, jsonify, request

app = Flask(__name__)

# Temporary storage for tasks

tasks = {
1: {
"id": 1,
"title": "Learn Python",
"status": "Pending"
},
2: {
"id": 2,
"title": "Learn AWS",
"status": "In Progress"
}
}

# Home endpoint

@app.route("/", methods=["GET"])
def home():
    return jsonify({
"message": "Welcome to my Cloud Task Manager API!",
"project": "Cloud Task Manager",
"status": "Running"
}), 200

# Health check endpoint

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
"status": "healthy"
}), 200

# GET: View all tasks

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(list(tasks.values())), 200

# GET: View one task

@app.route("/tasks/[int:task_id](int:task_id)", methods=["GET"])
def get_task(task_id):
    task = tasks.get(task_id)


    if task is None:
        return jsonify({"error": "Task not found"}), 404

    return jsonify(task), 200


from flask import Flask, jsonify, request

app = Flask(__name__)

# Temporary storage for tasks

tasks = {
1: {
"id": 1,
"title": "Learn Python",
"status": "Pending"
},
2: {
"id": 2,
"title": "Learn AWS",
"status": "In Progress"
}
}

# Home endpoint

@app.route("/", methods=["GET"])
def home():
    return jsonify({
"message": "Welcome to my Cloud Task Manager API!",
"project": "Cloud Task Manager",
"status": "Running"
}), 200

# Health check endpoint

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
"status": "healthy"
}), 200

# GET: View all tasks

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(list(tasks.values())), 200

# GET: View one task


@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = tasks.get(task_id)

    if task is None:
        return jsonify({"error": "Task not found"}), 404

    return jsonify(task), 200




# POST: Create a new task
@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "A JSON object is required"}), 400

    title = data.get("title")
    status = data.get("status", "Pending")

    if not isinstance(title, str) or not title.strip():
        return jsonify({"error": "A task title is required"}), 400

    if not isinstance(status, str) or not status.strip():
        return jsonify({"error": "Status must be a non-empty string"}), 400

    new_id = max(tasks.keys(), default=0) + 1

    new_task = {
        "id": new_id,
        "title": title.strip(),
        "status": status.strip()
    }

    tasks[new_id] = new_task

    return jsonify(new_task), 201


# PUT: Update an existing task
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = tasks.get(task_id)

    if task is None:
        return jsonify({"error": "Task not found"}), 404

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "A JSON object is required"}), 400

    if "title" in data:
        if not isinstance(data["title"], str) or not data["title"].strip():
            return jsonify({"error": "Title must be a non-empty string"}), 400

        task["title"] = data["title"].strip()

    if "status" in data:
        if not isinstance(data["status"], str) or not data["status"].strip():
            return jsonify({"error": "Status must be a non-empty string"}), 400

        task["status"] = data["status"].strip()

    return jsonify(task), 200






# DELETE: Delete a task
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = tasks.pop(task_id, None)

    if task is None:
        return jsonify({"error": "Task not found"}), 404

    return jsonify({
        "message": "Task deleted successfully",
        "task": task
    }), 200




# Start the application

if __name__ == "__main__":
    app.run(debug=True)






