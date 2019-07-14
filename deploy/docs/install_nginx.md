  ```markdown
sudo apt update
sudo apt install nginx -y
```

# config site
```markdown
cd /etc/nginx/sites-enabled
touch .conf

sudo systemctl restart nginx
```