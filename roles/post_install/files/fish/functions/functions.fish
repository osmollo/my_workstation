function mkvenv --description="create python virtual environment"
  set python_virtual_environment $argv[1]
  set python_virtual_environment_path {{ ansible_user_dir }}/.virtualenvs/$python_virtual_environment
  mkdir -p $python_virtual_environment_path
  mkvirtualenv -p /usr/bin/python3 -a $python_virtual_environment_path $python_virtual_environment
end

{% raw %}
function docker_ip --description="get docker container IPs"
  for CONTAINER in $(docker ps --format "{{.Names}}")
    echo "$(docker inspect -f "{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}} --> $CONTAINER" $CONTAINER)"
  end
end
{% endraw %}

function bind_bang
    switch (commandline -t)[-1]
        case "!"
            commandline -t -- $history[1]
            commandline -f repaint
        case "*"
            commandline -i !
    end
end

function bind_dollar
    switch (commandline -t)[-1]
        case "!"
            commandline -f backward-delete-char history-token-search-backward
        case "*"
            commandline -i '$'
    end
end

function fish_user_key_bindings
    bind ! bind_bang
    bind '$' bind_dollar
end
