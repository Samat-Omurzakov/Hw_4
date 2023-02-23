from aiogram.utils import executor
import logging
from config import dp
from handler import client, callback, extra, adminka, fsm_anketa

fsm_anketa.reg_hand_anketa(dp)
adminka.reg_ban(dp)
client.reg_client(dp)
callback.reg_hand_callback(dp)
extra.reg_hand_extra(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
