pipeline {
    agent any
    stages {
        stage('Setup Python Virtual Environment') {
            steps {
                script {
                    sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install textblob
                    '''
                }
            }
        }
        stage('Analyze Commit') {
            steps {
                script {
                    def commitMessage = sh(script: 'git log -1 --pretty=%B', returnStdout: true).trim()
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
}