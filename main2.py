import json
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()

def nextButton():
    try:
        next_buttonses = driver.find_element(By.CSS_SELECTOR, '.m-pagination.m-pagination--ds')
        if next_buttonses:
            next_buttons = next_buttonses.find_elements(By.CSS_SELECTOR, 'button')
            next_button = next_buttons[-1]
            next_button.click()  
            return True
        else:
            return False  
    except NoSuchElementException:
        return False  

driver.get('https://www.sydney.edu.au/courses/search.html?search-type=course&page=1&years=2025&sort=metatitle')

time.sleep(3)

page_count = 1
max_pages = 2
print(f"Collecting data from page {page_count}")
courses_data = []

while page_count <= max_pages:  

    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'section.m-content.m-course-card'))
    )

    courses = driver.find_elements(By.CSS_SELECTOR, 'section.m-content.m-course-card')
    if courses:
        for course in courses:
            link = course.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
            
            baseUrl = link
            jsonurl1 = baseUrl.replace('.html', '.explorer.json')
            jsonurl3 = baseUrl.replace('.html', '.coredata.json')

            headers = {
                'Host': 'www.sydney.edu.au',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
                'Referer': baseUrl
            }
            data_dict = {'Url': baseUrl}

            try:
                # Fetch JSON 1 (explorer.json)
                response1 = requests.get(jsonurl1)
                response1.raise_for_status() 
                data1 = response1.json()
                
                data_dict['campuses'] = data1.get('content', {}).get('course-details-panel', {}).get('location', '')    
                data_dict['intakeSemesters'] = data1.get('content', {}).get('course-how-to-apply', {}).get('domCommencingSemesterText', '')
                data_dict['partTimeAvailable'] = data1.get('content', {}).get('course-details-panel', {}).get('partTimeDuration', '')
                data_dict['studyMode'] = data1.get('content', {}).get('course-details-panel', {}).get('studyMode', '')
                data_dict['careerPaths'] = data1.get('content', {}).get('nd-career-paths', {}).get('description', '')
                description = data1.get('content', {}).get('nd-about-this-course', {}).get('description', '')
                subdescription = data1.get('content', {}).get('nd-about-this-course', {}).get('subDescription', '')
                overview_description = f"{description} {subdescription}".strip()
                data_dict['descriptionOverview'] = overview_description
                data_dict['descriptionStructure'] = data1.get('content', {}).get('nd-what-youll-learn', {}).get('description', '')
                data_dict['fullTimeDuration'] = data1.get('content', {}).get('course-details-panel', {}).get('fullTimeDuration', '')

            except requests.RequestException as e:
                print(f"Error fetching JSON 1 for {baseUrl}: {e}")
                continue  

            try:
                # Fetch JSON 3 (.coredata.json)
                response3 = requests.get(jsonurl3)
                response3.raise_for_status()
                data3 = response3.json()

                data_dict['courseName'] = data3.get('attributes', {}).get('title', '')
                data_dict['qualificationLevel'] = data3.get('attributes', {}).get('qualification', '')
                data_dict['courseCodeUni'] = data3.get('attributes', {}).get('programCode', '')
                data_dict['courseCodeUac'] = data3.get('attributes', {}).get('uacCode', '')
                data_dict['duration'] = data3.get('attributes', {}).get('lengthInYear', '')
                data_dict['active'] = data3.get('attributes', {}).get('active', '')
                data_dict['published'] = data3.get('attributes', {}).get('published', '')
                data_dict['creditPoints'] = data3.get('attributes', {}).get('creditPoints', '')
                data_dict['intakeYears'] = data3.get('attributes', {}).get('offeredYears', '')

                # Handle latest fees and English requirements
                fees_areas_by_year = data3.get('attributes', {}).get('feeSummary', {}).get('feesByYear', [])
                if fees_areas_by_year:
                    latest_fees = max(fees_areas_by_year, key=lambda x: x['year']).get('fees', '')
                    data_dict['latestFees'] = latest_fees

                english_requirements_by_year = data3.get('attributes', {}).get('entryRequirements', {}).get('entryRequirementsByYear', [])
                if english_requirements_by_year:
                    latest_english_requirements = max(english_requirements_by_year, key=lambda x: x['year']).get('entryRequirements', '')
                    data_dict['latestEnglishRequirements'] = latest_english_requirements

                # Handle ATAR scores latest
                int_score_by_year = data3.get('attributes', {}).get('entryRequirements', {}).get('entryCode', [])
                if int_score_by_year:
                    latest_year_int_score = max(int_score_by_year, key=lambda x: x['year'])
                    data_dict['atarInternational'] = latest_year_int_score['qualifications'][1].get('intScore', '')
                    data_dict['atarDomestic'] = latest_year_int_score['qualifications'][1].get('domScore', '')

                    # For 2025
                    year_2025_data_int_score = next((item for item in int_score_by_year if item['year'] == 2025), None)
                    if year_2025_data_int_score:
                        data_dict['atarInternational_2025'] = year_2025_data_int_score['qualifications'][1].get('intScore', '')
                        data_dict['atarDomestic_2025'] = year_2025_data_int_score['qualifications'][1].get('domScore', '')

            except requests.RequestException as e:
                print(f"Error fetching JSON 3 for {baseUrl}: {e}")
                continue  

            courses_data.append(data_dict)

    if not nextButton():
        break
    page_count += 1
    print(f"Collecting data from page {page_count}")
    time.sleep(3) 

with open('all_courses_data.json', 'w') as json_file:
    json.dump(courses_data, json_file, indent=4)

print("Data has been saved to all_courses_data.json")
driver.quit()
