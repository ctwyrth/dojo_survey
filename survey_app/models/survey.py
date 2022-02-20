from survey_app.config.mysqlconnection import connectToMySQL
from flask import flash

DB = 'dojo_surveys'

class Survey:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.dojo_location = data['dojo_location']
        self.favorite_language = data['favorite_language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO surveys (first_name, last_name, dojo_location, favorite_language, comment) VALUES (%(fname)s, %(lname)s, %(location)s, %(language)s, %(comment)s);"
        return connectToMySQL(DB).query_db(query,data)

    @classmethod
    def show_all(cls):
        query = "SELECT * FROM surveys;"
        surveys_from_db = connectToMySQL(DB).query_db(query)
        all_surveys = []
        for survey in surveys_from_db:
            all_surveys.append(cls(survey))
        return all_surveys

    @classmethod
    def show(cls,data):
        query = "SELECT * FROM surveys WHERE surveys.id = %(id)s;"
        result = connectToMySQL(DB).query_db(query,data)
        survey = cls(result[0])
        return survey

    @classmethod
    def update(cls,data):
        query = "UPDATE surveys SET first_name=%(fname)s, last_name=%(lname)s, dojo_location=%(location)s, favorite_language=%(language)s, comment=%(comment)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query,data)

    @classmethod
    def delete(cls,data):
        query = "DELETE FROM surveys WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query,data)

    @staticmethod
    def validate_survey(survey):
        is_valid = True
        if len(survey['fname']) < 3:
            flash("* First name is a required field and must be more than 3 characters long.")
            is_valid = False
        if len(survey['lname']) < 3:
            flash("* Last name is a required field and must be more than 3 characters long.")
            is_valid = False
        if survey['location'] == 'select':
            flash("* Please choose a Dojo location from the dropdown menu.")
            is_valid = False
        if survey['language'] == 'select':
            flash("* Please select your favorite coding language from the dropdown menu.")
            is_valid = False
        return is_valid
