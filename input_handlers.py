import tcod.event
from typing import Optional
from actions import Action, EscapeAction, MovementAction


class EventHandler(tcod.event.EventDispatch[Action]):
    def ev_quit(self, event: tcod.event.Quit):
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym

        if key == tcod.event.K_KP_1:
            action = MovementAction(dx=-1, dy=-1)
        elif key == tcod.event.K_KP_2 or key == tcod.event.K_DOWN:
            action = MovementAction(dx=0, dy=1)
        elif key == tcod.event.K_KP_3:
            action = MovementAction(dx=1, dy=-1)
        elif key == tcod.event.K_KP_4 or key == tcod.event.K_LEFT:
            action = MovementAction(dx=-1, dy=0)
        elif key == tcod.event.K_KP_5 or key == tcod.event.K_PERIOD:
            action = MovementAction(dx=0, dy=0)
        elif key == tcod.event.K_KP_6 or key == tcod.event.K_RIGHT:
            action = MovementAction(dx=1, dy=0)
        elif key == tcod.event.K_KP_7:
            action = MovementAction(dx=-1, dy=1)
        elif key == tcod.event.K_KP_8 or key == tcod.event.K_UP:
            action = MovementAction(dx=0, dy=-1)
        elif key == tcod.event.K_KP_9:
            action = MovementAction(dx=1, dy=1)

        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction()
        return action
