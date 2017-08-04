# JANUS
analysis of river ice movement (polar hackathon '17) -- building a scalable pipeline that computes the velocity displacement of images collected by planet.org API

## Configuration of Jupyter Notebook with GCP

* Create VM instance: Ubuntu, allow http traffic
* On GCP console --> networking --> external IP: Change external IP address from ephemeral to static for VM instance
* From terminal : ```gcloud compute --project "<project-name>" ssh --zone "<your-zone>" "<instance-name>"```
* ```apt-get install bzip2```
* ```wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh```
* ```sudo bash Miniconda2-latest-Linux-x86_64.sh```
* create/source conda environment, conda install jupyter notebook 
* Connect VM with Jupyter via HTTP by first creating a firewall rule: 
    * GCP Console --> Networking --> Firewall rules 
    * Create filewall rule with settings: 
    
      Network
      default
      
      Priority
      1000
      
      Direction
      Ingress
      
      Action on match
      Allow
      
      Targets
      Target tags
      https-server
      
      Source filters
      IP ranges
      0.0.0.0/0
      
      Protocols and ports
      tcp:8800
    
 * Initialize jupyter notebook in terminal: ```jupyter notebook --ip=0.0.0.0 --port=8800 --no-browser &```
 * Launch notebook from browser: ```http://<your-static-external-ip>:8800```
 * source(https://jeffdelaney.me/blog/running-jupyter-notebook-google-cloud-platform/) 

