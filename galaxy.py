from utils import *


class Galaxy():

    def __init__(self, rect):
        self.rect = rect
        self.entities = {}
        self.entity_id = 0

    def add_entity(self, entity):
        self.entities[self.entity_id] = entity
        entity.id = self.entity_id
        self.entity_id += 1

    def remove_entity(self, entity):
        del self.entities[entity.id]

    def get_entity_by_name(self, entity_name):
        for entity in self.entities.values():
            if entity.name == entity_name:
                return entity
        return None

    def get_entities_by_name(self, entity_name):
        entities = []
        for entity in self.entities.values():
            if entity.name == entity_name:
                entities.append(entity)
        return entities

    def update(self, time_passed, event_list):
        for entity in list(self.entities.values()):
            entity.update(time_passed, event_list)

    def render(self, surface):
        surface.fill(BLACK)
        for entity in self.entities.values():
            entity.render(surface)

    def cleanup(self):
        # remove all dead entities
        for entity in list(self.entities.values()):
            if entity.dead == True:
                self.remove_entity(entity)
