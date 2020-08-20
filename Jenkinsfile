pipeline {
    agent any

    stages {
        stage('Clean up'){
            steps {
                sh "rm -rf jenkins-repo"
                sh "rm -rf venv"
            }
        }
        
        stage('Check out SCM') {
            steps {
                sh """
                sudo apt-get update -y
                sudo apt-get install git -y
                git clone https://github.com/vishalaniruth98/jenkins-repo.git
                """
            }
        }
        
        stage('Build') {
            steps {
                sh """
                    sudo apt-get install python3 -y
                    sudo virtualenv pyenv
                    . pyenv/bin/activate
                    cd jenkins-repo
                    python3 main.py
                   """
            }
        }
        
        stage('Deploy') {
            steps {
                sh "sudo ssh -i '$WORKSPACE/20953-jenkins.pem' -o StrictHostKeyChecking=no -p 22  ec2-user@34.232.72.17 ls -la"
                sh "sudo scp -i '$WORKSPACE/20953-jenkins.pem' -o StrictHostKeyChecking=no -r try.txt ec2-user@34.232.72.17:/tmp"
            }
        }
    }
}
