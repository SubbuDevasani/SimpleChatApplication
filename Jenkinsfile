pipeline {
    agent any
    stages{
        stage('Deploy') {
            steps {
                sh ''' #!/bin/bash
                cd /home/ubuntu
                sudo aws deploy create-deployment --application-name chatapp-2 --deployment-group-name trail-grp  --deployment-config-name CodeDeployDefault.OneAtATime --github-location commit_Id=242f6cfdfe9cbe89786091f482dce402f98910bf,repository=ManiDevasani/SimpleChatApplication
                '''
            }
        }
        stage('Status') {
            steps {
                sh ''' #!/bin/bash
                echo Deployment started
                '''
            }
        }
    }
}
