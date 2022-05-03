pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Clean the workspace'
          
             //   cleanWs()
             //  sh 'cp -r C:\Users\Administrator\Desktop\amazingkart\db.sqlite3 .'
             //  sh 'cp -r C:\Users\Administrator\Desktop\amazingkart\.env .'
            }
        }
        stage('workspace clone') {
            steps {
                echo 'workspace clone'
                git branch: 'main', credentialsId: 'Amazing kart', url: 'https://github.com/narayanareddy11/amazingkart.git'
    
                
            }
        }
        stage('Test server') {
            steps {
                echo 'Test the server'
              //  sh 'python manage.py test'
    
            }
        }
        stage('Runserver') {
            steps {
                echo 'Clean the workspace'
                echo "Running ${env.BUILD_ID} on ${env.JENKINS_URL}"
                echo "python manage.py runserver"
    
            }
        }
        stage('artifacts') {
            steps {
                echo 'archiveArtifacts for kart setup'
                archiveArtifacts artifacts: 'templates', followSymlinks: false
            }
        }
        stage('Mail Notification') {
            steps {
                echo 'Mail Report'
                mail bcc: '', body: 'job succus amazingkart  Running ${env.BUILD_ID} on ${env.JENKINS_URL} ', cc: '', from: '', replyTo: '', subject: 'Test Jenkins', to: '6reddy6@gmail.com'
      
            }
        }
    }
}
