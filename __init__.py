from mycroft import MycroftSkill, intent_handler


class AiPbxAppointermentForNailSalon(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler('salon.nail.for.appointerment.pbx.ai.intent')
    def handle_salon_nail_for_appointerment_pbx_ai(self, message):
        self.speak_dialog('salon.nail.for.appointerment.pbx.ai')


def create_skill():
    return AiPbxAppointermentForNailSalon()

