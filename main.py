"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""
from flask import Flask, render_template, request, redirect, send_file
from so import get_so_jobs
from remoteok import extract_remo_job,get_remo_soup
from weworkremotely import get_wewo_soup,extract_wewo_jobs
# # so job 가져오기
# last = last_so_page()
# print(extract_so_jobs(last))
# # remote job 가져오기
# soup = get_remo_soup()
# print(extract_remo_job(soup))
# # 나머지 가져오기
# soup = get_wewo_soup()
# print(extract_wewo_jobs(soup))



app = Flask("MultiScrapper")
db = {}
@app.route("/")
def home():
   
  return render_template('home.html')

@app.route("/report")
def report():
  word = request.args.get('word')
  jobs = get_so_jobs(word)

  return render_template('report.html',word=word,jobs=jobs)


app.run(host="0.0.0.0")
