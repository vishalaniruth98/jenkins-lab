
pipeline {
    agent any 
    stages {
        stage('build') {
            steps {
               sh '''
               pip3 install venv
               venv --no-site-packages
               source bin/activate
               '''
            }  
        }
        
        stage('Run') {
            steps {
               sh 'python3 calci.py'
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
