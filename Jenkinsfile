pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                echo "Executing test cases..."
                sh "pytest ./tests/test_AdventureWorks2019DB.py"
            }
        }
        stage('Release') {
            when {
              expression {
                currentBuild.result == null || currentBuild.result == 'SUCCESS'
              }
            }
            steps {
                echo "Copying tested source code to the Release branch..."
                sh "git merge -X release master"
            }
        }
    }
}