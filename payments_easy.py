import asyncio, logging
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types.message import ContentType
from config import TOKEN, PAYMENT_TOKEN, TIME_MACHINE_IMAGE_URL
from messages import MESSAGES

loop = asyncio.get_event_loop()
bot = Bot(token=TOKEN, parse_mode=types.ParseMode.MARKDOWN)
dp = Dispatcher(bot, loop=loop)

PRICE = types.LabeledPrice(label="Настоящая машина времени", amount=4200000)


@dp.message_handler(commands=["terms"])
async def process_terms_command(message: types.Message):
    await message.reply(MESSAGES["terms"], reply=False)
    
    
@dp.message_handler(commands=["buy"])
async def process_buy_command(message: types.Message):
    if PAYMENT_TOKEN.split(":")[1] == "TEST":
        await bot.send_message(message.from_user.id, MESSAGES['pre_buy_demo_alert'])
        
        await bot.send_invoice(
            message.from_user.id, 
            title = MESSAGES["tm_title"],
            description = MESSAGES["tm_description"],
            provider_token=PAYMENT_TOKEN,
            currency = "rub",
            photo_url = TIME_MACHINE_IMAGE_URL,
            photo_height = 512, # photo_heigh, photo_width != 0/None. иначе изображения не будет
            photo_width = 512,
            photo_size = 512,
            is_flexible = False, # is_flexible = True, если конечная цена зависит от способа доставки
            prices = [PRICE], start_parameter = "time-machine-example", payload = "some-invoice-payload-for-our-internal-use")



@dp.pre_checkout_query_handler(lambda query: True)
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)
    
    
@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def process_successful_payment(message: types.Message):
    print("successful payment")
    pmnt = message.successful_payment.to_python()
    for key, value in pmnt:
        print(f"{key} = {value}")
    
    
    await bot.send_message(
        message.from_user.id,
        MESSAGES["successful_payment"].format(
            total_amount = message.successful_payment.total_amount // 100,
            currency = message.successful_payment.currency
        )
    )


executor.start_polling(dp, skip_updates=True)