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
                        git branch: "main", url: ""
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
        always {
            emailext body: 'Check console output at $BUILD_URL to view the results.',
            subject: '$PROJECT_NAME - Build #BUILD_NUMBER =$BUILD_STATUS',
            to: 'towehcorina@gmail.com'
        }
    }
}
