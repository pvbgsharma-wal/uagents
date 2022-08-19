from django.http import HttpResponse
from django_user_agents.utils import get_user_agent

def index(request):
    user_agent = get_user_agent(request)
    print(user_agent, "useragent")
    return HttpResponse("You're at  the ua check\nUA : " + user_agent.browser.family)