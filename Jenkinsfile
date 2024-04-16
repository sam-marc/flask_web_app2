pipeline {
    agent { label 'ansible-master' }

    stages {
        stage('Deploy with Playbook') {
            steps {
                // Execute Ansible Playbook for deployment
                sh '/usr/bin/ansible-playbook -i /home/centos/flask_web_app/hosts.ini /home/centos/flask_web_app/install-flask.yml'
            }
        }
    }

    post { 
        success {
            echo 'Flask app deployment successful'
        }
        failure {
            echo 'Flask app deployment failed'
        }
    }
}
