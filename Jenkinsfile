/*
//  jenkins file have four important sections 
pipeline{
    agent  {
            label "master"
            }
    tools {
            maven "Maven"
            }
    environment{
            var=value
            }
    stages{
            stage() {}
            stage() {}
        }
}
*/

pipeline{
    agent { label "ub-jen" }
    tools {
        maven "MAVEN3.9"
        jdk "JDK17"
    }
    environment{
        USER_NAME = "admin"
        PASSWORD = "4223"
        MY_TEXT = "hello world from environment"
        SONARQUBE_ENV = "SONAR6.2"
    }
    stages{
        stage ("code checkout") {
            steps{
                git url:"https://github.com/hkhcoder/vprofile-project.git" , branch: "atom"
            }
        }

        stage('BUILD'){
            steps {
                echo "####################################################"
                sh "java -version"
                echo "####################################################"
                sh 'mvn clean install -DskipTests'
            }
            post {
                success {
                    echo "Now Archiving..."
                    archiveArtifacts artifacts: "**/target/*.war"
                }
                failure {
                    echo 'Build failed. No artifacts will be archived.'
                }
            }
        }

        stage ("TEST"){
            steps{
                sh "mvn clean test"
            }
        }

        stage ('CODE ANALYSIS WITH CHECKSTYLE'){
            steps {
                sh 'mvn checkstyle:checkstyle'
            }
            post {
                success {
                    echo 'Generated Analysis Result'
                }
            }
        }
    }
}