pipeline {
    agent any
    parameters {
        string(name : 'select_branch',
               defaultValue : 'sub-branch'
               description : 'This brnach has pom file')
    }
    triggers {
        pollSCM('* * * * *')
    }
    stages {
        stage('Example') {
            steps {
                echo "the branch is :${params.select_branch}"
            }
        }

        stage('Build') {
            steps {
                echo 'Building..'
                bat 'mvn clean package'
            }
        }
        stage('Deploy') {
            steps {
                echo 'deploying..'
                bat 'mvn clean deploy'
            }
        }
    }
    
}
