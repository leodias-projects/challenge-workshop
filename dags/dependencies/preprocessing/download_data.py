# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 09:23:54 2022

@author: LeonardoDiasdaRosa
"""

import boto3
import os

def main():
    s3_client = boto3.client('s3')
    s3_bucket_name = 'masters-data-region3'
    s3 = boto3.resource('s3',
                        aws_access_key_id='AKIA425K74CLYLEHA2RP',
                        aws_secret_access_key='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',
                        region_name='sa-east-1')

    bucket = s3.Bucket(s3_bucket_name)

    for files in bucket.objects.all():
        full_path = files.key.split('/')[:-1] # get only the "paths"
        for i, directory in enumerate(full_path):
            if i == 0:
                ''' 
                    Just to create the "main" directories
                '''
                if not os.path.exists(full_path[i]):
                    os.mkdir(full_path[i])
        
            else:
                '''
                    Create directories according to the S3 bucket keys
                '''
                if not (directory == "Aerodata") | (directory == "Airfoils"):
                    path = full_path[0:i+1]
                    path = '/'.join(path)
                    if not os.path.exists(path):
                        os.mkdir(path)
                        print("downloading "+path)
        
        file_name = files.key.split('/')[-1]
        path_name = '/'.join(full_path)
        
        if file_name.endswith('.out'):
            if not os.path.isfile(path_name+'/'+file_name):
                bucket.download_file(files.key, path_name+'/'+file_name)
    print("Finished downloading!")


if __name__ == "__main__":
    main()
