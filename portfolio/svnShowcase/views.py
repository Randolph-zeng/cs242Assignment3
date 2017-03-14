from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from lxml import etree

# Create your views here.

@csrf_exempt
def getPortfolio(request):

    # contains several key-value pairs,key is the name of project
    # value is a dictionary containing 'date','version','title' three keys
    projects_info = {}
    # contains several key-value pairs,key is the name of project
    # value is a list containing dictionaries for every file in this project
    # the keys are
    files_info = {}
    with open('../svn_list.xml') as file:
        root = etree.XML(file.read())

    #find all project names
    for entry in root.iter('entry'):
        key = entry.find('name')
        if key != None and '/' not in key.text:
            projects_info[key.text] = {}
            projects_info[key.text]['title'] = key.text
            projects_info[key.text]['version'] = entry.find('commit').get('revision')
            projects_info[key.text]['date'] = entry.find('commit').find('date').text
    for prj_name in projects_info:
        files_info[prj_name] = {}

    #find all files
    for entry in root.iter('entry'):
        if entry.get('kind') == 'file':
            element = {}
            key = entry.find('name').text.split('/')[0]
            element['name'] = entry.find('name').text
            element['size'] = entry.find('size').text
            element['author'] = entry.find('commit').find('author').text
            element['date'] = entry.find('commit').find('date').text
            files_info[key][element['name']] = element

    return JsonResponse(files_info,status = 202)
