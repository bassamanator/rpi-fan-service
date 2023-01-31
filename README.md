Step 1

```
sudo cp runfan.py /usr/local/bin/runfan.py
sudo chmod +x /usr/local/bin/runfan.py
```

Step 2

```
sudo cp runfan.service /lib/systemd/system/runfan.service
sudo chmod 644 /lib/systemd/system/runfan.service
```

Step 3

```
sudo systemctl daemon-reload
sudo systemctl enable runfan.service
sudo systemctl start runfan.service
```
