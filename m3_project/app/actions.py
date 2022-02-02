from django.contrib.auth.models import User
from objectpack.ui import ModelEditWindow, BaseListWindow
from objectpack.ui import ObjectTab
from objectpack.actions import ObjectPack
from django.contrib.auth.models import User, Group, Permission, ContentType
from m3.actions import Action
from m3.actions import ActionPack
from m3.actions.results import OperationResult
from .models import Person


class PersonPack(ObjectPack):

    model = Person
    add_window = edit_window = ModelEditWindow.fabricate(model=model)

    add_to_menu = True

    columns = [
        {
            'data_index': 'name',
            'header': u'Имя',
            'width': 2,
        },
        {
            'data_index': 'surname',
            'header': u'Фамилия',
            'width': 2,
        },
        {
            'data_index': 'gender',
            'header': u'Пол',
            'width': 1,
        },
        {
            'data_index': 'birthday',
            'header': u'Дата рождения',
            'width': 1,
        }
    ]


class GroupPack(ObjectPack):

    model = Group
    print(model.__name__)
    add_window = edit_window = ModelEditWindow.fabricate(model=model)

    add_to_menu = True


class UserPack(ObjectPack):

    model = User
    add_window = edit_window = ModelEditWindow.fabricate(model=model)

    add_to_menu = True

    columns = [
        {
            'data_index': 'username',
            'header': u'username',
            'width': 2,
        },
        {
            'data_index': 'email',
            'header': u'email',
            'width': 2,
        }
    ]

class PermissionPack(ObjectPack):

    model = Permission
    add_window = edit_window = ModelEditWindow.fabricate(model=model)

    add_to_menu = True


class ContentTypePack(ObjectPack):

    model = ContentType
    add_window = edit_window = ModelEditWindow.fabricate(model=model)

    add_to_menu = True

