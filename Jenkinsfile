pipeline {
    agent any
 
    environment {
        STUDENT_NAME    = 'Viktor'
        STUDENT_SURNAME = 'Kim'
        STUDENT_GROUP   = 'IT2-2313'
        STUDENT_ID      = '37145'
        IMAGE_NAME      = 'viktor-kim-devops'
        CONTAINER_NAME  = 'viktor-kim-container'
    }
 
    stages {
        stage('Checkout') {
            steps {
                checkout scm
                sh 'git log --oneline -1'
            }
        }
        stage('Build') {
            steps {
                sh '''
                    echo "Student:  "
                    echo "Group: "
                    echo "Student ID: "
                    bash -n scripts/Viktor_Kim_system.sh
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    test -f Viktor_Kim_info.txt
                    test -f Dockerfile
                    bash scripts/Viktor_Kim_system.sh
                '''
            }
        }
        stage('Docker Build') {
            steps {
                sh 'docker build -t  .'
            }
        }

        stage('Docker Run') {
            steps {
                sh '''
                    docker rm -f  || true
                    docker run -d --name                        -e STUDENT_NAME=                       -e STUDENT_SURNAME=                       -e STUDENT_GROUP=                       -e STUDENT_ID=                       
                    sleep 3
                    docker logs 
                '''
            }
        }
    }
}
