#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Add ACL to the bucket. Grant Read privilages to the bucket using canonical user id
- Info   : Add ACL to the bucket. Grant READ privilages to the bucket using canonical user id of the AWS Account
            * 101-s3-aws
"""

import boto

def addacl(name):
   bucket = conn.get_bucket(name)
   bucket.add_user_grant("READ","ba54237358a1eaafd46b06257a8e7a8023f71e243b86bfaef3e9e25429b401cc")
   print "Added ACL to the Bucket named ", bucket.name, " "

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   addacl(bucketname)
