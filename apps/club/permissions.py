from rest_framework.permissions import *
from rest_framework import permissions
from club.models import Club,Coach

class IsOwnerOrReadOnly(BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        # print("-------------")
        # print(request.user)
        # print(obj.user)
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.club_administrator == request.user

    # def has_permission(self, request, view):
    #     # return self.user == request.user
    #     print(view)
    #     return True
class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method is 'DELETE' and obj.user_id == None:
            return True
        print("=========")
        return obj.user == request.user

class IsClubAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        print("come in obj")
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method in ('DELETE','PUT',):
            if obj.club:
                print("---")
                print(obj.club)
                club_id = obj.club
                user = request.user
                club = Club.objects.filter(club_administrator=user)
                print(club)
                return club_id in club
            else:
                return False
        else:
            return False

    def has_permission(self, request, view):
        print("come in has")
        # print(request.META)
        if request.method in permissions.SAFE_METHODS:
            print("xxx")
            return True
        elif request.method in ('POST',):
            if 'club' in request.data:
                print("---")
                club_id = request.data['club']
                club = Club.objects.get(club_id=club_id)
                return club.club_administrator == request.user
            else:
                return False
        else:
            print(".....")
            return True

class IsClubAdmin2(BasePermission):
    def has_object_permission(self, request, view, obj):
        print("come in IsClubAdmin2 obj")
        return True
    def has_permission(self, request, view):
        print("come in IsClubAdmin2")
        print(view)
        if request.method in permissions.SAFE_METHODS:
            return True
        # elif request.method in ('PUT','DELETE'):
        #     if ''
        return True

class IsClubCoach(BasePermission):
    def has_object_permission(self, request, view, obj):
        return True
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method in ('POST','PUT'):
            coach_id = request.data["coach"]
            club = Coach.objects.get(coach_id=coach_id).club
            # print(type(club.club_id))
            # print(type(request.data["club"]))
            # print(club.club_id == request.data["club"])
            return int(request.data["club"]) == club.club_id
        else:
            return False

class IsClubPerson(BasePermission):
    def has_object_permission(self, request, view, obj):
        return True
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method in ('POST','PUT'):
            if 'club' in request.data:
                club_id = request.data["club"]
                club_administrator = Club.objects.get(club_id=club_id).club_administrator
                coaches = Coach.objects.filter(club_id=club_id)
                return request.user == club_administrator or request.user in coaches
            else:
                return False
        else:
            return False
