pipeline {
    agent any
    stages{
        stage('Build-image') {
            steps {
                sh ''' #!/bin/bash
                  cd /var/lib/jenkins/workspace/docker-sample/
                  docker build --build-arg build_num=12 -t chatapp .
                  docker login -u manidevasani -p manisubbu@24697                                    
                  docker tag chatapp:latest manidevasani/chatapp
                  docker push manidevasani/chatapp
                  ''' 
            }
        }
         stage('Build-Container') {
            steps {
                sh ''' #!/bin/bash           
                  ssh -i /var/lib/jenkins/.ssh/id_rsa ubuntu@10.0.3.19 "
                  cd /home/ubuntu/
                  docker rm -f chatproject
                  docker pull manidevasani/chatapp:latest
                  docker run --name chatproject  --network ubuntu_network -d -p 80:8000 ubuntu:5000/chatapp:latest
                  docker restart db
                  docker restart ubuntu_nginx_1
                  docker restart chatproject
                  "
                '''
            }
        }
    }
}
