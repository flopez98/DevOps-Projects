Ansible Playbook - README

This Ansible playbook is designed to automate the installation and configuration of packages for different server types. The playbook is divided into four sections based on the server types: all, web_servers, db_servers, and file_servers.
Requirements

    Ansible 2.0 or later
    Target servers running CentOS or Ubuntu operating systems

Usage

To use this playbook, follow these steps:

    Update the inventory file with the IP addresses or hostnames of your target servers.
    Modify the pre_tasks section to fit your needs.
    Modify the tasks section for each server type to install the packages you require.
    Run the playbook with the following command: ansible-playbook -i inventory playbook.yml

The playbook will run on all servers listed in the inventory file, so make sure to add or remove servers as needed.

Note: If you are using a user other than root to login into the machines, please modify the remote_user value in the ansible.cfg file to match your username. If you are using root, please remove remote_user from the ansible.cfg file.
Section 1: all

This section contains pre-tasks that will be executed on all servers.

    install updates (CentOS): This task uses the dnf package manager to update the system packages on CentOS servers.
    install updates (Ubuntu): This task uses the apt package manager to update the system packages on Ubuntu servers.

Section 2: web_servers

This section contains tasks that will be executed on servers assigned to the web_servers group in the inventory file.

    install apache2 and php packages for Ubuntu: This task installs the Apache2 web server and PHP packages using the apt package manager on Ubuntu servers.
    add php support for apache and php for CentOS: This task installs the Apache web server and PHP packages using the dnf package manager on CentOS servers.

Section 3: db_servers

This section contains tasks that will be executed on servers assigned to the db_servers group in the inventory file.

    install mariadb package (CentOS): This task installs the MariaDB database server using the dnf package manager on CentOS servers.
    install mariadb package (Ubuntu): This task installs the MariaDB database server using the apt package manager on Ubuntu servers.

Section 4: file_servers

This section contains tasks that will be executed on servers assigned to the file_servers group in the inventory file.

    install samba package: This task installs the Samba file sharing service using the package module on all servers.
