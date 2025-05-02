from aiogram.dispatcher.filters.state import State,StatesGroup

class QRStates(StatesGroup):
    waiting_for_text = State()

class Textabout(StatesGroup):
    text1=State()

class Reklmayoz(StatesGroup):
    reklamayoz= State()