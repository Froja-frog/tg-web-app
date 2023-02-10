from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from tg_bot.keyboards.for_start import get_start_keyboard


router = Router()


@router.message(Command(commands=['start']))
async def cmd_start(message: Message) -> None:
    await message.answer(f"Здравствуйте, **{message.from_user.full_name}\!**", reply_markup=get_start_keyboard())
