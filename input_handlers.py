import tcod.event
from typing import Optional
from actions import Action, EscapeAction, MovementAction


class EventHandler(tcod.event.EventDispatch[Action]):
    def ev_quit(self, event: tcod.event.Quit):
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym

        if key == tcod.event.K_UP or key == tcod.event.K_KP_8:
            action = MovementAction(dx=0, dy=-1)
        elif key == tcod.event.K_DOWN or key == tcod.event.K_KP_2:
            action = MovementAction(dx=0, dy=1)
        elif key == tcod.event.K_LEFT or key == tcod.event.K_KP_4:
            action = MovementAction(dx=-1, dy=0)
        elif key == tcod.event.K_RIGHT or key == tcod.event.K_KP_6:
            action = MovementAction(dx=1, dy=0)
        elif key == tcod.event.K_PERIOD or key == tcod.event.K_KP_5:
            action = MovementAction(dx=0, dy=0)

        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction()
        return action
