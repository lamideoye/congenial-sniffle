from pymongo import MongoClient
from django.conf import settings

# Establish MongoDB connection
client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
db = client[settings.DATABASES['default']['NAME']]

# Example model for Users collection
class User:
    collection = db['users']

    @staticmethod
    def create_user(email, name, password):
        return User.collection.insert_one({
            'email': email,
            'name': name,
            'password': password
        })

    @staticmethod
    def get_all_users():
        return list(User.collection.find())

# Example model for Teams collection
class Team:
    collection = db['teams']

    @staticmethod
    def create_team(name, members):
        return Team.collection.insert_one({
            'name': name,
            'members': members
        })

    @staticmethod
    def get_all_teams():
        return list(Team.collection.find())

# Example model for Activities collection
class Activity:
    collection = db['activities']

    @staticmethod
    def create_activity(user_id, type, duration, date):
        return Activity.collection.insert_one({
            'user_id': user_id,
            'type': type,
            'duration': duration,
            'date': date
        })

    @staticmethod
    def get_all_activities():
        return list(Activity.collection.find())

# Example model for Leaderboard collection
class Leaderboard:
    collection = db['leaderboard']

    @staticmethod
    def create_leaderboard(team_id, points):
        return Leaderboard.collection.insert_one({
            'team_id': team_id,
            'points': points
        })

    @staticmethod
    def get_all_leaderboards():
        return list(Leaderboard.collection.find())

# Example model for Workouts collection
class Workout:
    collection = db['workouts']

    @staticmethod
    def create_workout(name, description):
        return Workout.collection.insert_one({
            'name': name,
            'description': description
        })

    @staticmethod
    def get_all_workouts():
        return list(Workout.collection.find())
