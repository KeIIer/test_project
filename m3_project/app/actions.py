from django.contrib.auth.models import User
from objectpack.ui import ModelEditWindow, BaseListWindow, BaseEditWindow, BaseSelectWindow, BaseWindow
from objectpack.ui import ObjectTab
from objectpack.actions import ObjectPack
from objectpack.ui import BaseEditWindow, make_combo_box
from m3_ext.ui import all_components as ext
from django.contrib.auth.models import User, Group, Permission, ContentType
from m3.actions import Action
from m3.actions import ActionPack
from m3.actions.results import OperationResult
from . import models
from . import ui


class PersonObjectPack(ObjectPack):
    """
    ObjectPack для модели Person
    """

    model = models.Person
    add_to_desktop = True
    add_to_menu = True

    edit_window = add_window = ModelEditWindow.fabricate(model)

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


class FabricateUserPack(ObjectPack):

    model = User
    add_window = edit_window = ModelEditWindow.fabricate(model)

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

    add_to_desktop = True
    add_to_menu = True


class ContentTypePack(ObjectPack):

    model = ContentType
    add_window = edit_window = ModelEditWindow.fabricate(model=model)

    add_to_desktop = True
    add_to_menu = True


