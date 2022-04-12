print("restarted")

import time

import os
try:
	import tgcrypto
except:
	os.system("pip install tgcrypto")

try:
	from pyrogram import Client
except:
	os.system("pip install pyrogram")
	from pyrogram import Client
from pyrogram import filters

app = Client(
    session_name=os.environ['joma'],
    api_id=int(os.environ['ab']),
    api_hash=os.environ['cd'],
)

from pyrogram.types import Message
import sys

#os.system("pip uninstall py-tgcalls -y")
#os.system("rm -r /app/pytgcalls")
#os.system("git clone https://github.com/billa298/pytgcalls.git /app/pytgcalls/")
#sys.path.insert(0,str(os.getcwd())+"/pytgcalls")
#sys.path.insert(0,"/app/pytgcalls/pytgcalls")
#print(str(os.getcwd()))
try:
	from pytgcalls import idle
except:
	#import sys
	#os.system("git clone https://github.com/billa298/pytgcalls.git")
	#sys.path.insert(0,str(os.getcwd())+"/pytgcalls")
	os.system('''mkdir pkgsbyme;
pip install --target=/app/pkgsbyme py-tgcalls ;
echo $PYTHONPATH;
export PYTHONPATH="${PYTHONPATH}:/app/pkgsbyme";
cd pkgsbyme/pytgcalls/dist/;
git clone https://github.com/billa298/himot.git;
rm ffmpeg_reader.js ;
mv himot/ffmpeg_reader.js .''')
	from pytgcalls import idle
from pytgcalls import PyTgCalls
from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioVideoPiped
from pytgcalls.types.input_stream.quality import LowQualityAudio
from pytgcalls.types.input_stream.quality import MediumQualityVideo
call_py = PyTgCalls(app)


import asyncio
video_file = 'https://infotellinktofile.billhui8006u.repl.co/34518054418452/ATK%20-%20Spider-Man%20No%20Way%20Home%20(2021)%C2%A0%5BTam%20Tel%20Hin%20Eng%5D.mkv'

extra_sec=0
play_start=None

vq=MediumQualityVideo()
aq=LowQualityAudio()

youtube_vq= 'best[height<=?480][width<=?852]'
async def get_youtube_stream(link):
	global youtube_vq
	try:
		import youtube_dl
	except:
		os.system("pip install youtube_dl")
	proc = await asyncio.create_subprocess_exec(
			'youtube-dl',
			'-g',
			'-f',
			# CHANGE THIS BASED ON WHAT YOU WANT
			youtube_vq,
			link,
			stdout=asyncio.subprocess.PIPE,
			stderr=asyncio.subprocess.PIPE,
	)
	stdout, stderr = await proc.communicate()
	return stdout.decode().split('\n')[0]


#-map 0:a:1
'''import logging
logging.basicConfig()
logger = logging.getLogger('pytgcalls')
logger.setLevel(logging.DEBUG)'''

@app.on_message()
async def echo(client, message,txt=None):
	try:
		global youtube_vq
		global video_file
		global extra_sec
		global aq
		global vq
		global play_start
		if txt ==None:
			txt=str(message.text)
		if txt=="!res":
			os._exit(1)
		elif txt=="!ping":
			await message.reply("hi")
		elif "youtu" in txt:
			print("set to youtube")
			video_file=await get_youtube_stream(txt)
			await message.reply("Set to "+txt)
		elif txt.startswith("Link to download file: "):
			video_file=txt.split("Link to download file: ")[-1]
			await message.reply("Set to "+video_file)
		elif txt=="!play":
			print("playing from start")
			await call_py.join_group_call(-1001790459774,AudioVideoPiped(video_file,
					aq,
	        vq,
	    ),join_as=await app.resolve_peer(-1001790459774),stream_type=StreamType().pulse_stream,)
			play_start=time.time()
			extra_sec =0
		elif txt == "!lang":
			import subprocess
			ffprobe_cmd = f"ffmpeg -i '{video_file}'"
			process = subprocess.Popen(ffprobe_cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=True)
			output = str(process.communicate()[1]).split("Stream")
			output.pop(0)
			streams=""
			for i in output:
					stream=i.split("Metadata")[0]
					streams=streams+stream+"\n"
			await message.reply(f"<code> {streams} </code>",parse_mode="html")
	
		elif txt.startswith("!play"):
			txt=txt.split("!play")[-1]
			try:
				int(txt)
			except:
				print("!play shuld be int")
				return
			print("playing from",str(txt))
			await call_py.join_group_call(-1001790459774,AudioVideoPiped(video_file,
					aq,
	        vq,
					additional_ffmpeg_parameters=f' -ss {txt} -atend -map 0:v:0 -map 0:a:3',), join_as=await app.resolve_peer(-1001790459774),stream_type=StreamType().pulse_stream,)
			extra_sec=int(txt)
			play_start=time.time()
		elif txt=="!pause":
			await call_py.pause_stream(message.chat.id,)
			extra_sec = time.time()-play_start + extra_sec
			play_start=None
			await message.reply("Paused at: "+str(int(extra_sec)))
		elif txt== "!stop":
			await call_py.leave_group_call(message.chat.id,)
		elif txt=="!resume":
			await echo("client",message,"!stop")
			if int(extra_sec)>5:
				await echo("client",message, "!play "+str(int(extra_sec)-5))
			elif  int(extra_sec)<=5:
				await echo("client",message,"!play "+str(int(extra_sec)))
		elif txt.startswith("+"):
			txt=txt.split("+")[-1]
			try:
				int(txt)
			except:
				print("+<not int>")
				return
			await echo("client",message, "!pause")
			extra_sec=extra_sec+int(txt)
			await echo("client",message, "!resume")
		elif txt.startswith("-"):
			txt=txt.split("-")[-1]
			try:
				int(txt)
			except:
				return
			await echo("client",message, "!pause")
			extra_sec=extra_sec-int(txt)
			await echo("client",message, "!resume")
		elif txt.startswith("!v"):
			txt=txt.split("!v")[-1]
			try:
				txt=int(txt)
			except:
				return
			if txt ==1:
				await message.reply("Video Quality: 1")
				from pytgcalls.types.input_stream.quality import LowQualityVideo
				vq=LowQualityVideo()
				youtube_vq='best[height<=?480][width<=?852]'
				await message.reply("youtube v1")
			elif txt ==2:
				await message.reply("Video Quality: 2")
				vq=MediumQualityVideo()
			elif txt ==3:
				await message.reply("Video Quality: 3")
				from pytgcalls.types.input_stream.quality import HighQualityVideo
				vq=HighQualityVideo()
				youtube_vq='best[height<=?720][width<=?1280]'
				await message.reply("youtube v3")
			else:
				return
			await echo("client",message, "!pause")
			await echo("client",message, "!resume")
		elif txt.startswith("!a"):
			txt=txt.split("!a")[-1]
			try:
				txt=int(txt)
			except:
				return
			if txt ==1:
				await message.reply("Audio Quality: 1")
				aq=LowQualityAudio()
			elif txt ==2:
				await message.reply("Audio Quality: 2")
				from pytgcalls.types.input_stream.quality import MediumQualityAudio
				aq=MediumQualityAudio()
			elif txt ==3:
				await message.reply("Audio Quality: 3")
				from pytgcalls.types.input_stream.quality import HighQualityAudio
				aq=HighQualityAudio()
			else:
				return
			await echo("client",message, "!pause")
			await echo("client",message, "!resume")
	except Exception as ab:
		if "FileNotFoundError" in str(ab):
			await message.reply("File not Found")
		else:
			await message.reply(str(ab))
	
			
			
		




call_py.start()



idle()
