Vagrant.configure("2") do |config|

  config.vm.provider 'virtualbox' do |v|
    v.memory = 4096
    v.cpus = 2
    v.customize ["modifyvm", :id, "--usb", "on"]
    v.customize ["modifyvm", :id, "--usbehci", "off"]
  end

  config.vm.define 'mint' do |node|
    node.vm.box = "boxcycler/linuxmint-19-cinnamon-64bit-v2-release"
    node.vm.network :private_network, ip: "192.168.56.200"
    node.vm.provision "ansible" do |ansible|
      ansible.inventory_path = "ansible_hosts"
      ansible.playbook = "vagrant/install.yml"
    end
    config.vm.provision "shell" do |s|
      ssh_pub_key = File.readlines("#{Dir.home}/.ssh/id_rsa.pub").first.strip
      s.inline = <<-SHELL
        echo #{ssh_pub_key} >> /home/vagrant/.ssh/authorized_keys
      SHELL
    end
  end

  config.vm.define 'ubuntu' do |node|
    node.vm.box = "ubuntu/bionic64"
    node.vm.network :private_network, ip: "192.168.56.201"
    #node.vm.hostname = 'ubuntu'
    node.vm.provision "ansible" do |ansible|
      ansible.inventory_path = "ansible_hosts"
      ansible.playbook = "vagrant/install.yml"
    end
    config.vm.provision "shell" do |s|
      ssh_pub_key = File.readlines("#{Dir.home}/.ssh/id_rsa.pub").first.strip
      s.inline = <<-SHELL
        echo #{ssh_pub_key} >> /home/vagrant/.ssh/authorized_keys
      SHELL
    end
  end

  config.vm.define 'fedora' do |node|
    node.vm.box = "bento/fedora-30"
    node.vm.network :private_network, ip: "192.168.56.202"
    #node.vm.hostname = 'fedora'
    node.vm.provision "ansible" do |ansible|
      ansible.inventory_path = "ansible_hosts"
      ansible.playbook = "vagrant/install.yml"
    end
    config.vm.provision "shell" do |s|
      ssh_pub_key = File.readlines("#{Dir.home}/.ssh/id_rsa.pub").first.strip
      s.inline = <<-SHELL
        echo #{ssh_pub_key} >> /home/vagrant/.ssh/authorized_keys
      SHELL
    end
  end
end
