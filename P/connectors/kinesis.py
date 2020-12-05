import json

import boto3


class FirehoseStream:
    """
    A Kinesis stream.
    """

    def __init__(self, stream_name):
        self.client = boto3.client("firehose")
        self.stream_name = stream_name

    def put(self, data: dict):
        self.client.put_record(
            DeliveryStreamName=self.stream_name, Record={"Data": json.dumps(data)}
        )


if __name__ == "__main__":
    fh = FirehoseStream(stream_name="styx")
    fh.put(data={"data_source_name": "test_source", "values": [1, 2, 3]})
