pipeline {
    agent any
    stages{
        stage('Compile Stage'){
            steps {
                withMaven(maven : 'maven1'){
                    sh 'mvn clean compile'  
                }
            post {
                success {
                    echo 'Now Archiving...'
                    
                }
            }
        }
    }
}
}
