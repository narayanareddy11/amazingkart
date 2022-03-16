pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Clean the workspace'
                cleanWs()
                
            }
        }
        stage('workspace clone') {
            steps {
                echo 'workspace clone'
                git branch: 'main', credentialsId: 'Amazing kart', url: 'https://github.com/narayanareddy11/amazingkart.git'
    
                
            }
        }
        stage('Runserver') {
            steps {
                echo 'Clean the workspace'
                echo "python manage.py runserver"
    
            }
        }
        stage('artifacts') {
            steps {
                echo 'archiveArtifacts for kart setup'
                archiveArtifacts artifacts: 'template/*', followSymlinks: false
            }
        }
        stage('Mail Notification') {
            steps {
                echo 'Mail Report'
                emailext body: 'Test demo', subject: 'Sample Demo', to: '458narayana@gmail.com'
      
            }
        }
    }
}
