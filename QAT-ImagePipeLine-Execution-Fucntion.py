import json
import boto3

image_pipeline = boto3.client("imagebuilder")
pipeline = boto3.client("codepipeline")



def lambda_handler(event, context):
    # TODO implement
    
    image_build = image_pipeline.start_image_pipeline_execution(
        imagePipelineArn="arn:aws:imagebuilder:us-east-1:440136985809:image-pipeline/qat-aws-well-architecht-imagebuilderpipe"
        
        )
    # response = pipeline.put_job_success_result(
    #      jobId=event['CodePipeline.job']['id']
    #     )
    return {
        'statusCode': 200,
        'body': json.dumps("image_build")
    }
