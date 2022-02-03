from objectpack.ui import ModelEditWindow, TabbedEditWindow, TabbedWindow
from objectpack.actions import ObjectPack
from django.contrib.auth.models import User, Group, Permission, ContentType
from . import models
from . import ui


class PersonObjectPack(ObjectPack):
    """
    ObjectPack для модели Person
    """

    model = models.Person
    add_to_desktop = True
    add_to_menu = True

    # edit_window = add_window = ModelEditWindow.fabricate(model)
    edit_window = add_window = ui.PersonAddWindow

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
    add_window = edit_window = ModelEditWindow.fabricate(model=model)

    add_to_desktop = True
    add_to_menu = True


class UserPack(ObjectPack):

    model = User
    add_window = edit_window = ui.UserEditWindow
    # add_window = edit_window = ModelEditWindow.fabricate(model)

    add_to_desktop = True
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
    add_window = edit_window = ui.PermissionEditWindow
    # add_window = edit_window = ModelEditWindow.fabricate(model=model)

    add_to_desktop = True
    add_to_menu = True


class ContentTypePack(ObjectPack):

    model = ContentType
    add_window = edit_window = ModelEditWindow.fabricate(model=model)

    add_to_desktop = True
    add_to_menu = True


