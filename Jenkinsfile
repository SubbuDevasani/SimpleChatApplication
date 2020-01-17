pipeline {
    agent any
    stages{
        stage('Build-image') {
            steps {
                sh ''' #!/bin/bash
                  cd /var/lib/jenkins/workspace/chatapp-1/
                  docker build --build-arg build_num=12 -t chatapp .
                  docker tag chatapp:latest ubuntu:5000/chatapp:latest
                  docker push ubuntu:5000/chatapp:latest
                  ssh -i /var/lib/jenkins/.ssh/id_rsa ubuntu@10.0.3.19
                '''
            }
        }
        stage('Status') {
            agent {
                docker {
                    { image 'chatapp' }
                }
            }
        }
    }
}
