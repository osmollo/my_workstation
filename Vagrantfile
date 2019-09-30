Vagrant.configure("2") do |config|

  config.vm.provider 'virtualbox' do |v|
    v.memory = 4096
    v.cpus = 2
  end

  config.vm.define 'ubuntu' do |node|
    node.vm.box = "ubuntu/bionic64"
    node.vm.network :private_network, ip: "192.168.56.200"
    #node.vm.hostname = 'ubuntu'
    node.vm.provision "ansible" do |ansible|
      ansible.inventory_path = "inventory/ubuntu"
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
    node.vm.box = "fedora/30-cloud-base"
    node.vm.network :private_network, ip: "192.168.56.100"
    #node.vm.hostname = 'fedora'
    node.vm.provision "ansible" do |ansible|
      ansible.inventory_path = "inventory/fedora"
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
