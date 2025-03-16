pipeline {
    agent any
    stages {
        stage('Setup Python Virtual Environment') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install --upgrade pip
                pip install textblob
                '''
            }
        }
        stage('Analyze Commit') {
            steps {
                sh '''
                source venv/bin/activate
                python3 analyze_commit.py
                '''
            }
        }
    }
}
