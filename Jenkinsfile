pipeline {
    agent any
    stages{
        stage('Build-image') {
            steps {
                sh ''' #!/bin/bash
                  cd /var/lib/jenkins/workspace/chatapp-1/
                  docker build -t chatapp .
                  docker tag chatapp:latest ubuntu:5000/chatapp:latest
                  docker push ubuntu:5000/chatapp:latest
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
