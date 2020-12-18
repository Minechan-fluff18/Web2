from django.conf import settings
from json import loads, dumps
from django.http import HttpResponse
import redis
from users.models import User
from shop_items.models import ShoppingItem
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


def like(request):
    _redis = redis.StrictRedis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=0
    )
    if _redis.get("login") is None:
        return HttpResponse("You are not logged in. Log in to perform such actions.", status=401)
    body = loads(request.body)
    item = get_object_or_404(ShoppingItem, id=body['id'])
    user = get_object_or_404(User, login=_redis.get("login").decode())
    likes = user.likes
    if likes == None:
        likes = []
    if item.id in likes:
        idx = likes.index(item.id)
        new_likes = likes[:idx]
        new_likes.extend(likes[idx+1:])
        user.likes = new_likes
        user.save()
        item.likes = item.likes - 1
        item.save()
        return HttpResponse("Ви забрали лайк з товару.")
    likes.append(item.id)
    user.likes = likes
    user.save()
    item.likes = item.likes + 1
    item.save()
    (item.likes)
    return HttpResponse(f"Ви успішно лайкнули товар '{item.name}'! Тепер на ньому {item.likes} лайк(ів).")
