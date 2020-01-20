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
                  docker tag chatapp:$BUILD_NUMBER manidevasani/chatproject:$BUILD_NUMBER
                  docker push manidevasani/chatproject:$BUILD_NUMBER
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
                  docker pull manidevasani/chatproject:$BUILD_NUMBER
                  docker run --name chatproject  --network ubuntu_network -d -p 80:8000 manidevasani/chatproject:$BUILD_NUMBER
                  docker restart db
                  docker restart ubuntu_nginx_1
                  docker restart chatproject
                  "
                '''
            }
        }
    }
}
 
 
