pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/DishaAdiga/CI-CD.git'
            }
        }
        stage('Analyze Commit Message') {
            steps {
                script {
                    sh 'python3 analyze_commit.py'
                }
            }
        }
    }
}
