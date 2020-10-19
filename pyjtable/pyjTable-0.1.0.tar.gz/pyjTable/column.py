# -*- coding: utf-8 -*-
"""
Created on Mar 2, 2016

@author: Derek Wood
"""
from collections import namedtuple
from enum import Enum
import logging
import textwrap


class Visibility(Enum):
    """
    Visibility options for columns.

    #Note: User can open column selection list by right clicking the table header if columnSelectable option is true (it's true as default).
    """
    fixed = 1  # This column is always visible and can not be hided by the user.
    visible = 2  # This column is visible as default but can be hided by the user.
    hidden = 3  # This column is hidden as default but can be showed by the user.


OptionTuple = namedtuple('OptionTuple', ['Value', 'DisplayText'])


class DataType(Enum):
    text = 1
    password = 2
    date = 3
    radiobutton = 4
    checkbox = 5
    hidden = 6


class Column(object):
    """
    Class defining a table Column
        
    Parameters
    ----------
    sa_column : SQLAlchemy Column to get data from
        Column as defined by the SQLAlchemy model
    
    column_name : str
        name of the columnName property as defined in the DataTables javascript options (default None)
    
    title = None
    
    key : boolean (default = false)
        A boolean value that indicates whether this field is the key (primary key) field of the record.
        Every record must has one and only one key field that is used on update and delete operations.
        If a field is marked as key, create and edit options are set to false as default.
        If a key field is not editable in edit form, a hidden input element is generated for it.
        Thus, key value is post to server. If the key field is editable (with setting edit option to true),
        key's original value (the value before update) is posted to server as jtRecordKey.
    
    create : boolean
        A boolean value that indicates whether this field is shown in the create record form.
        Default value is false for the key field. True for other fields.
    
    list : boolean (default = True)
        A boolean value that indicates whether this field is shown in the table.
    
    edit : boolean (default = False for key, True for others) 
        A boolean value that indicates whether this field is shown in the edit record form.
    
    dataType: string or DataType (default: text)
         Data type for this field. If field is text or number, no need to set type. Other types are:
            password: Show a password textbox for this field on edit/create forms.
            textarea: Shows a textarea for this field on edit/create forms.
            date: A date field (not including time part). A jQueryUI date picker is automatically created for this field on edit/create forms.
                  additional options:
                    displayFormat
            radiobutton: If field is a value from an option list, it can be a combobox (default) or radio button list.
                        If it is a radio button list, set type as radiobutton. You must supply options list for this type.
            checkbox: To show a checkbox while editing this field. 
                If a field is checkbox, it can define additional options:
                checkboxValues, checkboxFormText, checkboxSetOnTextClick
            hidden: A hidden field can be used hidden fields in edit and create forms. It is not shown on the table.
                    You may want to use defaultValue option with hidden types, thus given default value is automatically set to the hidden field on creating form. See master/child demo for sample usage.
    
    dateDisplayFormat: str ( Default = "mm/dd/yy" )
        Format of date. See jQueryUI datepicker formats.
    
    checkboxValues: list of 2 tuples
        Values for checked/unchecked states. Example: { '0' : 'Passive', '1' : 'Active' }. First value is for unchecked state, second value is for checked state.
    
    checkboxFormText: str
        By default, a checkbox's text changes when user changes the state of the checkbox.
        If you want to fix the text, you can set the formText option for this field (string).
    
    checkboxSetOnTextClick: boolean (default = true)
        By default, when the user clicks the checkbox's text, the state of the checkbox changes.
        If you do not want that, you can set setOnTextClick to false.
    
    listClass : str (default = None)
        A string value that can be set as class/classes of a cell of this field (td element) in the table. Thus, you can stylize fields in the table.
    
    displayFunction : str defining a javascript function
        This option is a function that allows you to define a fully custom column for table. jTable directly shows return value of this function on the table
        http://www.jtable.org/ApiReference/FieldOptions#fopt-display
        This sample Test column returns a bold 'test' string for all rows. You can return any text, html code or jQuery object that will be shown on the table. This method is called for each row. You can get record of the row using data.record. So, if your record has Name property, you can use data.record.Name property to get the Name.
        display function can be used for many purposes such as creating calculated columns, opening child tables for a row... etc.
        example value:
        "
        function (data) {
            return $('<a href="/plants/' + data.record.Id + '">' + data.record.Name + '</a>');
        }
        "
    
    width: pct
        Percentage of table width to try and allocate
    
    columnResizable : boolean (default = true)
        A boolean value that indicates whether this column can be resized by user. Table's columnResizable option must be set to true (it's default) to use this option.
    
    sorting : boolean (default = true)
        Indicates that whether this column will be used to sort the table (If table is sortable).
    
    inputFunction : str defining a javascript function
        This option is a function that allows you to define a fully custom input element for create and edit forms. jTable directly shows return value of this function on the form.
        See the samples below:
        "
        function (data) {
            return '<input type="text" name="Name" style="width:200px" value="' + data.value + '" />';
        }
        "
        
        "
        function (data) {
            if (data.record) {
                return '<input type="text" name="Name" style="width:200px" value="' + data.record.Name + '" />';
            } else {
                return '<input type="text" name="Name" style="width:200px" value="enter your name here" />';
            }
        }
        "
        data argument has some fields those can be used while creating the input:
            data.formType: Can be 'create' or 'edit' according to the form.
            data.form: Reference to the form element as jQuery selection.
            data.record: Gets the editing record if this input is being created for edit form (if formType='edit'). So, it's undefined for 'create' form.
            data.value: Gets current value of the field. This is default value (if defined) of field for create form, current value of field for edit form.
        While jTable automatically creates appropriate input element for each field, you can use input option to create custom input elements. 
        Remember to set name attribute of input element if you want to post this field to the server.
        
    inputType: str
        The HTML <input> type attribute value to use. This has no effect if inputFunction is provided.

    inputStyle: str
        The HTML <input> elements style value to use. This has no effect if inputFunction is provided.
        
    inputWidth: str or int
        The HTML <input> elements width style value to use. This has no effect if inputFunction is provided.

    
    inputClass : str (default = none)
        A string value that can be set as the class of an input item for this field in create/edit forms. So you can style input elements in the forms for this field. This can be useful when working with validation plug-ins (we will see soon).
    
    inputTitle : str (default = none)
        This option can be used to show a different title for a field in edit/create forms. If it's not set, input title will be same as title option.
    
    defaultValue : str (default = none)
        You can set a default value for a field. It must be a valid value. For instance, if the field is an option list, it must be one of these options.
    
    options : string, array, URL or a function  (default: none)
         http://www.jtable.org/ApiReference/FieldOptions#fopt-options
         If this field's value will be selected in an option list (combobox as default, can be radio button list),
         you must supply a source. An option source can be one of these values:
            string: forms a javascript object Property names are values, property values are display texts.
                e.g. '{ '1': 'Home phone', '2': 'Office phone', '3': 'Cell phone' }'
                the string must start with { to be sent as a javascript object and not a javascript string
            list: An list of OptionTuples
                e.g. [ OptionTuple('1','Home phone'), OptionTuple('2','Office phone'), OptionTuple('3','Cell phone')]
                Also, if values of your options are same as display texts, you can write as shown below:
                options: ['1','2','3','4']
            URL: A URL to download the option list for this field.
                e.g. '/Demo/GetPhoneTypes.php'
                Your URL must return array of options with column Value and DisplayText formatted the same way as the query results.
                If you need it to be different for each row, use the function style below, otherwise the options can't be cached properly.
            function: A function that takes some arguments and returns an object, an array or a URL string.
                e.g.
                 "
                 function(data) {
                    if (data.source == 'list') {
                        //Return url all options for optimization.
                        return '/Demo/GetPhoneTypes.php?UserType=0';
                    }
                    //This code runs when user opens edit/create form to create combobox.
                    //data.source == 'edit' || data.source == 'create'
                    return '/Demo/GetPhoneTypes.php?UserType=' + data.record.UserType;
                }
                "
    
    dependsOn : string or array  (default = none)
        This option is used to create cascaded dropdowns. If a combobox field depends on another combobox, jTable can automatically create cascaded dropdowns.
        A field can be depended to more than one field. In this case, you can write fields separated by comma as dependsOn: 'ContinentalId,CountryId' or as an array like dependsOn: ['ContinentalId', 'CountryId']
        See http://www.jtable.org/ApiReference/FieldOptions#fopt-dependsOn
    
    searchable: boolean (default = True)
        Should this field be included in the all columns search.
    
    searchField: str (default = sSearch_{columnName}
        Search form field name for this column.
    
    searchUsingLike: boolean (default = False)
        Search using like?
    
    searchSAColumn: SQLAlchemy Column to use when filtering (also used for sorting)
    
    formatStr: str (default = none)
        A python string format specifier to use. e.g. '6.2f'
        
        See https://docs.python.org/3/library/string.html#grammar-token-format_spec  
        See http://strftime.org/ for date time formats

    """

    def __init__(self, sa_column=None, column_name=None, **kwargs):
        self.log = logging.getLogger(__name__)
        self.saColumn = sa_column

        # Add all valid settings to this instance
        self.attribute_name = None
        self.title = None
        self.key = None
        self.create = None
        self.list = None
        self.edit = None
        self.dataType = None
        self.dateDisplayFormat = None
        self.checkboxFalseValue = '0'
        self.checkboxFalseText = 'No'
        self.checkboxTrueValue = '1'
        self.checkboxTrueText = 'Yes'
        self.checkboxFormText = None
        self.checkboxSetOnTextClick = None
        self.listClass = None
        self.displayFunction = None
        self.width = None
        self.columnResizable = None
        self.visibility = None
        self.sorting = None
        self.inputClass = None
        self.inputTitle = None
        self.inputFunction = None
        self.inputType = None
        self.inputStyle = None
        self.inputWidth = None
        self.defaultValue = None
        self.options = None
        self.dependsOn = None

        self.searchable = True
        self.searchField = None
        self.searchUsingLike = False
        self.searchSAColumn = None
        self.formatStr = None

        self._javascript_definition_lines = 0
        self._javascript_definition = None

        # Set members based on passed arguments (rejects any attributes that don't already exist)
        for k, v in kwargs.items():
            if hasattr(self, k):
                setattr(self, k, v)
            else:
                raise TypeError("Invalid keyword argument {}".format(k))

        # Note this needs to be set after the searchFieled member is created
        self._columnName = None
        if column_name is not None:
            self.column_name = column_name
        elif self.saColumn is not None:
            if hasattr(self.saColumn, 'name'):
                self.column_name = self.saColumn.name
            else:
                raise ValueError('columnName needs to be set for property {}'.format(self.saColumn))
            if '.' in self.column_name:
                parts = self.column_name.split('.')
                self.column_name = parts[-1]

        # Check values passed in
        if self.dataType is not None:
            self.dataType = self.dataType.lower()
            assert self.dataType in ['text', 'password', 'textarea', 'date', 'radiobutton', 'checkbox',
                                     'hidden'], "dataType {} is not valid".format(self.dataType)
        if self.dateDisplayFormat and self.dataType != 'date':
            raise ValueError("dateDisplayFormat is only valid for a date column")
        if self.dataType != 'checkbox':
            if self.checkboxFormText:
                raise ValueError("checkboxFormText is only valid for a checkbox column")
            if self.checkboxSetOnTextClick:
                raise ValueError("checkboxSetOnTextClick is only valid for a checkbox column")

        # self.log.debug(pformat(self.__dict__))

    def __str__(self):
        return self.column_name

    def __repr__(self):
        return "Column({},{})".format(self.column_name, self.saColumn)

    @staticmethod
    def js_bool(value):
        if value:
            return "true"
        else:
            return "false"

    def append_js_definiton(self, definition_entry):
        if self._javascript_definition_lines > 0:
            self._javascript_definition += ','
        self._javascript_definition += '\n'
        self._javascript_definition += '    '
        self._javascript_definition += definition_entry
        self._javascript_definition_lines += 1

    def append_simple_js_definiton(self, attribute_name, override_name=None):
        attr_val = getattr(self, attribute_name)
        if attr_val is not None:
            if override_name is not None:
                attribute_name = override_name
            self.append_js_definiton("{}: '{}' ".format(attribute_name, attr_val))

    def append_simple_js_definiton_nq(self, attribute_name, override_name=None):
        attr_val = getattr(self, attribute_name)
        if attr_val is not None:
            if override_name is not None:
                attribute_name = override_name
            if isinstance(attr_val, bool):
                attr_val = Column.js_bool(attr_val)
            self.append_js_definiton("{}: {} ".format(attribute_name, attr_val))

    def javascript_definition(self, arguments=None):
        if self._javascript_definition is None:
            assert self.column_name, "columnName is required"
            self._javascript_definition = self.column_name + ": {"
            self.append_simple_js_definiton('title')
            self.append_simple_js_definiton_nq('key')
            self.append_simple_js_definiton_nq('create')
            self.append_simple_js_definiton_nq('list')
            self.append_simple_js_definiton_nq('edit')
            self.append_simple_js_definiton('dataType', 'type')
            self.append_simple_js_definiton('listClass')
            self.append_simple_js_definiton_nq('displayFunction', 'display')
            if self.width is not None:
                if not str(self.width).endswith('%'):
                    pct = '%'
                else:
                    pct = ''
                self.append_js_definiton("width: '{val}{pct}'".format(val=self.width, pct=pct))

            self.append_simple_js_definiton_nq('columnResizable')
            self.append_simple_js_definiton_nq('sorting')
            self.append_simple_js_definiton('inputClass')
            self.append_simple_js_definiton('inputTitle')
            self.append_simple_js_definiton('defaultValue')
            if self.inputFunction is not None:
                self.append_simple_js_definiton_nq('inputFunction', 'input')
            elif (self.inputType is not None or
                  self.inputWidth is not None or
                  self.inputStyle is not None):
                if self.inputType is None:
                    self.inputType = "text"
                style = self.inputStyle or ''
                if self.inputWidth is not None:
                    style += ';width:{width}'.format(width=self.inputWidth)
                style_entry = 'style="{style};"'.format(style=style)
                inputFunction = \
                    """                  
                    function (data) {{
                        return '<input type="{inputType}" name="{columnName}" {style_entry} value="' + data.value + '" />';
                    }}
                    """
                textwrap.dedent(inputFunction)
                inputFunction = inputFunction.format(inputType=self.inputType,
                                                     columnName=self.column_name,
                                                     style_entry=style_entry,
                                                     )

                self.append_js_definiton("input: " + inputFunction)
            if self.visibility is not None:
                if isinstance(self.visibility, Visibility):
                    self.append_js_definiton("visibility: '{}' ".format(self.visibility.name))
                else:
                    self.append_js_definiton("visibility: '{}' ".format(self.visibility))
            if self.options is not None:
                if hasattr(self.options, '__call__'):
                    # pylint: disable=not-callable
                    options = self.options(arguments)
                else:
                    options = self.options
                if isinstance(options, list):
                    self.append_simple_js_definiton("options: {}".format(options))
                elif options.strip().startswith('{') or options.strip().startswith('function'):
                    self.append_simple_js_definiton("options: {}".format(options))
                else:
                    self.append_js_definiton("options: '{}' ".format(options))
            if self.dependsOn is not None:
                if isinstance(self.dependsOn, list):
                    self.append_js_definiton("dependsOn: {}".format(self.dependsOn))
                else:
                    self.append_js_definiton("dependsOn: '{}' ".format(self.dependsOn))
            if self.dataType == 'checkbox':
                self.append_js_definiton(
                    "values: {{ '{false_value}':'{false_text}', '{true_value}':'{true_text}',  }}".format(
                        false_value=self.checkboxFalseValue,
                        false_text=self.checkboxFalseText,
                        true_value=self.checkboxTrueValue,
                        true_text=self.checkboxTrueText,
                        )
                    )
            self.append_simple_js_definiton('checkboxFormText', 'formText')
            self.append_simple_js_definiton_nq('checkboxSetOnTextClick', 'setOnTextClick')
            self._javascript_definition += "}"

        return self._javascript_definition

    @property
    def column_name(self):
        return self._columnName

    @column_name.setter
    def column_name(self, value):
        self._columnName = value
        if not self.searchField and value:
            self.searchField = str(self.column_name)
