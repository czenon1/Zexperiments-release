#! usr/bin/bash
echo "DNS Fixer for Ubuntu server 22.04 LTS - Will recreate /etc/resolv.conf"
echo "working"
echo " "
echo "OLD File =============================================================="
cat /etc/resolv.conf
echo " "
sudo cp /etc/resolv.conf /etc/resolv.conf.bak
echo "Backup is /etc/resolv.conf.bak"
sudo rm /etc/resolv.conf
sudo touch /etc/resolv.cof
sudo echo 'nameserver 1.1.1.1' >> /etc/resolv.conf
echo "NEW File =============================================================="
cat /etc/resolv.conf
echo " "
ping ecole2600.com -c 3
echo "Done !"
