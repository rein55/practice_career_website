from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
      'Id':1,
      'Title':'Python Developer',
      'Location':'New York',
      'Salary':'$100,000'
    },
    {
      'Id':2,
      'Title':'Data Analyst',
      'Location':'Canada',
      'Salary':'$150,000'
    },
    {
      'Id':3,
      'Title':'Data Scientist',
      'Location':'Los Angeles',
      'Salary':'$120,000'
    },
    {
      'Id':4,
      'Title':'Backend Engineer',
      'Location':'San Francisco',
    }
]

@app.route("/")
def hello_world():
  return render_template('home.html',
                         jobs=JOBS,
                        company_name = 'Career Website')
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
if __name__ == "__main__":
  app.run(host= "0.0.0.0", debug=True)