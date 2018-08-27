pipeline {
    agent any
    parameters {
        string(name : 'select_branch',
               defaultValue : 'sub-branch',
               description : 'This brnach has pom file')
    }
    triggers {
        pollSCM('5 * * * *')
    }
    stages {
        stage('Example') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: "*/${select_branch}"]],  userRemoteConfigs: [[url: "https://github.com/sagunbhuvanai/bhuvana1.git"]]])
               
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
