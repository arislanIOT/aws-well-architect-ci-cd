# Documentation for aws ci/cd pipeline using Aws service. 

## Services Used and Count

| Service          |  Nos |
|------------------|------|     
| Cloudwatch Event | 1    |
| Lambda Fucntions | 5    |
| Ec2 Image Builder| 2    |
| CodePipeLine     | 2    |
| CodeCommit       | 2    |
| CodeDeploy       | 2    |
| Sns              | 3    |
| Ec2 Instance     | 3    |
| LoadBalancer     | 1    |
| Launch Template  | 2    |
| Auto ScalingGroup| 1    |




Here the process is divided into two pipeline. One pipeline is called QAT and other one is Production. Both the pipline have codecommit attached to the same repo and master branch. 

## Custom settings created for this project

- Both the pipeline is executed using Lambda Fucntions, ie pipeline won't start on each code change. 

- Here more robust approach of deployment is taken with the creating AMI on each code push and deploying the instance with the latest AMI using Blue/ Green deployment strategy. 

- The architecture diagram is self explainatory

## Steps for the Infrastructure Setup

- create a codecommit repository with branch on master 

- create an application in codedeploy

- create a deployment group under the codedeploy application.

