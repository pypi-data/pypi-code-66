# Generated by Django 2.2.14 on 2020-07-23 08:49

from django.db import migrations, models
import django.db.models.deletion
import parler.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shuup', '0071_fix_shop_product_typo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attributetranslation',
            name='master',
            field=parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='shuup.Attribute'),
        ),
        migrations.AlterField(
            model_name='categorytranslation',
            name='master',
            field=parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='shuup.Category'),
        ),
        migrations.AlterField(
            model_name='contactgrouptranslation',
            name='master',
            field=parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='shuup.ContactGroup'),
        ),
        migrations.AlterField(
            model_name='customertaxgrouptranslation',
            name='master',
            field=parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='shuup.CustomerTaxGroup'),
        ),
        migrations.AlterField(
            model_name='displayunittranslation',
            name='master',
            field=parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='shuup.DisplayUnit'),
        ),
        migrations.AlterField(
            model_name='fixedcostbehaviorcomponenttranslation',
            name='master',
            field=parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='shuup.FixedCostBehaviorComponent'),
        ),
        migrations.AlterField(
            model_name='labeltranslation',
            name='master',
            field=parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='shuup.Label'),
        ),
        migrations.AlterField(
            model_name='orderstatustranslation',
            name='master',
            field=parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='shuup.OrderStatus'),
        ),
        migrations.AlterField(
            model_name='paymentmethodtranslation',
            name='master',
            field=parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='shuup.PaymentMethod'),
        ),
        migrations.AlterField(
            model_name='productattributetranslation',
            name='master',
            field=parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='shuup.ProductAttribute'),
        ),
        migrations.AlterField(
            model_name='productmedia',
            name='public',
            field=models.BooleanField(blank=True, default=True, help_text='Enable this if you want this image be shown on the product page. Enabled by default.', verbose_name='public (shown on product page)'),
        ),
        migrations.AlterField(
            model_name='productmedia',
            name='purchased',
            field=models.BooleanField(blank=True, default=False, help_text='Enable this if you want the product media to be shown for completed purchases.', verbose_name='purchased (shown for finished purchases)'),
        ),
        migrations.AlterField(
            model_name='productmediatranslation',
            name='master',
            field=parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='shuup.ProductMedia'),
        ),
        migrations.AlterField(
            model_name='producttranslation',
            name='master',
            field=parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='shuup.Product'),
        ),
        migrations.AlterField(
            model_name='producttypetranslation',
            name='master',
            field=parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='shuup.ProductType'),
        ),
        migrations.AlterField(
            model_name='productvariationvariabletranslation',
            name='master',
            field=parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='shuup.ProductVariationVariable'),
        ),
        migrations.AlterField(
            model_name='productvariationvariablevaluetranslation',
            name='master',
            field=parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='shuup.ProductVariationVariableValue'),
        ),
        migrations.AlterField(
            model_name='serviceprovidertranslation',
            name='master',
            field=parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='base_translations', to='shuup.ServiceProvider'),
        ),
        migrations.AlterField(
            model_name='shippingmethodtranslation',
            name='master',
            field=parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='shuup.ShippingMethod'),
        ),
        migrations.AlterField(
            model_name='shopproducttranslation',
            name='master',
            field=parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='shuup.ShopProduct'),
        ),
        migrations.AlterField(
            model_name='shoptranslation',
            name='master',
            field=parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='shuup.Shop'),
        ),
        migrations.AlterField(
            model_name='suppliertranslation',
            name='master',
            field=parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='shuup.Supplier'),
        ),
        migrations.AlterField(
            model_name='taxclasstranslation',
            name='master',
            field=parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='shuup.TaxClass'),
        ),
        migrations.AlterField(
            model_name='taxtranslation',
            name='master',
            field=parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='shuup.Tax'),
        ),
        migrations.AlterField(
            model_name='waivingcostbehaviorcomponenttranslation',
            name='master',
            field=parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='shuup.WaivingCostBehaviorComponent'),
        ),
        migrations.AlterField(
            model_name='weightbasedpricerangetranslation',
            name='master',
            field=parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='shuup.WeightBasedPriceRange'),
        ),
    ]
