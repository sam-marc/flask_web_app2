pipeline {
    agent any

    tools {
        // Define the git tool
        git 'Default'
    }

    stages {
        stage('Echo') {
            steps {
                sh "chmod -R 755 ${env.WORKSPACE}"
            }
        }

        stage('Clone repository') {
            steps {
                script { 
                    // Specify the target directory
                    def targetDir = "${env.WORKSPACE}"
                    // Clone the repo into the specified directory
                    dir(targetDir) {
                        git branch: 'main', url: 'https://github.com/ctoweh/flask_web_app.git'
                    }
                }
            }
        }

        stage('Configure servers') {
            steps {
                sh "cd ${env.WORKSPACE}/ && ansible-playbook /flask_app/tasks/main.yml -i hosts.ini"
            }
        }

        stage('Build app.py') {
            steps {
                sh "cd ${env.WORKSPACE}/ && ansible-playbook -e 'external_yaml_file=app.py' /flask_app/tasks/main.yml -i hosts.ini"
            }
        }

        stage('Run Ansible playbook') {
            steps {
                ansiblePlaybook credentialsId: 'ansible-master', 
                                installation: 'Ansible', 
                                inventory: '/home/centos/flask_web_app/hosts.ini', 
                                playbook: '/home/centos/flask/_app/tasks/main.yml', 
                                vaultTmpPath: ''
            }
        }
    }

    post {
        always { 
            emailext body: 'Check console output at $BUILD_URL to see the results.',
                subject: '$PROJECT_NAME - Build # $BUILD_NUMBER - $BUILD_STATUS!',
                to: 'towehcorina@gmail.com'
        }
    }
}