pipeline {
    agent any
    stages{
        stage('Build-image') {
            steps {
                sh ''' #!/bin/bash
                  cd /var/lib/jenkins/workspace/docker-sample/
                  docker rmi -f chatapp
                  docker build -t chatapp:$BUILD_NUMBER .
                  docker login -u manidevasani -p manisubbu@24697    
                # pushing to the Docker-hub
                # docker tag chatapp:$BUILD_NUMBER manidevasani/chatproject:$BUILD_NUMBER
                # docker push manidevasani/chatproject:$BUILD_NUMBER
                # docker tag chatapp:$BUILD_NUMBER manidevasani/chatproject:latest
                # docker push manidevasani/chatproject:latest
                # pushing to the Instance-registry
                # docker tag chatapp:$BUILD_NUMBER ubuntu:5000/chatapp:$BUILD_NUMBER
                # docker push ubuntu:5000/chatapp:$BUILD_NUMBER
                # docker tag chatapp:$BUILD_NUMBER ubuntu:5000/chatapp:latest
                # docker push ubuntu:5000/chatapp:latest
                # Pushing to the  Aws-ECR
                  $(aws ecr get-login --no-include-email --region ap-south-1)
                  docker tag chatapp:$BUILD_NUMBER 416604440517.dkr.ecr.ap-south-1.amazonaws.com/chatapp:latest
                  docker push 416604440517.dkr.ecr.ap-south-1.amazonaws.com/chatapp:BUILD_NUMBER 
                  docker tag chatapp:latest 416604440517.dkr.ecr.ap-south-1.amazonaws.com/chatapp:latest
                  docker push 416604440517.dkr.ecr.ap-south-1.amazonaws.com/chatapp:latest
                  ''' 
            }
        }
    }
}
 
  
