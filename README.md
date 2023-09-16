# CI/CD Exploration and Research

## References and Resources
- [Best Continuous Integration Tools for 2023 ‒ Survey Results](https://blog.jetbrains.com/teamcity/2023/07/best-ci-tools/)
- [DevOps Foundations: Infrastructure as Code Course Handout](./Documents/Infrastructure_as_Code_Course_Handout.pdf)
- [DevOps Foundations: Infrastructure as Code Lab Setup Instructions](./Documents/Infrastructure_as_Code_Lab_Setup_Instructions.pdf)
- [How to Launch AWS Elastic beanstalk using Terraform](https://automateinfra.com/2021/03/24/how-to-launch-aws-elastic-beanstalk-using-terraform/)
- [Hands-on AWS CloudFormation - Part 5. IAM users, groups and roles](https://dev.to/tiamatt/hands-on-aws-cloudformation-part-5-iam-users-groups-and-roles-5d9f)
- [IAM_Users_Groups_and_Policies.yaml](https://github.com/awslabs/aws-cloudformation-templates/blob/master/aws/services/IAM/IAM_Users_Groups_and_Policies.yaml)
- [Launching a Jenkins Master using AWS CloudFormation](http://beta.awsdocs.com/infrastructure_as_code/cloudformation/applications/jenkins_cf_deployment/)
- [Elastic Beanstalk template snippets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-elasticbeanstalk.html)


## Tools
### Bamboo
- [Bamboo Server and Data Center feature comparison](https://confluence.atlassian.com/bamboo/bamboo-server-and-data-center-feature-comparison-1063170546.html)
- [Server Deprecation Details and Countdown](https://www.atlassian.com/migration/assess/journey-to-cloud)


## Chapters
0. Introduction
1. Self-Hosted
1. Software as a Service (SaaS)
1. Cloud Service Providers
1. Code Repositories
1. Selecting the Right CI Tool
1. Conclusion

## Sections
| Section | Title | Length | Rank | Comments |
|:--------|:------|:-------|:-----|:---------|
| 00_01   | Building your CI/CD pipeline| 1m 16s |||
| 00_02   | What you should know| 2m 25s|||
| 00_03   | Landscape of CI/CD tools and CI/CD tool categories| 1m 20s|||
| 00_04   | Pros and cons| 3m 30s|||
| 00_05   | The experimental pipeline| 3m 6s|||
| 00_06   | About the exercise files| 36s|||
| 01_01   | Jenkins| 4m 40s| 2/17| Multiple courses|
| 01_02   | Bamboo| 4m 32s| 12/17| One dated course (2018)|
| 01_03   | TeamCity| 4m 30s| 10/17|||
| 02_01   | Travis CI| 4m 9s| 6/17|||
| 02_02   | Codeship| 4m 25s| 17/17|||
| 02_03   | CircleCI| 5m 12s| 5/17|||
| 03_01   | Amazon Web Services (AWS) CodePipeline and CodeBuild| 7m 11s| 8/17| Some courses|
| 03_02   | Azure Pipelines| 5m 20s| 4/17| Two courses|
| 03_03   | Google Cloud Platform (GCP) Cloud Build| 5m| 11/17| One solid course|
| 04_01   | GitHub Actions| 5m 22s| 1/17| Multiple Courses|
| 04_02   | GitLab CI| 4m 30s| 3/17| Two solid courses|
| 04_03   | Bitbucket Pipelines| 4m 22s| 7/17|||
| 05_01   | Selecting the Right CI Tool (or better title)||||
| 05_02   | LinkedIn Courses for Further Exploration||||
| 06_01   | Next steps| 33s|||

## Courses
### Jenkins
- https://www.linkedin.com/learning/learning-jenkins-14423877
- https://www.linkedin.com/learning/jenkins-essential-training-17420152
- https://www.linkedin.com/learning/running-jenkins-on-aws-8591136

### Bamboo
- https://www.linkedin.com/learning/bamboo-essential-training (2018?)

### AWS CodePipeline
- https://www.linkedin.com/learning/devops-with-aws
- https://www.linkedin.com/learning/deploy-javascript-apps-to-aws-elastic-beanstalk

### Azure Pipelines
- https://www.linkedin.com/learning/continuous-delivery-with-azure-devops
- https://www.linkedin.com/learning/azure-devops-continuous-delivery-with-yaml-pipelines

### Google Cloud Build
- https://www.linkedin.com/learning/google-cloud-for-developers-learning-the-cloud-build-ci-cd-platform

### GitHub Actions
- https://www.linkedin.com/learning/learning-github-actions-2
- https://www.linkedin.com/learning/advanced-github-actions
- https://www.linkedin.com/learning/practical-github-actions
- https://www.linkedin.com/learning/build-and-deploy-containerized-apps-with-github-actions

### GitLab CI
- https://www.linkedin.com/learning/continuous-integration-and-continuous-delivery-with-gitlab


## Notes
- 2023-07-14
  - Added cfn template for service account, target application, and 2 environments (Staging + Production)for the application
  - need to combine them into one template
  - need to update the application, the deployment scripts, etc
  - need to update the pipelines to take the application and environment names
  - need to update upload script to take the name of the applciation and the name of the bucket

        upload-new-version.sh python-web-application-application

  - need up update the deploy script to take the application name first and the environment second.  currently in use:

        ./deploy-new-version.sh pytho-Stag-W7hgJD1LTmxb python-web-application-application

- 2023-07-14
  - Maybe use App Runner instead of Elastic Beanstalk or Lambda?
  - [AWS App Runner CloudFormation Template generated using AWS Copilot](https://gist.github.com/toricls/5c448b723e25118e683ae065ce58fa1d)



## Experimental Pipeline

Secrets:
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY

Variables:
- AWS_DEFAULT_REGION
- STAGING_FUNCTION_NAME
- STAGING_URL
- PRODUCTION_FUNCTION_NAME
- PRODUCTION_URL

1. Requirements

    python3 -m venv local
    . ./local/bin/activate
    make requirements

2. Check-Lint-Test

    . ./local/bin/activate
    make check lint test

3. Build

    make build

4. Deploy Staging

    make deploy \
        ENVIRONMENT="Staging" \
        PLATFORM="TeamCity" \
        FUNCTION=${STAGING_FUNCTION_NAME} \
        VERSION=${BUILD_VCS_NUMBER} \
        BUILD_NUMBER=${BUILD_NUMBER}

5. Test Staging

    make testdeployment URL=${STAGING_URL}

6. Deploy Production

    make deploy \
        ENVIRONMENT="Production" \
        PLATFORM="TeamCity" \
        FUNCTION=${PRODUCTION_FUNCTION_NAME} \
        VERSION=${BUILD_VCS_NUMBER} \
        BUILD_NUMBER=${BUILD_NUMBER}

7. Test Production

    make testdeployment URL=${PRODUCTION_URL}

Bamboo Make Argument:
deploy ENVIRONMENT="Staging" PLATFORM="Bamboo" FUNCTION=${bamboo.STAGING_FUNCTION_NAME} VERSION=${bamboo.planRepository.revision} BUILD_NUMBER=${bamboo.buildNumber}

Bamboo Evnrionment Variables:
AWS_ACCESS_KEY_ID=${bamboo.AWS_ACCESS_KEY_ID} AWS_SECRET_ACCESS_KEY=${bamboo.AWS_SECRET_ACCESS_KEY} AWS_DEFAULT_REGION=${bamboo.AWS_DEFAULT_REGION}