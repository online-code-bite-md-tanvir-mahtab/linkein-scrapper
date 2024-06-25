# from playwright.sync_api import sync_playwright, Playwright
from time import sleep
import pandas as pd
import requests
from flask import Flask, render_template, request, redirect


people_names = []
people_profile_url = []
people_job_company_names = []
datas = pd.DataFrame()


def parse_peoples(name, job_title,include_related_titles,exclude_job_titles,seniority,skills,years_in_current_role,total_years_experience,location,company,exclude_companies,company_size,min_revenue,max_revenue):
    url = "https://api.contactout.com/v1/people/search"
    headers = {
        
        'token': 'Y8CXbgb7I3FXZA7xuoNi5EkK'
    }
    payload = {
        "name": name,
        "job_title": job_title,
        "exclude_job_titles": exclude_job_titles,
        "current_titles_only": False,
        "include_related_job_titles": include_related_titles,
        "skills": skills,

    }

    response = requests.post(url, headers=headers, json=payload)
    profiles = response.json()['profiles']
    return profiles


# ========fontend part========


app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
def home():
    profiles = {}
    if request.method == 'POST':
        name = request.form.get('name')
        job_title = request.form.get('job_title')
        include_related_titles = request.form.get('include_related_titles')
        exclude_job_titles = request.form.get('exclude_job_titles')
        seniority = request.form.get('seniority')
        skills = request.form.get('skills')
        years_in_current_role = request.form.get('years_in_current_role')
        total_years_experience = request.form.get('total_years_experience')
        location = request.form.get('location')
        company = request.form.get('company')
        exclude_companies = request.form.get('exclude_companies')
        company_size = request.form.get('company_size')
        min_revenue = request.form.get('min_revenue')
        max_revenue = request.form.get('max_revenue')
        profiles = parse_peoples(name, job_title,include_related_titles,exclude_job_titles,seniority,skills,years_in_current_role,total_years_experience,location,company,exclude_companies,company_size,min_revenue,max_revenue)
        return render_template('index.html', people=profiles)
    else:
        return render_template('index.html', people=profiles)

if __name__ == '__main__':
    app.run(debug=True)