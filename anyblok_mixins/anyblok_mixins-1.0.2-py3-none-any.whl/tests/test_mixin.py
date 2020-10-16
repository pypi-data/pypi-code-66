# This file is a part of the AnyBlok project
#
#    Copyright (C) 2014 Jean-Sebastien SUZANNE <jssuzanne@anybox.fr>
#    Copyright (C) 2017 Jean-Sebastien SUZANNE <jssuzanne@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.
import pytest
from anyblok.tests.conftest import init_registry_with_bloks
from anyblok import Declarations
from anyblok.column import Integer, String, Boolean
from anyblok_mixins.mixins.exceptions import (
    ForbidDeleteException, ForbidUpdateException
)
register = Declarations.register
unregister = Declarations.unregister
Mixin = Declarations.Mixin
Model = Declarations.Model


class TestMixin:

    @pytest.fixture(autouse=True)
    def close_registry(self, request, bloks_loaded):

        def close():
            if hasattr(self, 'registry'):
                self.registry.close()

        request.addfinalizer(close)

    def init_registry(self, func):
        self.registry = init_registry_with_bloks(
            ('anyblok-mixins',), func)
        return self.registry

    def test_forbidden_delete(self):

        def add_in_registry():

            @register(Model)
            class Test(Mixin.ForbidDelete):

                id = Integer(primary_key=True)

        registry = self.init_registry(add_in_registry)
        t = registry.Test.insert()
        with pytest.raises(ForbidDeleteException):
            t.delete()

    def test_forbidden_update(self):

        def add_in_registry():

            @register(Model)
            class Test(Mixin.ForbidUpdate):

                id = Integer(primary_key=True)
                name = String()

        registry = self.init_registry(add_in_registry)
        t = registry.Test.insert()
        t.name = 'test'
        with pytest.raises(ForbidUpdateException):
            registry.flush()

    def test_readonly_delete(self):

        def add_in_registry():

            @register(Model)
            class Test(Mixin.ReadOnly):

                id = Integer(primary_key=True)

        registry = self.init_registry(add_in_registry)
        t = registry.Test.insert()
        with pytest.raises(ForbidDeleteException):
            t.delete()

    def test_readonly_update(self):

        def add_in_registry():

            @register(Model)
            class Test(Mixin.ReadOnly):

                id = Integer(primary_key=True)
                name = String()

        registry = self.init_registry(add_in_registry)
        t = registry.Test.insert()
        t.name = 'test'
        with pytest.raises(ForbidUpdateException):
            registry.flush()

    def test_conditional_forbidden_delete(self):

        def add_in_registry():

            @register(Model)
            class Test(Mixin.ConditionalForbidDelete):

                id = Integer(primary_key=True)
                forbid_delete = Boolean(default=False)

                def check_if_forbid_delete_condition_is_true(self):
                    return self.forbid_delete

        registry = self.init_registry(add_in_registry)
        t1 = registry.Test.insert()
        t2 = registry.Test.insert(forbid_delete=True)
        t1.delete()

        with pytest.raises(ForbidDeleteException):
            t2.delete()

    def test_conditional_forbidden_delete_mission_method(self):

        def add_in_registry():

            @register(Model)
            class Test(Mixin.ConditionalForbidDelete):

                id = Integer(primary_key=True)

        registry = self.init_registry(add_in_registry)
        t = registry.Test.insert()
        with pytest.raises(ForbidDeleteException):
            t.delete()

    def test_conditional_forbidden_update_missing_method(self):

        def add_in_registry():

            @register(Model)
            class Test(Mixin.ConditionalForbidUpdate):

                id = Integer(primary_key=True)
                name = String()

        registry = self.init_registry(add_in_registry)
        t = registry.Test.insert()
        t.name = 'test'
        with pytest.raises(ForbidUpdateException):
            registry.flush()

    def test_conditional_forbidden_update(self):

        def add_in_registry():

            @register(Model)
            class Test(Mixin.ConditionalForbidUpdate):

                id = Integer(primary_key=True)
                forbid_update = Boolean(default=False)
                name = String()

                def check_if_forbid_update_condition_is_true(self, **changed):
                    return self.forbid_update

        registry = self.init_registry(add_in_registry)
        t1 = registry.Test.insert()
        t1.name = 'test'
        registry.flush()
        t2 = registry.Test.insert(forbid_update=True)
        t2.name = 'test'
        with pytest.raises(ForbidUpdateException):
            registry.flush()

    def test_boolean_forbidden_delete(self):

        def add_in_registry():

            @register(Model)
            class Test(Mixin.BooleanForbidDelete):

                id = Integer(primary_key=True)

        registry = self.init_registry(add_in_registry)
        t1 = registry.Test.insert()
        t2 = registry.Test.insert(forbid_delete=True)
        t1.delete()

        with pytest.raises(ForbidDeleteException):
            t2.delete()

    def test_boolean_forbidden_update(self):

        def add_in_registry():

            @register(Model)
            class Test(Mixin.BooleanForbidUpdate):

                id = Integer(primary_key=True)
                name = String()

        registry = self.init_registry(add_in_registry)
        t1 = registry.Test.insert()
        t1.name = 'test'
        registry.flush()
        t2 = registry.Test.insert(forbid_update=True)
        t2.name = 'test'
        with pytest.raises(ForbidUpdateException):
            registry.flush()


