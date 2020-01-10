pipeline {
    agent any
    stages{
        stage('Deploy') {
            steps {
                sh ''' #!/bin/bash
                echo Branch :: Production
		echo Bulding testing environment
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
