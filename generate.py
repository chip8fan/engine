import shutil
import os
file = open("tokens.txt")
lines = [line.strip().split(",") for line in file]
file.close()
config = open("config.yml")
config_lines = [line.rstrip() for line in config]
config.close()
for bot in lines:
    if os.path.isdir(bot[1]) == False:
        shutil.copytree("lichess-bot", bot[1])
        with open(f"{bot[1]}/config.yml", "w") as config:
            for line in config_lines:
                if "token:" in line:
                    config.write(line.replace('""', f'"{bot[0]}"')+"\n")
                elif "dir:" in line:
                    config.write(line.replace('""', f'"{input(f"Directory for {bot[1]}: ")}"')+"\n")
                elif "name:" in line:
                    config.write(line.replace('""', f'"{input(f"Binary name for {bot[1]}: ")}"')+"\n")
                else:
                    config.write(line+"\n")