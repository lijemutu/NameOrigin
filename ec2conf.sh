sudo yum update -y;sudo yum install docker -y;sudo service docker start;sudo usermod -a -G docker ec2-user;sudo systemctl enable docker;sudo curl -L "https://github.com/docker/compose/releases/download/1.28.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose; sudo chmod +x /usr/local/bin/docker-compose;sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose;sudo yum install git -y;git clone https://github.com/lijemutu/NameOrigin.git;cd NameOrigin;echo 'API_KEY_NAMES=900670bcbd8a496c9bdda4c19670b110' > apikey.env;sudo chmod u+x entrypoint.sh;sudo docker-compose -f docker-compose.dev.yml up -d;cd ..;mkdir nginx;cd nginx;touch Dockerfile;touch nginx.conf;echo -e "FROM nginx \n RUN rm /etc/nginx/conf.d/default.conf \n COPY nginx.conf /etc/nginx/conf.d/default.conf\n COPY ser.key /etc/nginx/\n COPY ser.pem /etc/nginx/\n COPY nginx.conf /etc/nginx/\n EXPOSE 80 443\n CMD [\"nginx\", \"-g\", \"daemon off;\"]" > Dockerfile; echo -e "server {\n listen 80; \n location / { \n proxy_pass http://app:5000; \n proxy_set_header Host $host; \n proxy_set_header X-Real-IP $remote_addr; \n proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for; \n }\n }" > nginx.conf;docker build -t nginx .;docker run -p 80:80 --network=nameorigin_default -d nginx 