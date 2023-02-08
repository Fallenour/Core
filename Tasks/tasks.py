from celery import shared_task
from django.core.management import call_command # NEW
import json
import requests


@shared_task
def sample_task():
    print("The sample task just ran.")
    A = "testing return value"
    return A

# NEW
@shared_task
def send_email_report():
    call_command("email_report", )

@shared_task
def send_email_report():
    call_command("email_report", )


@shared_task
def testapicalls():
    api_url = 'http://192.168.240.3:3790/programming_languages'
    print(api_url)
    response = requests.get(api_url)
    print(response)
    return response.json()

@shared_task
def testapicalls2():
    api_url_base = 'http://192.168.240.3:3790/'
    api_url = 'programming_languages'.format(api_url_base)
    api_token = 'token:6bde125560088033c618c2app234'
    headers = {'Content-Type': 'application/json',
               'Authorization': 'Bearer {0}'.format(api_token)}

    response = requests.get(api_url, headers=headers)

    if response.status_code >= 500:
        print('[!] [{0}] Server Error'.format(response.status_code))
        return None
    elif response.status_code == 404:
        print('[!] [{0}] URL not found: [{1}]'.format(response.status_code, api_url))
        return None
    elif response.status_code == 401:
        print('[!] [{0}] Authentication Failed'.format(response.status_code))
        return None
    elif response.status_code == 400:
        print('[!] [{0}] Bad Request'.format(response.status_code))
        return None
    elif response.status_code >= 300:
        print('[!] [{0}] Unexpected Redirect'.format(response.status_code))
        return None
    elif response.status_code == 200:
        api_call = json.loads(response.content.decode('utf-8'))
        return response
    else:
        print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(response.status_code, response.content))
    return None


@shared_task
def apicalls():
    api_token = 'token:6bde125560088033c618c2app234'
    api_url_base = ''
#    api_url_base = 'https://localhost:3790/rest_api/v2/'
    headers = {'Content-Type': 'application/json',
               'Authorization': 'Bearer {0}'.format(api_token)}
    # Google API Test URL
#    api_url = 'https://searchconsole.googleapis.com/$discovery/rest?version=v1'.format(api_url_base)
    api_url = 'https://localhost:3790/rest_api/v2/workspaces/1/hosts'.format(api_url_base)

    response = requests.get(api_url, headers=headers)

    if response.status_code >= 500:
        print('[!] [{0}] Server Error'.format(response.status_code))
        return None
    elif response.status_code == 404:
        print('[!] [{0}] URL not found: [{1}]'.format(response.status_code, api_url))
        return None
    elif response.status_code == 401:
        print('[!] [{0}] Authentication Failed'.format(response.status_code))
        return None
    elif response.status_code == 400:
        print('[!] [{0}] Bad Request'.format(response.status_code))
        return None
    elif response.status_code >= 300:
        print('[!] [{0}] Unexpected Redirect'.format(response.status_code))
        return None
    elif response.status_code == 200:
        api_call = json.loads(response.content.decode('utf-8'))
        return response
    else:
        print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(response.status_code, response.content))
    return None

@shared_task
def atomicredteamapicalls():
    api_token = 'token:6bde125560088033c618c2app234'
    api_url_base = ''
#    api_url_base = 'https://localhost:3790/rest_api/v2/'
    headers = {'Content-Type': 'application/json',
               'Authorization': 'Bearer {0}'.format(api_token)}
    # Google API Test URL
#    api_url = 'https://searchconsole.googleapis.com/$discovery/rest?version=v1'.format(api_url_base)
    api_url = 'https://localhost:3790/rest_api/v2/workspaces/1/hosts'.format(api_url_base)
    response = requests.get(api_url, headers=headers)

    if response.status_code >= 500:
        print('[!] [{0}] Server Error'.format(response.status_code))
        return None
    elif response.status_code == 404:
        print('[!] [{0}] URL not found: [{1}]'.format(response.status_code, api_url))
        return None
    elif response.status_code == 401:
        print('[!] [{0}] Authentication Failed'.format(response.status_code))
        return None
    elif response.status_code == 400:
        print('[!] [{0}] Bad Request'.format(response.status_code))
        return None
    elif response.status_code >= 300:
        print('[!] [{0}] Unexpected Redirect'.format(response.status_code))
        return None
    elif response.status_code == 200:
        api_call = json.loads(response.content.decode('utf-8'))
        return api_call
    else:
        print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(response.status_code, response.content))
    return None


