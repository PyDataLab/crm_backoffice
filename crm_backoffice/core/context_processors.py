def user_role(request):
    if request.user.is_authenticated:
        return {'user_role': getattr(request.user, 'role', None)}
    return {}
