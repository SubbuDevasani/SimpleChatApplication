pipeline {
    agent any
    stages{  
        stage('Build-image') {
            steps {
                sh ''' #!/bin/bash
                  cd /var/lib/jenkins/workspace/chatapp/
                # docker rmi -f chatapp
                # docker build -t chatapp:$BUILD_NUMBER .
                  docker build -t chatapp:latest .
                # pushing to the Docker-hub
                # docker login -u manidevasani -p manisubbu@24697    
                # docker tag chatapp:$BUILD_NUMBER manidevasani/chatapp:$BUILD_NUMBER
                # docker push manidevasani/chatapp:$BUILD_NUMBER
                # docker tag chatapp:$BUILD_NUMBER manidevasani/chatapp:latest
                # docker push manidevasani/chatapp:latest
                # pushing to the Instance-registry
                # docker tag chatapp:$BUILD_NUMBER ubuntu:5000/chatapp:$BUILD_NUMBER
                # docker push ubuntu:5000/chatapp:$BUILD_NUMBER
                # docker tag chatapp:$BUILD_NUMBER ubuntu:5000/chatapp:latest
                # docker push ubuntu:5000/chatapp:latest
                # Pushing to the  Aws-ECR
                 $(aws ecr get-login --no-include-email --region ap-south-1)
                # docker tag chatapp:$BUILD_NUMBER 416604440517.dkr.ecr.ap-south-1.amazonaws.com/chatapp:$BUILD_NUMBER
                # docker push 416604440517.dkr.ecr.ap-south-1.amazonaws.com/chatapp:$BUILD_NUMBER 
                  docker tag chatapp:latest 416604440517.dkr.ecr.ap-south-1.amazonaws.com/chatapp:latest
                  docker push 416604440517.dkr.ecr.ap-south-1.amazonaws.com/chatapp:latest
                # aws ecs update-service --cluster ChatApp-Ec2 --service Ec2-Serice --force-new-deployment
                  ssh -i /var/lib/jenkins/.ssh/id_rsa ubuntu@10.0.3.217 "
                  kubectl scale deployment chatapp --replicas=0 -n default
                  sleep 20
                  kubectl scale deployment chatapp --replicas=2 -n default
                  "
                  '''  
            }
        }
    }
}  
 
   
