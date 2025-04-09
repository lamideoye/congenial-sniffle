from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout

# Removed admin.site.register calls as pymongo models cannot be registered with Django admin.
