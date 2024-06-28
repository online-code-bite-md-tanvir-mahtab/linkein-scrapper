# from playwright.sync_api import sync_playwright, Playwright
import json
from math import ceil
from time import sleep
import requests
from flask import Flask, jsonify, render_template, request, redirect


people_names = []
people_profile_url = []
people_job_company_names = []
token = '6WHUdgndzUt4P82WDcQ90bvH'

def parse_peoples(name, job_title,include_related_titles,exclude_job_titles,seniority,skills,years_in_current_role,total_years_experience,location,company,exclude_companies,company_size,min_revenue,max_revenue):
    url = "https://api.contactout.com/v1/people/search"
    headers = {
        
        'token': token
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
# Define the number of profiles per page
PROFILES_PER_PAGE = 10

@app.route('/', methods=['POST', 'GET'])
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
        profiles = parse_peoples(name, job_title, include_related_titles, exclude_job_titles, seniority, skills, years_in_current_role, total_years_experience, location, company, exclude_companies, company_size, min_revenue, max_revenue)

    # Pagination logic
    page = request.args.get('page', 1, type=int)
    total_profiles = len(profiles)
    num_pages = ceil(total_profiles / PROFILES_PER_PAGE)
    start_index = (page - 1) * PROFILES_PER_PAGE
    end_index = start_index + PROFILES_PER_PAGE
    paginated_profiles = dict(list(profiles.items())[start_index:end_index])

    return render_template('index.html', people=paginated_profiles, current_page=page, num_pages=num_pages, page_range=range(1, num_pages + 1))



@app.route('/company', methods=['GET', 'POST'])
def index():
    data = {}
    if request.method == 'POST':
        # Extract form data
        company = request.form.get('company')
        location = request.form.get('location')
        hq_only = request.form.get('hqLocationOnly') == 'on'
        industry = request.form.get('industry')
        company_size = request.form.get('companySize')
        revenue_min = request.form.get('revenueMin')
        revenue_max = request.form.get('revenueMax')
        technologies_used = request.form.get('technologiesUsed')
        year_founded_min = request.form.get('yearFoundedMin')
        year_founded_max = request.form.get('yearFoundedMax')
        domain = request.form.get('domain')
        keyword = request.form.get('keyword')
        print(company)
        # Create data payload for API request
        data = {
            "page": 1,
            "name": [company],
            # "domain": [domain],
            # "size": [company_size],
            # "hq_only": hq_only,
            # "location": [location],
            # "industry": [industry],
            # "min_revenue": int(revenue_min) if revenue_min else None,
            # "max_revenue": int(revenue_max) if revenue_max else None,
            # "year_founded_from": int(year_founded_min) if year_founded_min else None,
            # "year_founded_to": int(year_founded_max) if year_founded_max else None
        }

        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'basic',
            'token': token
        }

        response = requests.post("https://api.contactout.com/v1/company/search", headers=headers, json=data)
        results = {}
        data = {}
        # Handle the response
        if response.status_code == 200:
            results = response.json()
            print(results)
            return render_template('company.html', results=results['companies'])
        data = results
    
    return render_template('company.html', results=data)