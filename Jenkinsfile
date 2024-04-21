pipeline {
    agent {
        label 'node1'
    }

    tools {
        git 'Default'
    }

    stages {
        stage('Echo') {
            steps {
                sh "chmod -R 755 ${env.WORKSPACE}"
            }
        }

        stage('Clone Repository') {
            steps {
                script {
                    //Specify the target directory
                    def targetDir = "${env.WORKSPACE}"
                    //Clone the repo into the specified directory
                    dir(targetDir) {
                        git branch: "main", url: "https://github.com/sam-marc/flask_web_app2.git"
                    }
                }
            }
        }

        stage('Deploy with Playbook') {
            steps {
                //Execute ansible playbook for deployment
                sh "cd ${env.WORKSPACE}/ && ansible-playbook install-flask.yml -i hosts.ini"
            }
        }
    }

    post {
        success {
            mail to: "sam883marc2gmail.com",
            subject: "FlaskWebApp Succesful",
            body: "Check console output for details"
        }

        failure { 
            mail to: "sam883marc@gmail.com",
            subject: "FlaskWebApp Failed",
            body: "Check console output for details"
        }
    }
}
