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
max_pages = 58
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
            jsonurl2 = 'https://www.sydney.edu.au/bin/courses/course-common-content.json'
            
            headers = {
                'Host': 'www.sydney.edu.au',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
                'Referer': baseUrl
            }
            data_dict = {'Url': baseUrl}

            try:
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
                # Fetch JSON 2
                response2 = requests.get(jsonurl2, headers=headers)
                response2.raise_for_status()
                data2 = response2.json()
                
                data_dict['applicationProcess'] = data2.get('how_to_apply', {}).get('uac-message', {}).get('master', {}).get('jcr:content', {}).get('root', {}).get('content_container', {}).get('text', '')
                data_dict['requiredQualifications'] = data2.get('admission_criteria', {}).get('secondary-qualifications', {}).get('master', {}).get('jcr:content', {}).get('root', {}).get('content_container', {}).get('text', '')
                data_dict['prerequisites'] = data2.get('prerequisite', {}).get('master', {}).get('jcr:content', {}).get('root', {}).get('accordion_wide', {}).get('oI9x55bN', {}).get('content_container', {}).get('text', '')
                englishLanguageRequirements1 = data2.get('english-language-requirements', {}).get('standard', {}).get('jcr:content', {}).get('root', {}).get('content_container', {}).get('text', '')
                englishLanguageRequirements2 = data2.get('english-language-requirements', {}).get('standard', {}).get('jcr:content', {}).get('root', {}).get('accordion', {}).get('links', '')
                data_dict['englishLanguageRequirements'] = f"{englishLanguageRequirements1} {englishLanguageRequirements2}"

            except requests.RequestException as e:
                print(f"Error fetching JSON 2 for {baseUrl}: {e}")
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
