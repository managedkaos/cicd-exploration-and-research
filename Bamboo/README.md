# Bamboo
- https://confluence.atlassian.com/bamboo/installing-bamboo-on-linux-289276792.html
- https://confluence.atlassian.com/bamboo/running-bamboo-as-a-linux-service-416056046.html
- https://www.atlassian.com/software/bamboo/download-archives
- https://www.atlassian.com/software/bamboo/downloads/binary/atlassian-bamboo-9.3.2.tar.gz
- https://www.atlassian.com/software/bamboo/downloads/binary/atlassian-bamboo-9.2.4.tar.gz
- https://hub.docker.com/r/atlassian/bamboo-server
- https://my.atlassian.com/products/index?sen=19607160&evalId=19607160&eval=true#license_19607160


- /etc/systemd/system/bamboo.service
```
[Unit]
Description=Atlassian Bamboo
After=syslog.target network.target

[Service]
Type=forking
User=bamboo
Environment=CATALINA_PID=/var/bamboo/current/bin/Catalina.pid
PIDFile=/bamboo/current/bin/Catalina.pid
ExecStart=/var/bamboo/current/bin/start-bamboo.sh
ExecStop=/var/bamboo/current/bin/stop-bamboo.sh
SuccessExitStatus=143

[Install]
WantedBy=multi-user.target
```

    1  mysql -u root --password='application'
    2  ls
    3  cd /tmp
    4  ls
    5  ls -ltr
    6  cd bamboo/
    7  ls
    8  cd atlassian-bamboo-9.3.2/
    9  ls
   10  mysql --host=localhost --user=application --password= application application
   11  mysql --host=localhost --user=application --password=application application
   12  pwd
   13  ls
   14  cat README.txt
   15  yum install  java-17-amazon-corretto
   16  cat README.txt
   17  java -version
   18  echo $JAVA_HOME
   19  yum install java-17-amazon-corretto-devel
   20  echo $JAVA_HOME
   21  sudo find /usr/lib/jvm /usr/local /opt -name "javac"
   22  export JAVA_HOME=/usr/lib/jvm/java-17-amazon-corretto.x86_64/bin/
   23  echo $JAVA_HOME
   24  cat README.txt
   25  /usr/sbin/useradd --create-home --home-dir /usr/local/bamboo --shell /bin/bash bamboo
   26  vim atlassian-bamboo/WEB-INF/classes/bamboo-init.properties
   27  vim /etc/systemd/system/bamboo.service
   28  ls
   29  cd bin
   30  ls
   31  ls -ltr
   32  ./start-bamboo.sh
   33  cd ..
   34  cat bamboo.sh
   35  cd ..
   36  ls
   37  cd ..
   38  ls
   39  mv bamboo/ /var/bamboo
   40  cd /var/bamboo/
   41  ls
   42  vim /etc/systemd/system/bamboo.service
   43  cd atlassian-bamboo-9.3.2/
   44  cd bin/
   45  ls
   46  ls -ltr
   47  pwd
   48  ./start-bamboo.sh
   49  yum install java-17-amazon-corretto-devel
   50  export JAVA_HOME=/usr/lib/jvm/java-17-amazon-corretto.x86_64/bin
   51  ./start-bamboo.sh
   52  export JAVA_HOME=/usr/lib/jvm/java-17-amazon-corretto.x86_64/
   53  ./start-bamboo.sh
   54  systemctl enable bamboo
   55  systemctl start bamboo
   56  systemctl status bamboo
   57  systemctl status bamboo -f
   58  systemctl status bamboo -l
   59  pwd
   60  ls
   61  cd ..
   62  ls
   63  cd ..
   64  ls
   65  pwd
   66  ln -s $(pwd)/atlassian-bamboo-9.3.2 current
   67  cd current/
   68  ls
   69  pwd
   70  vim /etc/systemd/system/bamboo.service
   71  systemctl daemon-reload
   72  systemctl enable bamboo
   73  systemctl start bamboo
   74  systemctl status bamboo
   75  pwd
   76  cd ..
   77  ls
   78  ls -ltr
   79  chown -R atlassian-bamboo-9.3.2 bamboo:bamboo
   80  chown -R bamboo:bamboo ./atlassian-bamboo-9.3.2/
   81  systemctl start bamboo
   82  systemctl status bamboo
   83  touch /var/bamboo/current/logs/catalina.out
   84  pwd
   85  cd current/
   86  ls
   87  mkdir logs
   88  cd ..
   89  chown -R bamboo:bamboo ./atlassian-bamboo-9.3.2/
   90  systemctl start bamboo
   91  systemctl status bamboo
   92  ./current/bin/start-bamboo.sh -fg
   93  history


- for the cloudformation installation
          sources:
            /var/bamboo/: 'https://www.atlassian.com/software/bamboo/downloads/binary/atlassian-bamboo-9.3.2.tar.gz'