def add_in_registry_conditional_readonly():

    @register(Model)
    class Test(Mixin.ConditionalReadOnly):

        id = Integer(primary_key=True)
        readonly = Boolean(default=False)
        name = String()

        def check_if_forbid_update_condition_is_true(self,
                                                     **previous_values):
            return previous_values.get('readonly', self.readonly)

        def check_if_forbid_delete_condition_is_true(self):
            return self.readonly


@pytest.fixture(scope="class")
def registry_conditional_readonly(request, bloks_loaded):
    registry = init_registry_with_bloks(
        ('anyblok-mixins',), add_in_registry_conditional_readonly)
    request.addfinalizer(registry.close)
    return registry


class TestConditionalReadonly:

    @pytest.fixture(autouse=True)
    def transact(self, request, registry_conditional_readonly):
        transaction = registry_conditional_readonly.begin_nested()
        request.addfinalizer(transaction.rollback)
        return

    def test_delete(self, registry_conditional_readonly):
        registry = registry_conditional_readonly
        t1 = registry.Test.insert()
        t1.delete()
        t2 = registry.Test.insert(readonly=True)
        with pytest.raises(ForbidDeleteException):
            t2.delete()

    def test_update(self, registry_conditional_readonly):
        registry = registry_conditional_readonly
        t1 = registry.Test.insert()
        t1.name = 'test'
        registry.flush()
        t2 = registry.Test.insert(readonly=True)
        t2.name = 'test'
        with pytest.raises(ForbidUpdateException):
            registry.flush()


def add_in_registry_boolean_readonly():
    @register(Model)
    class Test(Mixin.BooleanReadOnly):

        id = Integer(primary_key=True)
        name = String()


@pytest.fixture(scope="class")
def registry_boolean_readonly(request, bloks_loaded):
    registry = init_registry_with_bloks(
        ('anyblok-mixins',), add_in_registry_boolean_readonly)
    request.addfinalizer(registry.close)
    return registry


class TestBooleanReadonly:

    @pytest.fixture(autouse=True)
    def transact(self, request, registry_boolean_readonly):
        transaction = registry_boolean_readonly.begin_nested()
        request.addfinalizer(transaction.rollback)
        return

    def test_delete(self, registry_boolean_readonly):
        registry = registry_boolean_readonly
        t1 = registry.Test.insert()
        t1.delete()
        t2 = registry.Test.insert(readonly=True)
        with pytest.raises(ForbidDeleteException):
            t2.delete()

    def test_update(self, registry_boolean_readonly):
        registry = registry_boolean_readonly
        t1 = registry.Test.insert()
        t1.name = 'test'
        registry.flush()
        t2 = registry.Test.insert(readonly=True)
        t2.name = 'test'
        with pytest.raises(ForbidUpdateException):
            registry.flush()


def add_in_registry_state_readonly():

    @register(Model)
    class Test(Mixin.StateReadOnly):
        DEFAULT_STATE = 'draft'

        @classmethod
        def get_states(cls):
            return {
                'draft': 'Draft',
                'started': 'Started',
                'done': 'Done',
            }

        def check_if_forbid_update_condition_is_true(self, **changed):
            if 'state' in changed:
                return False

            return self.state == 'done'

        def check_if_forbid_delete_condition_is_true(self):
            return self.state != 'draft'

        id = Integer(primary_key=True)
        name = String()


@pytest.fixture(scope="class")
def registry_state_readonly(request, bloks_loaded):
    registry = init_registry_with_bloks(
        ('anyblok-mixins',), add_in_registry_state_readonly)
    request.addfinalizer(registry.close)
    return registry


class TestStateReadonly:

    @pytest.fixture(autouse=True)
    def transact(self, request, registry_state_readonly):
        transaction = registry_state_readonly.begin_nested()
        request.addfinalizer(transaction.rollback)
        return

    def test_delete_1(self, registry_state_readonly):
        registry = registry_state_readonly
        t = registry.Test.insert()
        t.delete()

    def test_delete_2(self, registry_state_readonly):
        registry = registry_state_readonly
        t = registry.Test.insert(state='started')
        with pytest.raises(ForbidDeleteException):
            t.delete()

    def test_delete_3(self, registry_state_readonly):
        registry = registry_state_readonly
        t = registry.Test.insert(state='done')
        with pytest.raises(ForbidDeleteException):
            t.delete()

    def test_update_1(self, registry_state_readonly):
        registry = registry_state_readonly
        t1 = registry.Test.insert()
        t1.name = 'test'
        registry.flush()

    def test_update_2(self, registry_state_readonly):
        registry = registry_state_readonly
        t = registry.Test.insert(state='done')
        t.name = 'test'
        with pytest.raises(ForbidUpdateException):
            registry.flush()

    def test_update_3(self, registry_state_readonly):
        registry = registry_state_readonly
        t = registry.Test.insert()
        t.name = 'test1'
        t.state = 'started'
        registry.flush()
        t.name = 'test2'
        t.state = 'done'
        registry.flush()
        t.name = 'test3'
        with pytest.raises(ForbidUpdateException):
            registry.flush()
