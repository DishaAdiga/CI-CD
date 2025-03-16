pipeline {
    agent any
    stages {
        stage('Setup Python Virtual Environment') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate 
                pip install textblob
                python3 analyze_commit.py
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
