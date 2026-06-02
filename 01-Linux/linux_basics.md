# Linux Basics for DevOps

This file is a practical Linux checklist for DevOps work. If you can use these commands comfortably, you’ll be ready for servers, containers, CI/CD runners, and most cloud VMs.

## 1. Navigation and Filesystem Basics

Know where you are, what exists, and how to move around quickly.

- `pwd` to print the current directory.
- `ls -lah` to list files with human-readable sizes and hidden files.
- `cd`, `cd ..`, and `cd -` to move around efficiently.
- `tree` to visualize directory structure.
- `find` to locate files by name, type, size, or time.
- `which`, `whereis`, and `type` to see where commands come from.

```bash
pwd
ls -lah /var/log
find /etc -name "*.conf"
which python3
```

## 2. Viewing and Managing Files

You should be fluent with reading, copying, moving, and deleting files safely.

- `cat`, `less`, `head`, and `tail` for reading files.
- `cp`, `mv`, `rm`, `mkdir`, and `touch` for file operations.
- `ln -s` for symbolic links.
- `file` to identify what a file actually is.
- `stat` to inspect file metadata.

```bash
tail -f /var/log/syslog
cp app.conf app.conf.bak
ln -s /etc/nginx/sites-available/app.conf /etc/nginx/sites-enabled/app.conf
```

## 3. Permissions, Ownership, and sudo

This is one of the most important Linux topics in DevOps.

- Understand `rwx` for user, group, and others.
- Use `chmod` to change permissions.
- Use `chown` and `chgrp` to change ownership.
- Learn `umask` because it controls default permissions.
- Use `sudo` carefully and `visudo` when editing sudo rules.
- Check group membership with `id` and `groups`.

```bash
chmod 640 config.yaml
chown root:nginx /var/www/html/index.html
id
umask
```

## 4. Processes, Jobs, and System Resources

Servers fail, processes hang, and you need to know what is using CPU, memory, or ports.

- `ps aux` to list processes.
- `top` or `htop` to watch resource usage.
- `jobs`, `bg`, and `fg` to manage shell jobs.
- `kill`, `killall`, and `pkill` to stop processes.
- `nice` and `renice` to adjust priority.
- `lsof` and `fuser` to discover what owns a file or port.

```bash
ps aux | grep nginx
top
lsof -i :8080
pkill -f my-app
```

## 5. Package Management

DevOps work often means installing, updating, or auditing packages on Linux hosts.

- Debian/Ubuntu: `apt`, `dpkg`.
- RHEL/CentOS/Fedora: `dnf`, `yum`, `rpm`.
- SUSE/openSUSE: `zypper`.
- Always know how to update package lists and verify installed versions.

```bash
sudo apt update
sudo apt install nginx
rpm -qa | grep nginx
dpkg -l | grep nginx
```

## 6. Services and systemd

Most modern Linux systems use `systemd`.

- `systemctl status` to inspect a service.
- `systemctl start`, `stop`, `restart`, and `reload` to manage it.
- `systemctl enable` and `disable` to control startup at boot.
- `journalctl` to read service logs.

```bash
sudo systemctl status nginx
sudo systemctl restart docker
journalctl -u nginx -f
```

## 7. Logs and Troubleshooting

Logs are where the truth lives.

- Check `/var/log` for application and system logs.
- Use `journalctl -xe` for recent systemd errors.
- Use `dmesg` for kernel and boot messages.
- Search logs with `grep`, `awk`, and `sed`.

```bash
grep -i error /var/log/syslog
journalctl -p err -b
dmesg | tail -n 20
```

## 8. Networking Essentials

You do not need to be a network engineer, but you do need to debug connectivity issues.

- `ip addr` to view interfaces.
- `ip route` to inspect routing.
- `ss -tulpn` to see listening ports and sockets.
- `ping`, `traceroute`, `curl`, and `wget` for basic checks.
- `dig`, `nslookup`, and `host` for DNS debugging.
- `nc` and `tcpdump` for deeper troubleshooting.

```bash
ip addr
ip route
ss -tulpn
curl -I https://example.com
dig google.com
```

## 9. Storage, Disks, and Memory

Disk and memory issues are common in real environments.

- `df -h` to check filesystem usage.
- `du -sh` to find large directories.
- `lsblk` and `blkid` to inspect disks and partitions.
- `mount` and `umount` to manage filesystems.
- `free -h` to inspect memory and swap.

```bash
df -h
du -sh /var/log/*
lsblk
free -h
```

## 10. Users, Groups, and Access

Servers are shared systems, so access control matters.

- `useradd`, `usermod`, and `userdel` for account management.
- `passwd` to set passwords.
- `su -` and `sudo` for switching privilege levels.
- `id`, `whoami`, and `groups` to verify identity.

```bash
whoami
id devopsuser
sudo usermod -aG docker devopsuser
```

## 11. Shell Basics for Automation

Bash is everywhere in DevOps.

- Variables, quoting, and command substitution.
- Exit codes with `$?`.
- Pipes `|` and redirection `>`, `>>`, `2>`, `2>&1`.
- `grep`, `sed`, `awk`, and `xargs` for text processing.
- Loops, conditionals, and functions for scripts.
- `cron` and systemd timers for scheduled tasks.

```bash
name="devops"
echo "Hello $name"
if [ -f /etc/passwd ]; then echo "exists"; fi
```

## 12. Security Fundamentals

Security is not optional.

- Use SSH keys instead of passwords when possible.
- Know where `authorized_keys`, `sshd_config`, and `sudoers` live.
- Keep secrets out of shell history and git repos.
- Use firewalls like `ufw` or `firewalld`.
- Review open ports regularly.

```bash
ssh-keygen -t ed25519
sudo ufw status
sudo ss -tulpn
```

## 13. DevOps Troubleshooting Checklist

When something breaks, check in this order:

1. Is the service running?
2. Are logs showing the error?
3. Is the port listening?
4. Is DNS resolving?
5. Is disk full or memory exhausted?
6. Are permissions blocking access?
7. Did a recent change break the environment?

## 14. Commands Worth Memorizing

These are the ones you will actually use often.

- `ls`, `cd`, `pwd`, `find`
- `cat`, `less`, `tail`, `grep`
- `chmod`, `chown`, `sudo`
- `ps`, `top`, `kill`, `lsof`
- `systemctl`, `journalctl`
- `curl`, `ping`, `ss`, `dig`
- `df`, `du`, `free`, `lsblk`

## 15. What to Be Comfortable Doing

If you can do these without looking up every step, you are in good shape for DevOps work:

- SSH into a Linux server and inspect logs.
- Fix permissions on a file or directory.
- Find which process is using a port and restart it.
- Install or update a package.
- Read a service failure from `journalctl`.
- Trace a network issue with `curl`, `dig`, and `ss`.
- Write a small Bash script that automates a repetitive task.
