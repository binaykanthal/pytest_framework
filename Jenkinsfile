pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/yourusername/my_project.git'
            }
        }

        stage('Set up Python') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Start PostgreSQL') {
            steps {
                sh '''
                docker-compose up -d
                sleep 10  # wait for DB to be ready
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                mkdir -p reports
                .venv/Scripts/python -m pytest --junitxml=reports/results.xml --maxfail=1 --disable-warnings -v
                '''
            }
        }

        stage('Tear Down') {
            steps {
                sh 'docker-compose down'
            }
        }
    }
    post {
        always {
            junit 'reports/*.xml'
        }
    }
}
