from django.shortcuts import render
import requests, json
from requests.auth import HTTPBasicAuth
from .forms import CreateProjectForm, EditProjectForm
from datetime import datetime
from django.contrib import messages
from django.shortcuts import render_to_response
from django.http import JsonResponse


class Projects:
    def __int__(self):
        print("Project class started!")

    def edit_project(self, request):
        return render_to_response('project_edit.html')

    def remove_project(self, request, url):
        # do something with the your data
        data = {'remove': 0}
        if url != "":
            # delete the record and return response

            data = {'remove': 1}
            return JsonResponse(data)
        else:
            return JsonResponse(data)
