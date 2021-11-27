from transitions import Machine
import pickle


class State(object):
    def __init__(self, config):
        self.answers = [""] * len(config)
        self.state_dict = {}
        self.states_list = []
        self.transitions_list = []

        for i, step in enumerate(config):
            self.states_list.append(step.get("state"))
            choices = step.get("choices")
            if choices:
                for choice in choices:
                    self.transitions_list.append({
                        "trigger": choice.get("trigger"),
                        "source": step.get("state"),
                        "dest": choice.get("dest")
                    })
            self.state_dict[step.get("state")] = {
                "pk": i,
                "message_template": step.get("message_template"),
                "choices": step.get("choices")
            }
        self.initial = self.states_list[0]
        self.Machine = Machine(self, states=self.states_list,transitions=self.transitions_list,initial=self.initial)


def get_state_machine(config):
    # return State(config)
    if config:
        return pickle.dumps(State(config))
    else:
        return None

