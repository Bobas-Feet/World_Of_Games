pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                dir('C:/DevOps/WoG-project') {
                    bat 'docker-compose build'
                }
            }
        }

        stage('Run') {
            steps {
                dir('WoG-project') {
                    bat 'docker-compose up -d'
                }
            }
        }

        stage('Test') {
            steps {
                dir('WoG-project') {
                    bat 'e2e.py'
                }
            }
        }

        stage('Finalize') {
            steps {
                dir('WoG-project') {
                    bat 'docker-compose down'
                    bat 'docker-compose push'
                }
            }
        }
    }
}