# Interest API

This is a simple API that scrapes Bank Of Israel's site for the current national 'prime' interest rate.
On the app's launch it will scrape the data into a file.
The file will have the next date of decision. (updating the interest)
Every time a request is made, the API will first check to see if the current date is past (or equals to) the "Next Update Date" if so, the backend will update the date file with new data, otherwise the API will return the current interest rate and the next update date.

## Installaion 

### Build Your Own Container
```code
git clone https://github.com/Inframous/interestApiBoi.git
sudo docker build -t "interestapi" .
sudo docker run -d -p 80:80 --restart always --name interestapi interestapi
```
Point your browser at `http://<api_url>/api/interest/` to receive the latest information.

### Docker Hub (x86 only)
Pull the image from Docker.io and run it.
```code
sudo docker pull inframous/interestapi:latest
sudo docker run -d -p 80:80 --restart always --name interestapi interestapi
```
Point your browser at `http://<api_url>/api/interest/` to receive the latest information.
