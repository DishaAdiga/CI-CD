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
                    echo "Commit Message: ${commitMessage}"
                    def status = sh(script: """
                        . venv/bin/activate
                        python3 analyze_commit.py "${commitMessage}"
                        """, returnStatus: true) 
                    if (status != 0) {
                        error("❌ Build failed due to bad commit message")
                    }
                }
            }
        }
    }
}