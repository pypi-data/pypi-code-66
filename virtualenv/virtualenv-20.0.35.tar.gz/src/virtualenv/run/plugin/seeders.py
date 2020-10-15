from __future__ import absolute_import, unicode_literals

from .base import ComponentBuilder


class SeederSelector(ComponentBuilder):
    def __init__(self, interpreter, parser):
        possible = self.options("virtualenv.seed")
        super(SeederSelector, self).__init__(interpreter, parser, "seeder", possible)

    def add_selector_arg_parse(self, name, choices):
        self.parser.add_argument(
            "--{}".format(name),
            choices=choices,
            default=self._get_default(),
            required=False,
            help="seed packages install method",
        )
        self.parser.add_argument(
            "--no-seed",
            "--without-pip",
            help="do not install seed packages",
            action="store_true",
            dest="no_seed",
        )

    @staticmethod
    def _get_default():
        return "app-data"

    def handle_selected_arg_parse(self, options):
        return super(SeederSelector, self).handle_selected_arg_parse(options)

    def create(self, options):
        return self._impl_class(options)
