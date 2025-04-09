from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.collection.delete_many({})
        Team.collection.delete_many({})
        Activity.collection.delete_many({})
        Leaderboard.collection.delete_many({})
        Workout.collection.delete_many({})

        # Create users
        users = [
            User.create_user(email='thundergod@mhigh.edu', name='Thor', password='password123'),
            User.create_user(email='ironman@mhigh.edu', name='Tony Stark', password='password123'),
            User.create_user(email='captain@mhigh.edu', name='Steve Rogers', password='password123'),
        ]

        # Create teams
        team = Team.create_team(name='Avengers', members=['thundergod@mhigh.edu', 'ironman@mhigh.edu', 'captain@mhigh.edu'])

        # Create activities
        activities = [
            Activity.create_activity(user_id='thundergod@mhigh.edu', type='Running', duration=30, date='2025-04-08'),
            Activity.create_activity(user_id='ironman@mhigh.edu', type='Cycling', duration=60, date='2025-04-08'),
            Activity.create_activity(user_id='captain@mhigh.edu', type='Swimming', duration=45, date='2025-04-08'),
        ]

        # Create leaderboard entries
        leaderboard = Leaderboard.create_leaderboard(team_id='Avengers', points=100)

        # Create workouts
        workouts = [
            Workout.create_workout(name='Morning Run', description='A 5km run to start the day'),
            Workout.create_workout(name='Cycling Session', description='An hour of cycling'),
            Workout.create_workout(name='Swimming Laps', description='45 minutes of swimming'),
        ]

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
