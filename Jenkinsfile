pipeline {

    agent any

    stages {

        stage("cleaning ec2 instance") {

            steps{
                echo 'cleaning the directory..'
                echo 'before cleaning..'
                sh 'ssh ubuntu@18.207.210.185 ls -la'
                sh 'ssh ubuntu@18.207.210.185 rm -rf temp_deploy'
                echo 'After cleaning..'
                sh 'ssh ubuntu@18.207.210.185 ls -la'
            }
        }
        
        stage("build") {

            steps{
                echo 'building application..'
                echo 'creating virtual environment'
                sh "pwd"
                sh """
                    sudo apt-get -y install python3-pip python3-venv ssh
                    sudo touch app/history.txt
                    python3 -m venv python-env
                    . python-env/bin/activate
                    pip3 install pylint
                    """
            }
        }

        stage("linting-score") {

            steps{
                echo 'Linting the application..'
                sh 'python3 -m pylint calci.py'

            }
        }

        stage("test") {

            steps{
                echo 'testing the application..'
                sh 'python3 -m unittest discover -v'
                
            }
        }
        stage("deploy") {

            steps{
                echo 'Deploying the application..'
                echo 'removing previous deployed directory..'
                sh 'ssh ubuntu@18.207.210.185 rm -rf temp_deploy'
                echo 'create new deploy directory..'
                sh 'ssh ubuntu@18.207.210.185 mkdir -p temp_deploy'
                sh 'scp -r /var/lib/jenkins/workspace/python-virtual-env-pipeline ubuntu@18.207.210.185:/home/ubuntu/temp_deploy/'
                echo 'After moving files into ec2 instance'
                sh 'ssh ubuntu@18.207.210.185 ls -la'
                sh 'ssh ubuntu@18.207.210.185 touch temp_deploy/python-virtual-env-pipeline/app/history.txt'
                echo 'Running test application..'
                sh """
                    ssh ubuntu@18.207.210.185 python3 temp_deploy/python-virtual-env-pipeline/app/test_in_remote_calculator.py"""
               //      /ssh ubuntu@18.207.210.185 python3 calci.py/"""
                
            }
        }
    }
