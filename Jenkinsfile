
pipeline {
    agent any 
    stages {
        stage('build') {
            steps {
              echo 'hi'
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
