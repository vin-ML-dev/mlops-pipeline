pipeline {
    agent {
        docker {
            image 'vin1989/mlimage'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
            reuseNode true
        }
    }

    environment {
        DOCKER_REGISTRY = "docker.io/vin1989"
        DOCKER_IMAGE = "mlops-image"
        CONTAINER_NAME = "my-model"
        
        
    }

    stages {
        
        
        stage('Preprocessing stage') {
            steps {
                  

                   sh 'python3 preprocessing.py'
                   echo "Data prepared"
               }
           }
           
        stage('Train Model') {
            steps {
                script {
                    sh 'python3 train.py'
                }
            }
        }

        stage('Test Model') {
            steps {
                script {
                    sh 'python3 test.py'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    
                    sh "docker build -t $DOCKER_IMAGE ."
                    sh "docker push $DOCKER_IMAGE"
                }
            }
        }

        stage('Deploy') {
            steps {
               sh 'docker stop $CONTAINER_NAME || true'
               sh 'docker rm $CONTAINER_NAME || true'
               sh 'docker run -p 5000:5000 --name $CONTAINER_NAME  $DOCKER_IMAGE'
            }
        }
    }

    post {
        always {
            cleanWs()
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}

