pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/api_new_changes']], extensions: [], userRemoteConfigs: [[credentialsId: '2e71e8dd-67bb-4f9e-ad63-1693a71e4f3e', url: 'https://github.com/osaidkamal/DjangoRestApi.git']]])
            }
        }
    
//         stage("Docker image"){
//             steps {
//                 sh 'docker build -t osaidkamal/djangoauthapi .'
//             }
//         }
        stage("Push into docker Hub"){
            steps {
                withCredentials([string(credentialsId: 'dhubpass', variable: 'dhubpass')])  {
                sh 'docker logout'
                sh 'docker login -u osaidkamal -p ${dhubpass}'
                sh 'docker push osaidkamal/djangoauthapi'


        }
            }
        }
        stage("Docker Run") {
        steps {

               sh "docker-compose run web python manage.py migrate"
                sh "docker-compose up"


           }
        }
    }
}