@shared_task
def azureapicalls():
    api_token = 'token:6bde125560088033c618c2app234'
    api_url_base = ''
#    api_url_base = ''
    headers = {'Content-Type': 'application/json',
               'Authorization': 'Bearer {0}'.format(api_token)}
    # Google API Test URL
#    api_url = 'https://searchconsole.googleapis.com/$discovery/rest?version=v1'.format(api_url_base)
    api_url = 'https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines?api-version=2020-06-01'.format(api_url_base)
    response = requests.get(api_url, headers=headers)

    if response.status_code >= 500:
        print('[!] [{0}] Server Error'.format(response.status_code))
        return None
    elif response.status_code == 404:
        print('[!] [{0}] URL not found: [{1}]'.format(response.status_code, api_url))
        return None
    elif response.status_code == 401:
        print('[!] [{0}] Authentication Failed'.format(response.status_code))
        return None
    elif response.status_code == 400:
        print('[!] [{0}] Bad Request'.format(response.status_code))
        return None
    elif response.status_code >= 300:
        print('[!] [{0}] Unexpected Redirect'.format(response.status_code))
        return None
    elif response.status_code == 200:
        api_call = json.loads(response.content.decode('utf-8'))
        return api_call
    else:
        print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(response.status_code, response.content))
    return None


@shared_task
def azuremetricsapicalls():
    api_token = 'token:6bde125560088033c618c2app234'
    api_url_base = ''
#    api_url_base = ''
    headers = {'Content-Type': 'application/json',
               'Authorization': 'Bearer {0}'.format(api_token)}
    # Google API Test URL
#    api_url = 'https://searchconsole.googleapis.com/$discovery/rest?version=v1'.format(api_url_base)
    api_url = 'https://management.azure.com/subscriptions/<sub id>/providers/microsoft.Insights/metrics?timespan=2020-09-14T06:30:00.000Z/2020-09-15T06:45:00.000Z&interval=PT15M&metricnames=Percentage CPU&aggregation=average&metricNamespace=microsoft.compute%2Fvirtualmachines&top=10&orderby=average desc&autoadjusttimegrain=true&validatedimensions=false&api-version=2017-12-01-preview&region=westeurope'.format(api_url_base)
    response = requests.get(api_url, headers=headers)

    if response.status_code >= 500:
        print('[!] [{0}] Server Error'.format(response.status_code))
        return None
    elif response.status_code == 404:
        print('[!] [{0}] URL not found: [{1}]'.format(response.status_code, api_url))
        return None
    elif response.status_code == 401:
        print('[!] [{0}] Authentication Failed'.format(response.status_code))
        return None
    elif response.status_code == 400:
        print('[!] [{0}] Bad Request'.format(response.status_code))
        return None
    elif response.status_code >= 300:
        print('[!] [{0}] Unexpected Redirect'.format(response.status_code))
        return None
    elif response.status_code == 200:
        api_call = json.loads(response.content.decode('utf-8'))
        return api_call
    else:
        print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(response.status_code, response.content))
    return None


@shared_task
def azurededicatedhostsapicalls():
    api_token = 'token:6bde125560088033c618c2app234'
    api_url_base = ''
#    api_url_base = ''
    headers = {'Content-Type': 'application/json',
               'Authorization': 'Bearer {0}'.format(api_token)}
    # Google API Test URL
#    api_url = 'https://searchconsole.googleapis.com/$discovery/rest?version=v1'.format(api_url_base)
    api_url = 'https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/hostGroups/{hostGroupName}/hosts/{hostName}?api-version=2020-06-01'.format(api_url_base)
    response = requests.get(api_url, headers=headers)

    if response.status_code >= 500:
        print('[!] [{0}] Server Error'.format(response.status_code))
        return None
    elif response.status_code == 404:
        print('[!] [{0}] URL not found: [{1}]'.format(response.status_code, api_url))
        return None
    elif response.status_code == 401:
        print('[!] [{0}] Authentication Failed'.format(response.status_code))
        return None
    elif response.status_code == 400:
        print('[!] [{0}] Bad Request'.format(response.status_code))
        return None
    elif response.status_code >= 300:
        print('[!] [{0}] Unexpected Redirect'.format(response.status_code))
        return None
    elif response.status_code == 200:
        api_call = json.loads(response.content.decode('utf-8'))
        return api_call
    else:
        print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(response.status_code, response.content))
    return None