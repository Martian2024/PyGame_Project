import pygame
import pygame_gui
from pygame_gui.core import ObjectID
from Units_list import lst


class Close_Button(pygame_gui.elements.UIButton):
    def __init__(self, x, y, container, manager, wind):
        super().__init__(relative_rect=pygame.Rect(x, y, 20, 20), text='X', container=container, manager=manager,
                         object_id=ObjectID(class_id='@close_button'))
        self.container = container
        self.manager = manager
        self.wind = wind

    def close(self):
        self.wind.hide()


class Resourses_window(pygame_gui.elements.UIPanel):
    def __init__(self, x, y, manager):
        super().__init__(relative_rect=pygame.Rect(x, y, 800, 400), manager=manager,
                         object_id=ObjectID(object_id='#opening_window'), starting_layer_height=0, visible=0)
        self.container = self.get_container()
        self.visible = False
        self.close_button = Close_Button(775, 0, self.container, manager, self)
        self.labels = []
        for i in [(50, 60), (50, 112), (50, 164), (50, 216), (50, 268), (50, 330), (500, 60), (500, 112), (500, 164),
                  (500, 216), (500, 268)]:
            text = pygame_gui.elements.UILabel(relative_rect=pygame.Rect(*i, 100, 20), text='',
                                               manager=manager, container=self.container,
                                               object_id=ObjectID(class_id='@resourses_label'))
            text.set_text_alpha(100)
            self.labels.append(text)

    def show_telem(self, ship):
        for i in zip(self.labels, ship.resourses.keys()):
            i[0].set_text(i[1] + ': {}'.format(ship.resourses[i[1]]))
        self.show()


class Building_window(pygame_gui.elements.UIPanel):
    def __init__(self, x, y, manager):
        super().__init__(relative_rect=pygame.Rect(x, y, 800, 400), manager=manager,
                         object_id=ObjectID(object_id='#building_window'), starting_layer_height=0, visible=0)
        self.container = self.get_container()
        self.visible = False
        self.items = []
        self.manager = manager
        for i in zip([(60, 60), (50, 180), (50, 300), (180, 60), (180, 180), (180, 300), (300, 60), ],
                     ["#battery_button", "#armor_button", "#lab_button", "#powerplant_button", "#farm_button",
                      "#laser_button", "#engine_button"]):
            button = Building_Button(*i[0], self.container, self.manager, i[1])
            self.items.append(button)


class Building_Button(pygame_gui.elements.UIButton):
    def __init__(self, x, y, container, manager, object_id):
        super().__init__(relative_rect=pygame.Rect(x, y, 70, 70), text='', container=container, manager=manager,
                         object_id=ObjectID(object_id=object_id))


class Delete_Button(pygame_gui.elements.UIButton):
    def __init__(self, x, y, container, manager):
        super().__init__(relative_rect=pygame.Rect(x, y, 30, 30), text='', container=container, manager=manager,
                         object_id=ObjectID(object_id='delete_button'))
