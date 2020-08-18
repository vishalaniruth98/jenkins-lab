
pipeline {
    post { 
        always { 
            deleteDir()
        }
    }
    agent any 
    stages {
        stage('build') {
            steps {
     //         sh ‘aws ec2 run-instances --image-id ami-02354e95b39ca8dec --count 1 --instance-type t2.micro --key-name 20953-instance --security-group-ids sg-02c5981c049b67e2d’
            sh 'sudo ./myfile.sh'
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
