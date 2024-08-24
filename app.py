from flask import Flask,render_template,jsonify

app = Flask(__name__)

jobs = [
  {
    "id": 1,
    "title": "Data Analyst",
    "location": "Bengaluru, India",
    "salary": "Rs. 10,00,000"
  },
  {
    "id": 2,
    "title": "Data Scientist",
    "location": "Hyderabad, India",
    "salary": "Rs. 15,00,000"
  },
  {
    "id": 3,
    "title": "Frontend Engineer",
    "location": "Remote",
    "salary": "Rs. 12,00,000"
  },
  {
    "id": 4,
    "title": "Backend Engineer",
    "location": "San Francisco, USA",
    "salary": "$150,000"
  },
  {
    "id": 5,
    "title": "Software Engineer", 
    "location": "Menlo Park, CA",
    "salary": "$100,000"
  },
  {
    "id": 6,
    "title": "Product Manager",
    "location": "San Francisco, USA",
    "salary": "$200,000"
  },
  {
    "id": 7,
    "title": "Frontend Developer",
    "location": "San Francisco, USA",
    "salary": "$100,000"
  },
  {
    "id": 8,
    "title": "Backend Developer",
    "location": "Remote",
    "salary": "$150,000"
  }
]


@app.route("/")
def hello_world():
  return render_template("home.html",jobs=jobs)

@app.route("/api/jobs")
def list_jobs():
  return jsoniify(jobs)

if __name__ == "__main__":
  app.run(debug=True)