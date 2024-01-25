from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)
import pytz

def get_hours(timezone):
    match timezone:
        case 'America - PST':
            return 'US/Pacific'
        case 'Brazil - BRT':
            return 'America/Sao_Paulo'
        case 'Europe - GMT':
            return 'Etc/Greenwich'

# print(pytz.all_timezones)

