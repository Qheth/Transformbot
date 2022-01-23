import telebot,requests,urllib
from telebot import types

class bot:
	def __init__(self):
		self.bot = telebot.TeleBot("5024338795:AAFoLnw8oh1kL9XvyRS_uKI7RLuVUXOYpyU")#token
		self.admn=["1395609507"]
		self.En=['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
		self.Ar=['ض', 'ص', 'ث', 'ق', 'ف', 'غ', 'ع', 'ه', 'خ', 'ح', 'ج', 'ش', 'س', 'ي', 'ب', 'ل', 'ا', 'ت', 'ن', 'م', 'ك', 'ط', 'ذ', 'ء', 'ؤ', 'ر', 'ى', 'ة', 'و', 'ز', 'ظ', 'د', 'ئ', 'أ', 'إ', 'آ']
	def run(self):			
		@self.bot.message_handler(commands=['start'])
		def send_welcome(message):
			# -- code by ruks --		
			self.nam = message.from_user.first_name
			self.bot.send_message(message.chat.id,f"""
-- -- -- -- - -- -- -- -- -- -- -- -- --
⌯ welcome [{self.nam}](https://t.me/O9TO9) ⸙
⌯ translation bot
⌯ Coded By @MVWWW , 
⌯ Ch.Dev @O9TO9
-- -- -- -- - -- -- -- -- -- -- -- -- --
""",parse_mode="Markdown",disable_web_page_preview='True')		
		@self.bot.message_handler(func=lambda message: True)		
		def send_ruks(message):
			self.private=message.chat.type
			if self.private == "private":
				self.ms=message.text				
				self.len = types.InlineKeyboardMarkup(row_width=3)
				A1 = types.InlineKeyboardButton("العربية", callback_data="ar")
				# -- code by Ghaith --
				A2 = types.InlineKeyboardButton("النكليزية", callback_data="en")
				A3 = types.InlineKeyboardButton("الفارسية", callback_data="fr")
				A4 = types.InlineKeyboardButton("الكردية", callback_data="ku")
				A5 = types.InlineKeyboardButton("اليابانية", callback_data="ja")
				A6 = types.InlineKeyboardButton("الايطالية", callback_data="it")
				A7 = types.InlineKeyboardButton("التركية", callback_data="tr")
				A8 = types.InlineKeyboardButton("الروسية", callback_data="ru")
				A9 = types.InlineKeyboardButton("الهندية", callback_data="hi")
				A10 = types.InlineKeyboardButton("الالمانية", callback_data="de")
				A11 = types.InlineKeyboardButton("الكرواتية", callback_data="hr")
				# -- code by ruks --
				A12 = types.InlineKeyboardButton("الليتوانية", callback_data="lt")
				A13 = types.InlineKeyboardButton("الإستونية", callback_data="et")
				A14 = types.InlineKeyboardButton("الكورية", callback_data="ko")
				A15 = types.InlineKeyboardButton("البرتغالية", callback_data="pt")
				A16 = types.InlineKeyboardButton("البولندية", callback_data="pl")
				# -- code by ruks --
				A17 = types.InlineKeyboardButton("السويدية", callback_data="sv")
				A18 = types.InlineKeyboardButton("الأوكرانية", callback_data="uk-UA")
				A19 = types.InlineKeyboardButton("التايوانية", callback_data="el")
				A20 = types.InlineKeyboardButton("اليابانية", callback_data="ja")								
				self.len.add(A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,A12,A13,A14,A15,A16,A17)
				self.bot.send_message(message.chat.id,"⌯ قم بأختيار اللغة التي تريد الترجمة اليها",reply_markup=self.len)
				# -- code by ruks --				
			if message.reply_to_message:
				if message.text == "ترجمة":
					self.mas=message.reply_to_message.text
					self.get=self.translate("en", "ar", self.mas)
					self.bot.reply_to(message,self.get)	
		@self.bot.callback_query_handler(func=lambda call:True )
		def ruks(call):			
			self.get=self.translate("ar",call.data,self.ms)			
			self.bot.send_message(call.message.chat.id,self.get)
		self.str()	
		# -- code by Ghaith --								
	def translate(self,fr, to, text):
		url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl={fr}&tl={to}&hl=en-US&dt=t&dt=bd&dj=1&source=icon&tk=310461.310461&q=" + urllib.parse.quote_plus(str(text))
		response = requests.get(url).json()
		ruk=response['sentences'][0]["trans"]
		return ruk		
	def str(self):
		self.bot.polling(none_stop=True)

bot().run()