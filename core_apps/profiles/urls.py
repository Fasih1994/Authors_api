from django.urls import path

from .views import (
    FollowAPIView,
    FollowerListView,
    FollowingListView,
    ProfileDetailAPIView,
    ProfileListAPIView,
    UnFollowAPIView,
    UpdateProfileAPIView,
)

urlpatterns = [
    path("all/", ProfileListAPIView.as_view(), name="all-profiles"),
    path("me/", ProfileDetailAPIView.as_view(), name="my-profile"),
    path("me/update/", UpdateProfileAPIView.as_view(), name="update-profile"),
    path("me/following/", FollowingListView.as_view(), name="following"),
    path("me/followers/", FollowerListView.as_view(), name="followers"),
    path("<uuid:user_id>/follow", FollowAPIView.as_view(), name="follow"),
    path("<uuid:user_id>/unfollow", UnFollowAPIView.as_view(), name="unfollow"),
]
