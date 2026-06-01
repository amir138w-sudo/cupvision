from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8835794310:AAFobUtDcsFclBbc68A-pEl0ld5IWVDBm1c"

users = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    if user_id not in users:
        users[user_id] = {"points": 0, "predictions": []}

    keyboard = [
        [InlineKeyboardButton("⚽ ثبت پیش‌بینی", callback_data="predict")],
        [InlineKeyboardButton("👤 پروفایل", callback_data="profile")]
    ]

    await update.message.reply_text(
        "سلام اسد رفیق 😎⚽\nبه CupVision خوش اومدی!",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id
    await query.answer()

    if query.data == "profile":
        data = users.get(user_id, {"points": 0, "predictions": []})
        await query.message.reply_text(
            f"👤 پروفایل\n🏆 امتیاز: {data['points']}\n⚽ پیش‌بینی‌ها: {len(data['predictions'])}"
        )

    if query.data == "predict":
        users[user_id]["predictions"].append("match")
        await query.message.reply_text("⚽ پیش‌بینی ثبت شد!")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

app.run_polling()
