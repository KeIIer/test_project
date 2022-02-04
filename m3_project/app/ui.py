from objectpack.ui import BaseEditWindow, make_combo_box
from m3_ext.ui import all_components as ext

from .models import Person
from django.contrib.auth.models import User, Group, Permission, ContentType
# from django.contrib.contenttypes.models import ContentType


class UserEditWindow(BaseEditWindow):

    def _init_components(self):
        """
        Здесь следует инициализировать компоненты окна и складывать их в
        :attr:`self`.
        """
        super(UserEditWindow, self)._init_components()

        self.field__username = ext.ExtStringField(
            label=u'username',
            name='username',
            allow_blank=False,
            anchor='100%')

        self.field__password = ext.ExtStringField(
            label=u'password',
            name='password',
            allow_blank=False,
            anchor='100%')

        self.field__email = ext.ExtStringField(
            label=u'email',
            name='email',
            anchor='100%')

        self.field__first_name = ext.ExtStringField(
            label=u'first name',
            name='first_name',
            anchor='100%')

        self.field__last_name = ext.ExtStringField(
            label=u'last_name',
            name='first_name',
            anchor='100%')

        self.field__last_login = ext.ExtDateField(
            label=u'last login',
            name='last_login',
            anchor='100%',
            format='d.m.Y')

        self.field__date_joined = ext.ExtDateField(
            label=u'date joined',
            name='date_joined',
            anchor='100%',
            format='d.m.Y')

        self.field__is_superuser = ext.ExtCheckBox(
            label=u'superuser status',
            name='is_superuser',
            anchor='100%')

        self.field__is_staff = ext.ExtCheckBox(
            label=u'staff status',
            name='is_staff',
            anchor='100%')

        self.field__is_active = ext.ExtCheckBox(
            label=u'active status',
            name='is_active',
            anchor='100%')

    def _do_layout(self):
        """
        Здесь размещаем компоненты в окне
        """
        super(UserEditWindow, self)._do_layout()
        self.form.items.extend((
            self.field__username,
            self.field__password,
            self.field__email,
            self.field__first_name,
            self.field__last_name,
            self.field__last_login,
            self.field__date_joined,
            self.field__is_superuser,
            self.field__is_staff,
            self.field__is_active,
        ))

    def set_params(self, params):
        """
        Установка параметров окна

        :params: Словарь с параметрами, передается из пака
        """
        super(UserEditWindow, self).set_params(params)
        self.height = 'auto'


class PersonAddWindow(BaseEditWindow):

    def _init_components(self):
        """
        Здесь следует инициализировать компоненты окна и складывать их в
        :attr:`self`.
        """
        super(PersonAddWindow, self)._init_components()

        self.field__name = ext.ExtStringField(
            label=u'Имя',
            name='name',
            allow_blank=False,
            anchor='100%')

        self.field__surname = ext.ExtStringField(
            label=u'Фамилия',
            name='surname',
            allow_blank=False,
            anchor='100%')

        self.field__gender = make_combo_box(
            label=u'Пол',
            name='gender',
            allow_blank=False,
            anchor='100%',
            data=Person.GENDERS)

        self.field__birthday = ext.ExtDateField(
            label=u'Дата рождения',
            name='birthday',
            anchor='100%',
            format='d.m.Y')

    def _do_layout(self):
        """
        Здесь размещаем компоненты в окне
        """
        super(PersonAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__name,
            self.field__surname,
            self.field__gender,
            self.field__birthday,
        ))

    def set_params(self, params):
        """
        Установка параметров окна

        :params: Словарь с параметрами, передается из пака
        """
        super(PersonAddWindow, self).set_params(params)
        self.height = 'auto'


class PermissionEditWindow(BaseEditWindow):

    def _init_components(self):
        """
        Здесь следует инициализировать компоненты окна и складывать их в
        :attr:`self`.
        """
        super(PermissionEditWindow, self)._init_components()

        self.field__name = ext.ExtStringField(
            label=u'name',
            name='name',
            allow_blank=False,
            anchor='100%')

        content_types = ContentType.objects.values_list('id', 'model')
        final_choices = ()

        for item in content_types:
            final_choices += (item,)

        self.field__content_type = make_combo_box(
            label=u'python model class name',
            name='content_type_id',
            allow_blank=False,
            anchor='100%',
            data=final_choices)

        self.field__codename = ext.ExtStringField(
            label=u'codename',
            name='codename',
            allow_blank=False,
            anchor='100%')

    def _do_layout(self):
        """
        Здесь размещаем компоненты в окне
        """
        super(PermissionEditWindow, self)._do_layout()
        self.form.items.extend((
            self.field__name,
            self.field__content_type,
            self.field__codename,
        ))

    def set_params(self, params):
        """
        Установка параметров окна

        :params: Словарь с параметрами, передается из пака
        """
        super(PermissionEditWindow, self).set_params(params)
        self.height = 'auto'
