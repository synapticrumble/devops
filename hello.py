import click

import boto3

@click.command()

def bucket():
    """this lists my aws S3 buckets"""
    
    s3 = boto3.client("s3")
    buckets = s3.list_buckets()
    click.echo(
            click.style(f"mybuckets: {bucket}", bg="yellow", fg="blue")
            )
            
if __name__ == "__main__":
    bucket()
    