Vagrant.configure("2") do |config|

  config.vm.provider 'virtualbox' do |v|
    v.memory = 2048
    v.cpus = 2
  end

  config.vm.define 'ubuntu' do |node|
    node.vm.box = "envimation/ubuntu-xenial"
    node.vm.network :private_network, ip: "192.168.56.20"
    node.vm.hostname = 'ubuntu'
    config.vm.provision "shell" do |s|
      ssh_pub_key = File.readlines("/home/ohermosa/.ssh/id_rsa.pub").first.strip
      s.inline = <<-SHELL
        echo #{ssh_pub_key} >> /home/vagrant/.ssh/authorized_keys
      SHELL
    end
  end

  config.vm.define 'fedora' do |node|
    node.vm.box = "fedora/30-cloud-base"
    node.vm.network :private_network, ip: "192.168.56.10"
    node.vm.hostname = 'fedora'
    config.vm.provision "shell" do |s|
      ssh_pub_key = File.readlines("/home/ohermosa/.ssh/id_rsa.pub").first.strip
      s.inline = <<-SHELL
        echo #{ssh_pub_key} >> /home/vagrant/.ssh/authorized_keys
      SHELL
    end
  end
end
