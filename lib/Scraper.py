from bs4 import BeautifulSoup
import requests
from Course import Course
import ipdb


class Scraper:
    def __init__(self):
        self.courses = []

    def get_page(self):
        doc = BeautifulSoup(
            requests.get(
                "http://learn-co-curriculum.github.io/site-for-scraping/courses"
            ).text,
            "html.parser"
        )

        return doc

        
    def get_courses(self):
        return self.get_page().select(".post")
    
    def make_courses(self):
        for n in self.get_courses():

            title = n.select("h2")[0].text if n.select("h2") else ""
            date = n.select(".date")[0].text if n.select(".date") else ""
            description = n.select("p")[0].text if n.select("p") else ""

            new_course = Course(title, date, description)
            self.courses.append(new_course)

        return self.courses

    def print_courses(self):
        for n in self.make_courses():
            print(n)
