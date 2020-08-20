pipeline {
    agent any

    stages {
        stage('Clean up'){
            steps {
                sh "rm -rf jenkins-repo"
                sh "rm -rf pyenv"
            }
        }
        
        stage('Check out SCM') {
            steps {
                sh """
                sudo yum update -y
                sudo yum install git -y
                git clone https://github.com/ragavi9798/jenkins-repo.git
                """
            }
        }
        
        stage('Build') {
            steps {
                sh """
                    sudo yum install python3 -y
                    python3 -m venv pyenv
                    . pyenv/bin/activate
                    cd jenkins-repo
                    python3 test_emp.py
                   """
            }
        }
        
        stage('Deploy') {
            steps {
                sh "sudo ssh -i '$WORKSPACE/20954-quantiphi.pem' -o StrictHostKeyChecking=no ec2-user@54.90.71.24 ls -la"
                sh "sudo scp -i '$WORKSPACE/20954-quantiphi.pem' -o StrictHostKeyChecking=no -r try.txt ec2-user@54.90.71.24:/tmp"
            }
        }
    }
}
