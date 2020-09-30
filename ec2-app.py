#! /bin/bash/
            yum update -y
            yum install python3 -y
            pip3 install flask
            cd /home/ec2-user
            wget https://raw.githubusercontent.com/serdarcw/clarusway-aws-eu-workshop/master/aws/projects/001-roman-numerals-converter/app.py
            mkdir templates
            cd templates
            wget https://raw.githubusercontent.com/serdarcw/clarusway-aws-eu-workshop/master/aws/projects/001-roman-numerals-converter/templates/index.html
            wget https://raw.githubusercontent.com/serdarcw/clarusway-aws-eu-workshop/master/aws/projects/001-roman-numerals-converter/templates/result.html
            cd ..
            python3 app.py
            
            
            
            #seguntalternatif
            
            #! /bin/bash
            yum update -y
            yum install python3 -y
            pip3 install flask
            cd /home/ec2-user
            wget -P templates https://raw.githubusercontent.com/serdarcw/clarusway-python-workshop/master/001-project-roman-numerals-converter/templates/index.html
            wget -P templates https://raw.githubusercontent.com/serdarcw/clarusway-python-workshop/master/001-project-roman-numerals-converter/templates/result.html
            wget https://raw.githubusercontent.com/serdarcw/clarusway-python-workshop/master/001-project-roman-numerals-converter/app.py 
            python3 app.py
