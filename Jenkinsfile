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

pipeline {
    agent { label "ub-jen" }
    tools {
        maven "MAVEN3.9"
        jdk "JDK17"
    }
    environment{
        USER_NAME = "admin"
        PASSWORD = ""
        MY_TEXT = "hello world from environment"
        SONARQUBE_ENV = "SONAR6.2"
        SINAR_CUBE_SERVER ="sonarcube_server"
    }
    stages{
        stage ("code checkout") {
            steps{
                // ## git branch: "atom" , url:"https://github.com/hkhcoder/vprofile-project.git" 
                checkout([
                      $class: 'GitSCM',
                      branches: [[name: '*/atom']],
                      userRemoteConfigs: [[
                        url: "https://github.com/hkhcoder/vprofile-project.git"  ,
                        credentialsId: 'gh-token-id'
                      ]]
                    ])
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

        stage('SonarQube Scan') {
            steps {
                withSonarQubeEnv("${SINAR_CUBE_SERVER}") {
                    sh """
                    sonar-scanner \
                      -Dsonar.projectKey=imazy-jenkins-project \
                      -Dsonar.sources=. \
                      -Dsonar.java.binaries=target/classes
                    """
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