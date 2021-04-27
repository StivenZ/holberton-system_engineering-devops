# Web stack debugging #2
---
In this series of DevOps projects we are meant to learn and debug some servers and containers.

### Tasks
* 0-iamsomeoneelse: script to run the command *whoami* under the user passed as an argument.
* * usage: `$ ./0-iamsomeoneelse [username]`

* 1-run_nginx_as_nginx: to prevent attackers to use root priviledges in a hacking situation, this script will fix the container so that Nginx will be running as the *nginx* user and not *root*. nginx must be listening on all active IPs on port 8080.
