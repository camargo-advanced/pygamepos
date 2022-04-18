class Entity():
    def __init__(self, galaxy, name):
        self.galaxy = galaxy
        self.name = name
        self.dead = False
        self.__object_just_created = True
        self.visible = False

    def kill(self):
        self.dead = True

    def cleanup(self):
        for entity in list(self.entities):
            if entity.dead == True:
                self.remove_entity(entity)

    def update(self, time_passed, event_list):
        if self.__object_just_created:
            self.visible = True
            self.__object_just_created = False

    def render(self, surface):
        pass
