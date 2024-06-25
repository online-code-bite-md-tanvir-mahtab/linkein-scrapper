import requests


def parse_peoples():
    url = "https://api.contactout.com/v1/people/search"
    headers = {
        
        'token': 'Y8CXbgb7I3FXZA7xuoNi5EkK'
    }
    payload = {
        "name": "tanvir"
    }
    # payload = {
    #     "page": 1,
    #     "name": "John Smith",
    #     "job_title": [
    #         "Vice President",
    #         "VP Of Product"
    #     ],
    #     "exclude_job_titles": [
    #         "Sales"
    #     ],
    #     "current_titles_only": False,
    #     "include_related_job_titles": False,
    #     "skills": [
    #         "Network Security",
    #         "Networking"
    #     ],
    #     "education": [
    #         "Doctorate Degree",
    #         "Vertapple University"
    #     ],
    #     "location": [
    #         "Sydney, Australia"
    #     ],
    #     "company": [
    #         "ContactOut"
    #     ],
    #     "exclude_companies": [
    #         "Google"
    #     ],
    #     "domain": [
    #         "https://contactout.com"
    #     ],
    #     "industry": [
    #         "Computer Software",
    #         "Computer Networking"
    #     ],
    #     "company_size": [
    #         "1_10",
    #         "11_50"
    #     ],
    #     "years_of_experience": [
    #         "6_10",
    #         "10"
    #     ],
    #     "years_in_current_role": [
    #         "8_10",
    #         "10"
    #     ],
    #     "current_company_only": False,
    #     "data_types": [
    #         "personal_email",
    #         "work_email",
    #         "phone"
    #     ],
    #     "reveal_info": True
    # }

    response = requests.post(url, headers=headers, json=payload)

    for data in response.json()['profiles']:
        # print(response.json()['profiles'][data].get('full_name')) 
        profile = response.json()['profiles'][data]
        li_vanity = profile.get("li_vanity")
        full_name = profile.get("full_name")
        title = profile.get("title")
        headline = profile.get("headline")
        company = profile.get("company")
        company_name = company.get("name")
        company_url = company.get("url")
        location = profile.get("location")
        country = profile.get("country")
        industry = profile.get("industry")
        experience = profile.get("experience")
        education = profile.get("education")
        skills = profile.get("skills")
        updated_at = profile.get("updated_at")
        contact_availability = profile.get("contact_availability")
        contact_info = profile.get("contact_info") 
        print(f"LinkedIn Vanity: {li_vanity}")
        print(f"Full Name: {full_name}")
        print(f"Title: {title}")
        print(f"Headline: {headline}")
        print(f"Company Name: {company_name}")
        print(f"Company URL: {company_url}")
        print(f"Location: {location}")
        print(f"Country: {country}")
        print(f"Industry: {industry}")
        print(f"Experience: {experience}")
        print(f"Education: {education}")
        print(f"Skills: {skills}")
        print(f"Updated At: {updated_at}")
        print(f"Contact Availability: {contact_availability}")
        print(f"Contact Info: {contact_info}")
        
    
    
    
parse_peoples()