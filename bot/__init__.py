from .handlers import register_handlers
from .scheduler import start_scheduler

def setup_bot(dp, bot):
    register_handlers(dp)
    start_scheduler(bot)