#FROM selenium/standalone-chrome
#RUN sudo apt update
#RUN sudo apt install software-properties-common -y
#RUN sudo add-apt-repository ppa:deadsnakes/ppa -y
#RUN sudo apt install python3.8 -y
#RUN sudo apt remove python-pip
#RUN sudo apt install python3-pip -y
#RUN sudo rm /usr/bin/python3
#RUN sudo ln -s /usr/bin/python3.8 /usr/bin/python3
#RUN sudo mkdir project
#COPY . /project
#WORKDIR /project
#RUN sudo pip3 install -r requirements.txt

#// Move file to a directory that's already in PATH
#sudo mv ~/Downloads/chromedriver /usr/local/bin

#// Make file executable
#sudo chmod +x /usr/local/bin/chromedriver