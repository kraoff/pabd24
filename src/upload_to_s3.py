"""Upload selected files to S3 storage"""
import argparse

import boto3
from dotenv import dotenv_values

BUCKET_NAME = 'pabd24'
YOUR_ID = '8'
CSV_PATH = ['data/raw/1_2024-05-16_19-11.csv',
            'data/raw/2_2024-05-16_19-11.csv',
            'data/raw/3_2024-05-16_19-11.csv']

config = dotenv_values(".env")


def main(args):
    client = boto3.client(
        's3',
        endpoint_url='https://storage.yandexcloud.net',
        aws_access_key_id=config['KEY'],
        aws_secret_access_key=config['SECRET']
    )

    for csv_path in args.input:
        object_name = f'{YOUR_ID}/' + csv_path.replace('\\', '/')
        client.upload_file(csv_path, BUCKET_NAME, object_name)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', nargs='+',
                        help='Input local data files to upload to S3 storage',
                        default=CSV_PATH)
    args = parser.parse_args()
    main(args)
