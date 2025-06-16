pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Construyendo el contenedor...'
                sh 'docker build -t ci-cd-app .'
            }
        }

        stage('Test') {
            steps {
                echo 'Ejecutando pruebas...'
                sh 'python3 -m unittest test_app.py'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Desplegando contenedor...'
                sh 'docker run -d --name app_ci_cd ci-cd-app'
            }
        }
    }
}
