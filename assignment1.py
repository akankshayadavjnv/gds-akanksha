import logging
def lambda_handler(event, context):
    # accessing objet_name and object_size from event dictionary
    object_name = event["Records"][0]["s3"]["object"]["key"]
    object_size = event["Records"][0]["s3"]["object"]["size"]
    logging.warning("Size of {} object is {}B".format(object_name,object_size))
    #if object size is greater than 100MB then will log a alert to cloud watch
    if object_size > 100*1024*1024:
        logging.critical("file size is greater than 100bytes")