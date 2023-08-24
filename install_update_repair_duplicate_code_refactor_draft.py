def common_installation_logic(self, action, resume_state, action_description):
    print(f"{action_description}...")

    current_state = self.game.dir.id.get_installation_state(DirectoryMode.DEVELOPER)

    # check installation state
    if current_state is not InstallationState.COMPLETED:
        print("Not installed!")
        return False

    # get user directory
    if not self.game.installed(DirectoryMode.USER):
        try:
            self.game.dir.id.set_path(DirectoryMode.USER)
        except Exception as err_info:
            show_message(f"{err_info}", "error", "Could not get user directory!")
            return False

    # confirm start
    if not prompt_start(self.game, action, f"This will {action_description.lower()}"):
        return False

    # close game
    self.game.close()

    # activate developer mode
    self.game.dir.set(DirectoryMode.DEVELOPER)

    # enable paks
    self.__enable_paks()

    # set resume state
    self.game.dir.id.set_installation_state(DirectoryMode.DEVELOPER, resume_state)

    # perform installation steps
    try:
        self.__process_installation_steps(resume_state)
        print(f"Finished {action_description.lower()}ing!")
        return True
    except Exception as err_info:
        show_message(f"{action_description} error: {err_info}", "error")
        return False


def update(self):
    return self.common_installation_logic("update", InstallationState.VERIFYING_GAME, "Updating")


def repair(self):
    return self.common_installation_logic("repair", InstallationState.EXTRACTING_PAKS, "Repairing")


def install(self):
    return self.common_installation_logic("install", current_state, "Installing")
