pipeline {
    agent any
    stages{
        stage('Deploy') {
            steps {
                sh ''' #!/bin/bash
                echo Branch :: Production
		echo Bulding testing environment
		input message: 'Testing is completed'(click "proceed" to continue)
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
