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
                def commitMessage = sh(script: "git log -1 --pretty=%B", returnStdout: true).trim()
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install textblob
                python3 analyze_commit.py "${commitMessage}"
                '''
            }
        }
    }
}
