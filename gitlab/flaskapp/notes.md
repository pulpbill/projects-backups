Python app:
- python3 -m venv env #setting up a virtual env
- source env/bin/activate #activating the env
- pip install flask #installing flask
- vim app.py #writting the flask app (you must have flask install as shown on the previous step)
- python app.py #testing the app (go to localhost:5000)
- pip freeze > requirements.txt #Do this after succesfully running the app.py

Dockerfile:
- vim Dockerfile
- #Define the basics layers (FROM - RUN)
- #Define the requirements (COPY)
- #Define the working dir (WORKDIR)
- #Install requirements (RUN)
- #Copy files to working dir (COPY)
- #Setup the entrypoint (ENTRYPOINT)
- #Setup the command (CMD)
- docker build -t flaskapp2020 . #build the app (image) (based on the Dockerfile and set the image name (flaskapp2020))
- docker images (check for your just created "flaskapp2020")

Dockerhub:
- #Create a public repository
- #Copy the namespace rancormtg/flaskapp2020
- docker login --username=rancormtg #log into dockerhub
- docker tag flaskapp rancormtg/flaskapp2020:latest #tag your image
- docker image push rancormtg/flaskapp2020:latest #push your tagged image

Gitlab:
- #Create a public Project
- #Setup your git context and upload your files
- git config --global user.name <youruser>
- git config --global user.email <youremail>
- git init
- git remote add origin git@gitlab.com:<youruser>/flaskapp.git
- git add .
- git commit -m "Initial commit"
- git push -u origin master 

Gitlab Runner:
- curl -LJO -i https://gitlab-runner-downloads.s3.amazonaws.com/latest/deb/gitlab-runner_amd64.deb
- sudo dpkg -i gitlab-runner_amd64.deb
- sudo gitlab-runner start
- sudo gitlab-runner run
- sudo gitlab-runner register
- #In order to get the token and configure the Runner, go to: https://gitlab.com/<youruser>/flaskapp/-/settings/ci_cd
    - coordinator: https://gitlab.com/
    - token: <yourprojecttoken>
    - description: <whateveryoutwant>
    - tag: dockerflasktest
    - executor: shell
- sudo gitlab-runner verify 

ECS:
- #Pick custom: configure
- Container name: flaskapp
- Image: rancormtg/flaskapp2020 #(the one you previously pushed to dockerhub)
- Port Mappings: 5000 #Default for flask app
- Load Balancer Type: ALB
- Clustername: flaskcluster
- Create

Gitlab CI/CD:
- vim .gitlab-ci.yml
- #Write your build jobs and stages
- tags: dockerflasktest #The same you used for the runner
- #Write your script (the one that will execute your builds, test, etc.)
- #Will build the image (docker build)
- #Will push the image to dockerhub (docker image push)
- #Will update ECS service/cluster
    - force will update our existing ECS cluster
    - The cluster must be setup beforhand, this will update it

Validate:
- #Go to AWS console and at LB section, look for your DNS name (endpoint) and access it on port :5000

Test your CI/CD:
- #For example: Change the return msg at app.py file, to something like this (just adds "V2"):
    - return "<h1>Demo Flask App V2</h1>"
- #Remember to leave your gitlab-runner running in order to test this
- #Push your changes
- #Validate at gitlab on CI/CD -> Pipelines and Jobs section, you will see the runner (that's running on your PC executing the scripts)
- #Repeat the "Validate" step and refresh the DNS endpoint, you should see "V2" now

Pushing image from gitlab to dockerhub:
-docker info | grep Registry #Checks your registry
-#Add secrets to gitlab (your hub data)

CI_REGISTRY_USER=gableroux
CI_REGISTRY_PASSWORD=********
CI_REGISTRY=docker.io
CI_REGISTRY_IMAGE=index.docker.io/gableroux/unity3d

Also, add your AWS stuff:
AWS_ACCESS_KEY_ID
AWS_DEFAULT_REGION
AWS_SECRET_ACCESS_KEY