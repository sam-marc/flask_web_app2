pipeline {
    agent {
        label 'ansible-master'
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
                        git branch: "main", url: "https://github.com/ctoweh/flask_web_app.git"
                    }
                }
            }
        }

        stage('Deploy with Playbook') {
            steps {
                //Execute ansible playbook for deployment
                sh "cd ${env.WORKSPACE}/ && ansible-playbook -e 'external_yaml_file=app.py' install-flask.yml -i hosts.ini"
            }
        }
    }

    post {
        success {
            mail to: "towehcorina@gmail.com",
            subject: "FlaskWebApp Succesful",
            body: "Check console output for details"
        }

        fail { 
            mail to: "towehcorina@gmail.com",
            subject: "FlaskWebApp Failed",
            body: "Check console output for details"
        }
    }
}
