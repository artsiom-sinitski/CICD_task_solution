pipeline {
    agent any
    stages {
        stage('CI step') {
            steps {
                echo "Executing test cases..."
                sh "pytest ./tests/test_AdventureWorks2019DB.py"
            }
        }
        stage('CD step') {
            steps {
                echo "Copiying cource code to release branch..."
            }
        }
    }
}