from django.test import TestCase
from .factories import TestStorageTargetFactory, TestFileStorageModelFactory, TestImageStorageModelFactory


class TestStorageTargetFactoryTestCase(TestCase):
    def test_gcs(self):
        tstf = TestStorageTargetFactory(provider="gcloud")
        self.assertIsNotNone(tstf.pk)

    def test_aws(self):
        tstf = TestStorageTargetFactory(provider="s3boto3")
        self.assertIsNotNone(tstf.pk)

    def test_azure(self):
        tstf = TestStorageTargetFactory(provider="azure")
        self.assertIsNotNone(tstf.pk)


class TestFileStorageModelFactoryTestCase(TestCase):
    def test_gcs(self):
        tstf = TestStorageTargetFactory(provider="gcloud")
        tfsmf = TestFileStorageModelFactory(storage_target=tstf)
        self.assertIsNotNone(tfsmf.pk)
        self.assertIsNotNone(tfsmf.file.url)

    def test_aws(self):
        tstf = TestStorageTargetFactory(provider="s3boto3")
        tfsmf = TestFileStorageModelFactory(storage_target=tstf)
        self.assertIsNotNone(tfsmf.pk)
        self.assertIsNotNone(tfsmf.file.url)

    def test_azure(self):
        tstf = TestStorageTargetFactory(provider="azure")
        tfsmf = TestFileStorageModelFactory(storage_target=tstf)
        self.assertIsNotNone(tfsmf.pk)
        self.assertIsNotNone(tfsmf.file.url)

class TestImageStorageModelFactoryTestCase(TestCase):
    def test_gcs(self):
        tstf = TestStorageTargetFactory(provider="gcloud")
        tismf = TestImageStorageModelFactory(storage_target=tstf)
        self.assertIsNotNone(tismf.pk)
        self.assertIsNotNone(tismf.image.url)

    def test_aws(self):
        tstf = TestStorageTargetFactory(provider="s3boto3")
        tismf = TestImageStorageModelFactory(storage_target=tstf)
        self.assertIsNotNone(tismf.pk)
        self.assertIsNotNone(tismf.image.url)

    def test_azure(self):
        tstf = TestStorageTargetFactory(provider="azure")
        tismf = TestImageStorageModelFactory(storage_target=tstf)
        self.assertIsNotNone(tismf.pk)
        self.assertIsNotNone(tismf.image.url)
