"""Main Pulumi program"""
import pulumi
import pulumi_aws as aws

# Configuration
config = pulumi.Config()
environment = config.get("environment") or "dev"

# Example S3 bucket
bucket = aws.s3.Bucket(f"{environment}-bucket",
    tags={
        "Environment": environment,
        "ManagedBy": "Pulumi"
    })

# Exports
pulumi.export("bucket_name", bucket.id)
