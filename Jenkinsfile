
pipeline {
    node {
    def installed = fileExists 'bin/activate'
    if(!installed) {
        stage("Installing Python Environment") {
            sh 'virtualenv --no-sit-packages .'
        }
    }
    agent any 
    stages {
        stage('build') {
            steps {
               echo 'building'
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
