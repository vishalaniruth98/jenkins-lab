pipeline {
    agent any 
    stages {
        stage('build') {
            steps {
               // sh 'sudo apt-get install python3-pip'
                sh 'pip3 install virtualenv \ virtualenv venv \ source venv/bin/activate'
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
