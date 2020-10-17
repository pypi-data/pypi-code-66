"""Test cases for LayerModel classes."""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
from drf_chart_of_account.models import (LayerOneModel, LayerTwoModel, LayerThreeModel,
                                         LayerFourModel, LayerFiveModel)


class LayerModelClassesTestCases(TestCase):
    """Testing various methods of the Layer model class methods."""

    def setUp(self):
        """Construct the setup for the test cases."""
        test_user = get_user_model().objects.create(username='test_user_one', email='test_user_one@example.com', password='superacces123one')
        layer_one_obj_one = LayerOneModel(name='Layer one obj one', created_by=test_user)
        layer_one_obj_one.save()
        layer_one_obj_two = LayerOneModel(name='Layer one obj two', created_by=test_user)
        layer_one_obj_two.save()
        layer_one_obj_three = LayerOneModel(name='Layer one obj three', created_by=test_user)
        layer_one_obj_three.save()
        layer_two_object_one = LayerTwoModel(name='Layer two obj one', parent_layer=layer_one_obj_one, created_by=test_user)
        layer_two_object_one.save()
        layer_two_object_two = LayerTwoModel(name='Layer two obj two', parent_layer=layer_one_obj_two, created_by=test_user)
        layer_two_object_two.save()
        layer_two_object_three = LayerTwoModel(name='Layer two obj three', parent_layer=layer_one_obj_two, created_by=test_user)
        layer_two_object_three.save()
        layer_three_object_one = LayerThreeModel(name='Layer three obj one', parent_layer=layer_two_object_one, created_by=test_user)
        layer_three_object_one.save()
        layer_three_object_two = LayerThreeModel(name='Layer three obj two', parent_layer=layer_two_object_two, created_by=test_user)
        layer_three_object_two.save()
        layer_three_object_three = LayerThreeModel(name='Layer three obj three', parent_layer=layer_two_object_two, created_by=test_user)
        layer_three_object_three.save()
        layer_four_object_one = LayerFourModel(name='Layer four obj one', parent_layer=layer_three_object_one, created_by=test_user)
        layer_four_object_one.save()
        layer_four_object_two = LayerFourModel(name='Layer four obj two', parent_layer=layer_three_object_two, created_by=test_user)
        layer_four_object_two.save()
        layer_four_object_three = LayerFourModel(name='Layer four obj three', parent_layer=layer_three_object_two, created_by=test_user)
        layer_four_object_three.save()
        layer_five_object_one = LayerFiveModel(name='Layer five obj one', parent_layer=layer_four_object_one, created_by=test_user)
        layer_five_object_one.save()
        layer_five_object_two = LayerFiveModel(name='Layer five obj two', parent_layer=layer_four_object_two, created_by=test_user)
        layer_five_object_two.save()
        layer_five_object_three = LayerFiveModel(name='Layer five obj three', parent_layer=layer_four_object_two, created_by=test_user)
        layer_five_object_three.save()

    def test_layer_one_model_data(self):
        """Test LayerOneModel data."""
        layer_objects = LayerOneModel.objects.all()
        self.assertEqual(layer_objects[0].name, 'Layer one obj one')
        self.assertEqual(layer_objects[0].ref_no, '1.0.0.0.0')
        self.assertEqual(layer_objects[0].created_by.id, 1)
        self.assertEqual(layer_objects[1].name, 'Layer one obj three')
        self.assertEqual(layer_objects[1].ref_no, '3.0.0.0.0')
        self.assertEqual(layer_objects[1].created_by.id, 1)
        self.assertEqual(layer_objects[2].name, 'Layer one obj two')
        self.assertEqual(layer_objects[2].ref_no, '2.0.0.0.0')
        self.assertEqual(layer_objects[2].created_by.id, 1)
        self.assertRaisesMessage(PermissionDenied, 'The selected layer has child object', layer_objects[0].delete)
        self.assertEqual(layer_objects[1].delete()[0], 1)

    def test_layer_two_model_data(self):
        """Test LayerTwoModel data."""
        layer_objects = LayerTwoModel.objects.all()
        self.assertEqual(layer_objects[0].name, 'Layer two obj one')
        self.assertEqual(layer_objects[0].ref_no, '1.1.0.0.0')
        self.assertEqual(layer_objects[0].created_by.id, 1)
        self.assertEqual(layer_objects[1].name, 'Layer two obj three')
        self.assertEqual(layer_objects[1].ref_no, '2.3.0.0.0')
        self.assertEqual(layer_objects[1].created_by.id, 1)
        self.assertEqual(layer_objects[2].name, 'Layer two obj two')
        self.assertEqual(layer_objects[2].ref_no, '2.2.0.0.0')
        self.assertEqual(layer_objects[2].created_by.id, 1)
        self.assertRaisesMessage(PermissionDenied, 'The selected layer has child object', layer_objects[0].delete)
        self.assertEqual(layer_objects[1].delete()[0], 1)

    def test_layer_three_model_data(self):
        """Test LayerThreeModel data."""
        layer_objects = LayerThreeModel.objects.all()
        self.assertEqual(layer_objects[0].name, 'Layer three obj one')
        self.assertEqual(layer_objects[0].ref_no, '1.1.1.0.0')
        self.assertEqual(layer_objects[0].created_by.id, 1)
        self.assertEqual(layer_objects[1].name, 'Layer three obj three')
        self.assertEqual(layer_objects[1].ref_no, '2.2.3.0.0')
        self.assertEqual(layer_objects[1].created_by.id, 1)
        self.assertEqual(layer_objects[2].name, 'Layer three obj two')
        self.assertEqual(layer_objects[2].ref_no, '2.2.2.0.0')
        self.assertEqual(layer_objects[2].created_by.id, 1)
        self.assertRaisesMessage(PermissionDenied, 'The selected layer has child object', layer_objects[0].delete)
        self.assertEqual(layer_objects[1].delete()[0], 1)

    def test_layer_four_model_data(self):
        """Test LayerFourModel data."""
        layer_objects = LayerFourModel.objects.all()
        self.assertEqual(layer_objects[0].name, 'Layer four obj one')
        self.assertEqual(layer_objects[0].ref_no, '1.1.1.1.0')
        self.assertEqual(layer_objects[0].created_by.id, 1)
        self.assertEqual(layer_objects[1].name, 'Layer four obj three')
        self.assertEqual(layer_objects[1].ref_no, '2.2.2.3.0')
        self.assertEqual(layer_objects[1].created_by.id, 1)
        self.assertEqual(layer_objects[2].name, 'Layer four obj two')
        self.assertEqual(layer_objects[2].ref_no, '2.2.2.2.0')
        self.assertEqual(layer_objects[2].created_by.id, 1)
        self.assertRaisesMessage(PermissionDenied, 'The selected layer has child object', layer_objects[0].delete)
        self.assertEqual(layer_objects[1].delete()[0], 1)

    def test_layer_five_model_data(self):
        """Test LayerFiveModel data."""
        layer_objects = LayerFiveModel.objects.all()
        self.assertEqual(layer_objects[0].name, 'Layer five obj one')
        self.assertEqual(layer_objects[0].ref_no, '1.1.1.1.1')
        self.assertEqual(layer_objects[0].created_by.id, 1)
        self.assertEqual(layer_objects[1].name, 'Layer five obj three')
        self.assertEqual(layer_objects[1].ref_no, '2.2.2.2.3')
        self.assertEqual(layer_objects[1].created_by.id, 1)
        self.assertEqual(layer_objects[2].name, 'Layer five obj two')
        self.assertEqual(layer_objects[2].ref_no, '2.2.2.2.2')
        self.assertEqual(layer_objects[2].created_by.id, 1)
        self.assertEqual(layer_objects[0].delete()[0], 1)
