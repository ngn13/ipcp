# `ipcp` - Yet another one of my useless projects
While solving CTF challenges, I always need my IP address
for stuff like reverse shells. And everytime I need it,
I have to run `ifconfig <whatever-interface>` or `ip a`
and move my cursor to copy the IP... you know lots of
effort, some I wrote a simple python script that copies
your specified interface's IP address.

yes im that lazy :P

### Install
```
pip install -U https://github.com/ngn13/ipcp/archive/refs/heads/main.zip
```

### Usage
```
ipcp <interface>
```
