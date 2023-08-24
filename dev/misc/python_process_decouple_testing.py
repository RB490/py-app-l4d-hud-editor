# Use subprocess.Popen with DETACHED_PROCESS flag
# result = subprocess.Popen(steam_command, shell=True)
# result = subprocess.Popen([steam_command], shell=True)
# result = subprocess.run(steam_command, shell=True, check=True)
# result = subprocess.run([steam_command], shell=True, check=True)
# result = subprocess.Popen(steam_command, shell=False, creationflags=subprocess.DETACHED_PROCESS)
# result = subprocess.Popen([steam_command], shell=False, creationflags=subprocess.DETACHED_PROCESS)
# result = subprocess.Popen(["start", "/B", steam_command], shell=True)
# result = subprocess.Popen(["cmd", "/c", steam_command])
# os.system(steam_command)

# detached_process_flag = 0x00000008  # Constant for creating a detached process
# subprocess.Popen(
#     steam_command,
#     shell=True,
#     creationflags=detached_process_flag,
#     start_new_session=True,  # Required for some platforms
# )

# ahk_script = f"Run cmd.exe /c del {steam_command}"
# steam_command_cmd = f'{steam_exe} {steam_args} {" ".join(game_args)}'
# steam_command_cmd_quoted = f'"{steam_exe} {steam_args} {" ".join(game_args)}"'
# steam_command_quoted = f'"{steam_command}"'
# pristine_command = f'{steam_exe}'
# print(f"steam command cmd: {steam_command_cmd}")
# print(f"steam command cmd quoted: {steam_command_cmd_quoted}")
# print(f"steam command: {steam_command}")
# print(f"steam command quoted: {steam_command_quoted}")
# ahk_script = f"Run cmd.exe /k del {steam_command_cmd_quoted}"
# ahk_script = "run cmd /k E:\games\steam\steam.exe -applaunch 550 -novid -console"
# ahk_script = f"run cmd /k {pristine_command} {steam_args}"
# ahk_script = f"run {pristine_command} {steam_args}"
# print(ahk_script)
# ahk.run_script(ahk_script, blocking=False)

# print(self.game.steam.get_exe_path())
# subprocess.Popen(["rm", "-r", self.game.steam.get_exe_path()])

# subprocess.Popen(['python', os.path.realpath(__file__), '0'], close_fds=True)
# print(f'file =================================== {os.path.realpath(__file__)}')
# subprocess.Popen(["python", self.game.steam.get_exe_path(), "0"], close_fds=True)

# DETACHED_PROCESS = 0x00000008

# pid = subprocess.Popen([sys.executable, "longtask.py"], creationflags=DETACHED_PROCESS).pid

# import subprocess

# subprocess.Popen(["notepad.exe", "test.txt"])

# command = "longtask.py &"
# subprocess.Popen(command, shell=True)

# command = "start /B notepad.exe"
# subprocess.Popen(command, shell=True)

# command = f"start /B {self.game.steam.get_exe_path()}"
# subprocess.Popen(command, shell=True)
