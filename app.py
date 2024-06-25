# from playwright.sync_api import sync_playwright, Playwright
from time import sleep
import pandas as pd
import requests
from flask import Flask, render_template, request, redirect


people_names = []
people_profile_url = []
people_job_company_names = []
datas = pd.DataFrame()



# def run(playwright: Playwright):
#     # Launch a browser (Chromium, Firefox, or WebKit)
#     browser = playwright.firefox.launch(headless=True, executable_path='firefox-1449/firefox/firefox.exe')  # Set headless=True to run in headless mode
#     # Create a new browser context
#     context = browser.new_context()
#     # Open a new page
#     page = context.new_page()
#     # Navigate to a URL
#     page.goto("http://www.linkedin.com/")
#     sleep(5)
#     # Interact with the page (e.g., take a screenshot)
#     # page.screenshot(path="screenshot.png")
    
#     is_visible = page.locator(selector='a[data-tracking-control-name="guest_homepage-basic_guest_nav_menu_people"]').is_visible()
#     sleep(3)
#     if is_visible:
#         people =  page.locator(selector='a[data-tracking-control-name="guest_homepage-basic_guest_nav_menu_people"]')
#         people.click()
#         sleep(5)
        
        
#     f_name_feild_is_visible = page.locator(selector='input[name="firstName"]').is_visible()
    
    
#     if f_name_feild_is_visible :
#         f_name_feild = page.locator(selector='input[name="firstName"]')
#         f_name_feild.click()
#         sleep(2)
#         f_name_feild.type('tanvir')
#         sleep(2)
#         page.locator(selector='button[data-tracking-control-name="people-guest_people-search-bar_base-search-bar-search-submit"]').click()
    
    
#     sleep(5)
#     items = page.query_selector_all(selector='li[class="pserp-layout__profile-result-list-item"]')
#     sleep(5)
#     for item in items:
#         urls = ''
#         name = ''
#         company = ''
#         try:
#             urls = item.query_selector(selector='a').get_property('href')
#         except :
#             urls = "not found"
#         try:
#             name = item.query_selector(selector='h3[class="base-search-card__title"]').text_content().strip()
#         except :
#             name = ''
#         try:
#             company = item.query_selector(selector='span[class="entity-list-meta__entities-list"]').text_content().strip()
#         except :
#             company = "Not employeed"
        
#         people_profile_url.append(urls)
#         people_names.append(name)
#         people_job_company_names.append(company)
        
#     print("the application is finished")
#     datas = pd.DataFrame(
#             {
#                 'url':people_profile_url,
#                 'name': people_names,
#                 'company': people_job_company_names
#             }
#         )
#     datas.to_csv('datas.csv',index=False)
#     # Close the browser context and browser
#     context.close()
#     browser.close()

# with sync_playwright() as playwright:
#     run(playwright)

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
        # "education": [
        #     "Doctorate Degree",
        #     "Vertapple University"
        # ],
        # "location": location,
        # "company": [
        #     "ContactOut"
        # ],
        # "exclude_companies": [
        #     "Google"
        # ],
        # "domain": [
        #     "https://contactout.com"
        # ],
        # "industry": [
        #     "Computer Software",
        #     "Computer Networking"
        # ],
        # "company_size": [
        #     "1_10",
        #     "11_50"
        # ],
        # "years_of_experience": [
        #     "6_10",
        #     "10"
        # ],
        # "years_in_current_role": [
        #     "8_10",
        #     "10"
        # ],
        # "current_company_only": False,
        # "data_types": [
        #     "personal_email",
        #     "work_email",
        #     "phone"
        # ],
        # "reveal_info": True
    }
    # payload = {
    #     "page": 1,
    

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
        # for data in profiles:
        #     # print(response.json()['profiles'][data].get('full_name')) 
        #     profile = profiles[data]
        #     # li_vanity = profile.get("li_vanity")
        #     full_name = profile.get("full_name")
        #     title = profile.get("title")
        #     headline = profile.get("headline")
        #     company = profile.get("company")
        #     company_name = company.get("name")
        #     # company_url = company.get("url")
        #     location = profile.get("location")
        #     # country = profile.get("country")
        #     # industry = profile.get("industry")
        #     experience = profile.get("experience")
        #     # education = profile.get("education", [])
        #     skills = profile.get("skills")
        #     # updated_at = profile.get("updated_at")
        #     # contact_availability = profile.get("contact_availability", {})
        #     # contact_info = profile.get("contact_info", {}) 
        return render_template('index.html', people=profiles)
    else:
        return render_template('index.html', people=profiles)

if __name__ == '__main__':
    app.run(debug=True)