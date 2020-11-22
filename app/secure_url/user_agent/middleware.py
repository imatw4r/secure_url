from user_agent.models import UserAgent


def store_user_agent(get_response):
    def middleware(request):
        response = get_response(request)
        if request.user.is_authenticated:
            # @TODO: Should be also async
            agent, _ = UserAgent.objects.get_or_create(
                user=request.user,
            )

            agent.user_agent = request.META["HTTP_USER_AGENT"]
            agent.save()
        return response

    return middleware
