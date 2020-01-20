pipeline {
    agent any
    stages{
        stage('Build-image') {
            steps {
                sh ''' #!/bin/bash
                  cd /var/lib/jenkins/workspace/docker-sample/
                  docker rmi -f chatapp
                  docker build --build-arg build_num=12 -t chatapp .
                  docker login -u manidevasani -p manisubbu@24697    
                # pushing to the Docker-hub
                  docker tag chatapp:$BUILD_NUMBER manidevasani/chatproject:$BUILD_NUMBER
                  docker push manidevasani/chatproject:$BUILD_NUMBER
                  docker tag chatapp:$BUILD_NUMBER manidevasani/chatproject:latest
                  docker push manidevasani/chatproject:latest
                # pushing to the Instance-registry
                  docker tag chatapp:$BUILD_NUMBER ubuntu/chatapp:$BUILD_NUMBER
                  docker push ubuntu/chatapp:$BUILD_NUMBER
                  docker tag chatapp:$BUILD_NUMBER ubuntu/chatapp:latest
                  docker push ubuntu/chatpapp:latest
                # Pushing to the  Aws-ECR
                # $(aws ecr get-login --no-include-email --region ap-south-1)
                # docker tag chatapp:$BUILD_NUMBER 416604440517.dkr.ecr.ap-south-1.amazonaws.com/chatapp:latest
                # docker push 416604440517.dkr.ecr.ap-south-1.amazonaws.com/chatapp:BUILD_NUMBER 
                # docker tag chatapp:latest 416604440517.dkr.ecr.ap-south-1.amazonaws.com/chatapp:latest
                # docker push 416604440517.dkr.ecr.ap-south-1.amazonaws.com/chatapp:latest
                  ''' 
            }
        }
         stage('Build-Container') {
            steps {
                sh ''' #!/bin/bash           
                  ssh -i /var/lib/jenkins/.ssh/id_rsa ubuntu@10.0.3.19 "
                  cd /home/ubuntu/
                  docker rm -f chatproject
                  docker login -u manidevasani -p manisubbu@24697
                  docker pull manidevasani/chatproject:latest
                  docker run --name chatproject  --network ubuntu_network -d -p 80:8000 manidevasani/chatproject:latest
                  docker restart db
                  docker restart ubuntu_nginx_1
                  docker restart chatproject
                  "
                '''
            }
        }
    }
}
 
 
