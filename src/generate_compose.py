import yaml

from src.utils.utils import name_to_suffix

def generate_docker_compose(config):
    template = {
        "services": {},
    }

    total_instances = 0
    for server in config['server']:
        total_instances += int(server['server_intance'])
    starting_port = 11764

    for server in config['server']:
        num_instances = int(server['server_intance'])
        instance_suffix = name_to_suffix(server['selected_server'])
        for i in range(1, num_instances + 1):
            total_instances += 1
            instance_name = f"{instance_suffix}_{i}"
            starting_port += 10
            template["services"][instance_name] = {
                "image": "eldewrito:image",
                "depends_on": ["_image_build"],
                "restart": "always",
                "volumes": [
                    "./eldewrito:/game",
                    "./docker-eldewrito/scripts:/scripts",
                    f"./eldewrito/data:/config"
                ],
                "working_dir": "/game",
                "command": ["sh", "../scripts/start.sh"],
                "ports": [
                    f"{starting_port}:11774/udp",
                    f"{starting_port + 1}:11775/tcp",
                    f"{starting_port + 2}:11776/tcp",
                    f"{starting_port + 3}:11777/tcp",
                    f"{starting_port + 4}:11778"
                ],
                "environment": [
                    f"ED_CFG_VERSION=0.7.0",
                    f"SERVER_HOST=\"{config['host_name']}\"",
                    f"RCON_PASSWORD=\"{config['rcon_password']}\"",
                    f"GAME_PORT={starting_port}",
                    f"PORT={starting_port + 1}",
                    f"RCON_PORT={starting_port + 2}",
                    f"SIGNAL_SERVER_PORT={starting_port + 3}",
                    f"FILE_SERVER_PORT={starting_port + 4}",
                    f"INSTANCE_ID={instance_name}",
                    f"SERVER_NAME=\"{server['server_name']} | {i}\"",
                    f"SERVER_MESSAGE=\"{server['server_message']}\"",
                    f"CHAT_LOG=logs/chat_server_{instance_name}.log",
                    f"VOTING_JSON_PATH=/config/voting/voting_{instance_suffix}.json",
                    f"VOTING_SYSTEM_TYPE=1",
                    f"VOTING_TIME=15"
                ]
            }

    template["services"]["_image_build"] = {
        "image": "eldewrito:image",
        "command": ["echo", "build completed"],
        "build": {
            "context": "./docker-eldewrito",
            "dockerfile": "Dockerfile"
        }
    }

    return yaml.dump(template)