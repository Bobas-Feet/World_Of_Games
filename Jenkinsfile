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
                dir('C:/DevOps/WoG-project') {
                    bat 'docker-compose up -d'
                }
            }
        }

        stage('Test') {
            steps {
                dir('C:/DevOps/WoG-project/') {

                    bat 'start cmd.exe /c C:/DevOps/WoG-project/e2e.py'
                }
            }
        }

        stage('Finalize') {
             steps {

                    dir('C:/DevOps/WoG-project') {
                    bat 'docker-compose down'
                    bat 'docker-compose push'
                }
            }
        }
    }
}