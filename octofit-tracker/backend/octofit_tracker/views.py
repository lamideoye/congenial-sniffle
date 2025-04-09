from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import api_view
from .models import User, Team, Activity, Leaderboard, Workout

@api_view(['GET'])
def api_root(request, format=None):
    base_url = 'https://urban-space-spork-6rw45ppg7w7cr47g-8000.app.github.dev/'
    return Response({
        'users': base_url + 'api/users/',
        'teams': base_url + 'api/teams/',
        'activities': base_url + 'api/activities/',
        'leaderboard': base_url + 'api/leaderboard/',
        'workouts': base_url + 'api/workouts/'
    })

class UserViewSet(ViewSet):
    def list(self, request):
        users = User.get_all_users()
        return Response(users)

class TeamViewSet(ViewSet):
    def list(self, request):
        teams = Team.get_all_teams()
        return Response(teams)

class ActivityViewSet(ViewSet):
    def list(self, request):
        activities = Activity.get_all_activities()
        return Response(activities)

class LeaderboardViewSet(ViewSet):
    def list(self, request):
        leaderboards = Leaderboard.get_all_leaderboards()
        return Response(leaderboards)

class WorkoutViewSet(ViewSet):
    def list(self, request):
        workouts = Workout.get_all_workouts()
        return Response(workouts)
