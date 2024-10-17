# University Course Web Scraper

This project is a web scraper designed to extract course details from https://www.sydney.edu.au page. The scraper collects all courses and save in a JSON file.

## Features

-  baseUrl










- campuses
- intakeSemesters
- partTimeAvailable
- applicationProcess
- requiredQualifications
- prerequisites
- studyMode
- careerPaths
- descriptionOverview
- descriptionStructure
- fullTimeDuration
- englishLanguageRequirements

## Requirements

To run this project, ensure you have the following installed on your machine:

- Python 3.x
- Selenium

To install Selenium, run:

```
pip install selenium
```
## Installation

Clone the repository:
```
git clone https://github.com/sharifulislam141/Web_Scraper_for_University_Scholarships3
cd Web_Scraper_for_University_Scholarships3
```


## Usage
Run main.py file 
```
python3 main.py

```


## Output

The final results are saved in scholarship_content.json with the following structure:
```
{
    "url": "https://www.sydney.edu.au/courses/courses/uc/bachelor-of-advanced-computing-and-bachelor-of-science.html",
    "campuses": "Camperdown/Darlington campus",
    "intakeSemesters": "<p>Semester 1 (February) and Semester 2 (August)</p>\r\n",
    "partTimeAvailable": "Part time study available for eligible applicants (excluding international student visa holders)",
    "applicationProcess": "<p>All domestic students need to apply through the Universities Admissions Centre (UAC).</p>\r\n",
    "requiredQualifications": "<h4>Secondary or tertiary qualification</h4>\r\n<p>A secondary education qualification such as the NSW Higher School Certificate (including national and international equivalents), OR approved higher education study, including approved preparation courses.</p>\r\n<p><a href=\"https://www.sydney.edu.au/study/how-to-apply/undergraduate/recognised-qualifications.html\">See recognised qualifications</a></p>\r\n",
    "prerequisites": "<h4>Mathematics prerequisite</h4>\r\n<p>This course has a Mathematics prerequisite. <a href=\"/content/corporate/study/applying/how-to-apply/undergraduate/mathematics-prerequisite.html\">Find out if this applies to you</a>.&nbsp;</p>\r\n",
    "studyMode": "On-campus day",
    "careerPaths": "<p>Graduates of this course can be found in a range of careers and roles such as:</p>\r\n<ul>\r\n<li>Computer programmer</li>\r\n<li>Consulting</li>\r\n<li>Geophysicist</li>\r\n<li>Information services management</li>\r\n<li>Mathematician</li>\r\n<li>Microbiologist</li>\r\n<li>Psychologist</li>\r\n<li>Science historian</li>\r\n<li>Software engineer</li>\r\n<li>Forensics</li>\r\n<li>Medical laboratories</li>\r\n<li>Business analysis</li>\r\n<li>Museums</li>\r\n<li>Biotechnology</li>\r\n</ul>\r\n",
    "descriptionOverview": "<p>The combined Bachelor of Advanced Computing and Bachelor of Science program will develop your technical skills in computing while cultivating your expertise in scientific enquiry. Underpinned by critical analytical and leadership skills, you will be positioned to transform our world for the better.\u00a0</p>\r\n <p>This combined degree is ideal for students looking to launch a career as leaders of innovation by combining their computing skills and scientific knowledge.\u00a0</p>",
    "descriptionStructure": "<p>The Bachelor of Advanced Computing and Bachelor of Science is a combined undergraduate coursework degree that will develop your technical skills in computing while cultivating your expertise in scientific enquiry. Underpinned by critical analytical and leadership skills, this course is accredited by the Australian Computer Society.</p>\r\n<p>You will complete core units that cover the skills needed to work as a computing professional, along with a major from the Advanced Computing disciplinary pool and advanced computing elective units.</p>\r\n<p>Additionally, you will complete Science degree core and a program or major from the Science disciplinary pool. You will also complete units from the Open Learning Environment and elective units as needed to meet the requirements of the course.</p>\r\n<p>There are over 20 faculty and 100 shared pool majors to choose from. The Advanced Computing majors are:<br>\r\n</p>\r\n<ul>\r\n<li><a href=\"https://www.sydney.edu.au/courses/subject-areas/major/computational-data-science.html\">Computational Data Science</a></li>\r\n<li><a href=\"https://www.sydney.edu.au/courses/subject-areas/major/computer-science-engineering.html\">Computer Science</a></li>\r\n<li><a href=\"https://www.sydney.edu.au/courses/subject-areas/major/cybersecurity.html\">Cybersecurity</a></li>\r\n<li><a href=\"https://www.sydney.edu.au/courses/subject-areas/major/software-development-engineering.html\">Software Development</a></li>\r\n</ul>\r\n<p>View detailed course structure for this course:&nbsp;<a href=\"https://cusp.sydney.edu.au/students/view-degree-page/degree_id/771\">Bachelor of Advanced Computing and Bachelor of Science</a><br>\r\n</p>\r\n",
    "fullTimeDuration": "5 years full time for Domestic and International students",
    "englishLanguageRequirements": "<p>You may need to provide evidence of your English proficiency to study with us. Find out which requirements are applicable to you below:</p>\r\n ['{\"title\":\"English is my first language\",\"description\":\"<p>If English is your first language, you may be able to meet the English language requirements if you have;&nbsp;</p>\\\\n<p>\\\\n</p>\\\\n<ol>\\\\n\\\\n<li>citizenship or permanent long-term residency (minimum ten years), AND</li>\\\\n\\\\n<li>completed secondary or higher education (tertiary) studies recognised by the University in an approved English-speaking country below:<ul>\\\\n\\\\n<li>American Samoa&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</li>\\\\n\\\\n<li>Australia</li>\\\\n\\\\n<li>Bahamas</li>\\\\n<li>Barbados</li>\\\\n\\\\n<li>Belize</li>\\\\n\\\\n<li>Botswana</li>\\\\n\\\\n<li>Canada (excluding Quebec)</li>\\\\n\\\\n<li>Fiji</li>\\\\n\\\\n<li>Gambia</li>\\\\n\\\\n<li>Ghana</li>\\\\n\\\\n<li>Gibraltar</li>\\\\n\\\\n<li>Guyana</li>\\\\n\\\\n<li>Ireland</li>\\\\n\\\\n<li>Jamaica</li>\\\\n\\\\n<li>Kenya</li>\\\\n\\\\n<li>Lesotho</li>\\\\n\\\\n<li>Liberia</li>\\\\n\\\\n<li>New Zealand</li>\\\\n\\\\n<li>Nigeria</li>\\\\n\\\\n<li>Papua New Guinea</li>\\\\n\\\\n<li>Samoa</li>\\\\n\\\\n<li>Singapore</li>\\\\n\\\\n<li>Solomon Islands</li>\\\\n\\\\n<li>South Africa</li>\\\\n\\\\n<li>Tonga</li>\\\\n\\\\n<li>Trinidad and Tobago</li>\\\\n\\\\n<li>United Kingdom (including Northern Ireland)</li>\\\\n\\\\n<li>United States of America</li>\\\\n\\\\n<li>Zambia</li>\\\\n\\\\n<li>Zimbabwe</li>\\\\n\\\\n</ul>\\\\n\\\\n</li>\\\\n\\\\n</ol>\\\\n<p>\\\\n</p>\\\\n\"}', '{\"title\":\"English is NOT my first language\",\"description\":\"<h4>English language skills test</h4>\\\\n<p>If English is not your first language, you may be able to prove English proficiency with an approved English skills test taken within 2 years of commencing the course.</p>\\\\n<p>Required scores:</p>\\\\n<p>[REQUIREMENTS_TABLE]</p>\\\\n<h4>Other methods</h4>\\\\n<p>We may also consider factors such as previous studies in English. Please check the <a href=\\\\\"/content/corporate/study/applying/how-to-apply/international-students/english-language-requirements.html\\\\\">English language requirements page</a> for more information.</p>\\\\n<p>&nbsp;</p>\\\\n\"}']"
}
```
