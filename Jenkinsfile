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
    }
    stages{
        stage ("code checkout") {
            steps{
                git url:"https://github.com/hkhcoder/vprofile-project.git" , branch: "atom"
            }
        }
        stage ("run maven command"){
            steps{
                echo "####################################################"
                sh "java -version"
                echo "####################################################"
                echo "this is user name : ${USER_NAME}"
                echo "####################################################"
                echo "####################################################"
                sh "mvn clean test"
            }
        }
    }
}