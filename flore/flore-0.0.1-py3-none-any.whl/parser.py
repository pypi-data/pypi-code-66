import re


REGEX_FOUND_COLON = r"(\w+)\:(\d+)"


class Parser:
    def parse(self, table_name, columns):
        query = ""
        for name, fields in columns.items():
            text = f"{name} {' '.join(fields)}, "
            text = self.transform_required_to_not_null_field(text)
            query += self.tranform_colon_to_bracket_field(text)

        text = f"CREATE TABLE if not exists {table_name} ({query});"
        return text.replace(", )", ")")

    def transform_required_to_not_null_field(self, text):
        """when the field comes required, it be converted to not null"""

        if "required" in text:
            return text.replace("required", "not null")
        return text

    def tranform_colon_to_bracket_field(self, text):
        """when the field comes varchar:120, it be converted to varchar(120)"""

        if re.search(REGEX_FOUND_COLON, text):
            return re.sub(REGEX_FOUND_COLON, "\\1(\\2)", text)
        return text
