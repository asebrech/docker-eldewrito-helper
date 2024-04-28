import yaml

def generate_docker_compose(num_instances):
    template = {
        "services": {},
    }

    for i in range(1, num_instances + 1):
        instance_name = f"eldewrito_server_{i}"
        starting_port = 11774 + (i - 1) * 10
        template["services"][instance_name] = {
            "image": "eldewrito:image",
            "depends_on": ["_image_build"],
            "restart": "always",
            "volumes": [
                "./eldewrito:/game",
                "./scripts:/scripts",
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
                f"SERVER_HOST=Docker",
                f"RCON_PASSWORD=mypassword",
                f"GAME_PORT={starting_port}",
                f"PORT={starting_port + 1}",
                f"RCON_PORT={starting_port + 2}",
                f"SIGNAL_SERVER_PORT={starting_port + 3}",
                f"FILE_SERVER_PORT={starting_port + 4}",
                f"INSTANCE_ID={i}",
                f"SERVER_NAME=[Dockerized] HaloOnline Server #{i}",
                f"SERVER_MESSAGE=Welcome to my server!",
                f"CHAT_LOG=logs/chat_server_{i}.log",
                f"VOTING_SYSTEM_TYPE=1",
                f"VOTING_TIME=15",
                f"VOTING_JSON_PATH=/config/voting{i}.json"
            ]
        }

    template["services"]["_image_build"] = {
        "image": "eldewrito:image",
        "command": ["echo", "build completed"],
        "build": {
            "context": ".",
            "dockerfile": "Dockerfile"
        }
    }

    return yaml.dump(template)

if __name__ == "__main__":
    num_instances = 1  # Change this to the desired number of instances
    docker_compose_content = generate_docker_compose(num_instances)
    with open("docker-compose.yml", "w") as f:
        f.write(docker_compose_content)