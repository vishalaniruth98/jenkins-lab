
pipeline {
    agent any 
    stages {
        stage('build') {
            steps {
               sh '''
               pip install virtualenv
               virtualenv venv
               source venv/bin/activate
               '''
            }  
        }
        stage('test') {
            steps {
                echo 'testing the application'
            }  
        }
        stage('deploy') {
            steps {
                echo 'deploying the application'
            }  
        }
    }
}
