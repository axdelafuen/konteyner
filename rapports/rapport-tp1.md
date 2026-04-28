# TP1

### VirtualBox & SSH

**1. to 3.** After creating the VM, add a "Host-Only" network adapter to bypass NAT isolation and verified connectivity.

`ping <VM_PRIVATE_IP>`

**4.** Generate an SSH key pair (public/private) on host machine.

`ssh-keygen -t rsa -b 4096`

**5.** Copy public key to the VM and modify `/etc/ssh/sshd_config` to allow key-based root login.

`ssh-copy-id root@<VM_PRIVATE_IP>`

**6.:** Validate the SSH connection using private key, confirming that password authentication was successfully disabled.
  
`ssh -i ~/.ssh/id_rsa root@<VM_PRIVATE_IP>`

### Ansible

**1.** Create an inventory file (`inventory.ini`) containing the VM's IP and verify it was correctly parsed by Ansible.

`ansible-inventory -i inventory.ini --list`

**2.** Test the communication between host and the VM using an _ad hoc_ ping command.

`ansible all -i inventory.ini -m ping`

**3. to 8.:** Write a `playbook.yml` file containing all the requested tasks (creating a file, installing Apache, copying `index.html`, configuring a restart _handler_, and verifying the site via _curl_) and executed it.

`ansible-playbook -i inventory.ini playbook.yml`
