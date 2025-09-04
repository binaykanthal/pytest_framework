pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/binaykanthal/pytest_framework.git'
            }
        }

        stage('Set up Python') {
            steps {
                bat '''
                python -m venv venv
                call venv\\Scripts\\activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }



        stage('Run Tests') {
            steps {
                bat '''
                mkdir reports
                call venv\\Scripts\\activate
                pytest --junitxml=reports\\results.xml --maxfail=1 --disable-warnings -v
                '''
            }
        }


    }

    post {
        always {
            junit 'reports\\*.xml'
        }
    }
}
