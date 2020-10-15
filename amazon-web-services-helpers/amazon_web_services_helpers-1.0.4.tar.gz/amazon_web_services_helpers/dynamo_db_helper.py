from boto3.dynamodb.conditions import Key
from amazon_web_services_helpers.aws_helper import AwsHelper


class DynamoDbHelper:

    @staticmethod
    def getItems(tableName, key, value):
        items = None

        ddb = AwsHelper().getResource("dynamodb")
        table = ddb.Table(tableName)

        if key is not None and value is not None:
            filter = Key(key).eq(value)
            queryResult = table.query(KeyConditionExpression=filter)
            if(queryResult and "Items" in queryResult):
                items = queryResult["Items"]

        return items

    @staticmethod
    def insertItem(tableName, itemData):

        ddb = AwsHelper().getResource("dynamodb")
        table = ddb.Table(tableName)

        ddbResponse = table.put_item(Item=itemData)

        return ddbResponse

    @staticmethod
    def deleteItems(tableName, key, value, sk):
        items = DynamoDbHelper.getItems(tableName, key, value)
        if(items):
            ddb = AwsHelper().getResource("dynamodb")
            table = ddb.Table(tableName)
            for item in items:
                print("Deleting...")
                print("{} : {}".format(key, item[key]))
                print("{} : {}".format(sk, item[sk]))
                table.delete_item(
                    Key={
                        key: value,
                        sk : item[sk]
                    })
                print("Deleted...")