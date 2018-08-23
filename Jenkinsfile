pipeline {
    agent any
    triggers {
        cron('H */4 * * 1-5')
    }
    stages {
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
