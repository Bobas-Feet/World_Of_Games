pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                dir('WoG-project') {
                    sh 'docker-compose build'
                }
            }
        }

        stage('Run') {
            steps {
                dir('WoG-project') {
                    sh 'docker-compose up -d'
                }
            }
        }

        stage('Test') {
            steps {
                dir('WoG-project') {
                    sh 'python3 e2e.py'
                }
            }
        }

        stage('Finalize') {
            steps {
                dir('WoG-project') {
                    sh 'docker-compose down'
                    sh 'docker-compose push'
                }
            }
        }
    }
}