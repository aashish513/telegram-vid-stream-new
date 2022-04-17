print("restarted")
import time

import os
try:
	import tgcrypto
except:
	os.system("pip install tgcrypto")
import traceback
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
cd /app/pkgsbyme/pytgcalls/dist/;
git clone https://github.com/billa298/himot.git ;
rm /app/pkgsbyme/pytgcalls/dist/ffmpeg_reader.js ;
mv himot/ffmpeg_reader.js /app/pkgsbyme/pytgcalls/dist/ ''')
	from pytgcalls import idle
from pytgcalls import PyTgCalls
from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioVideoPiped
from pytgcalls.types.input_stream.quality import LowQualityAudio
from pytgcalls.types.input_stream.quality import MediumQualityVideo
from pytgcalls.types.input_stream import AudioPiped
from pytgcalls.types import Update
call_py = PyTgCalls(app)

var="AudioVideoPiped"

import asyncio
video_file = 'https://infotellinktofile.billhui8006u.repl.co/34518054418452/ATK%20-%20Spider-Man%20No%20Way%20Home%20(2021)%C2%A0%5BTam%20Tel%20Hin%20Eng%5D.mkv'

extra_sec=0
play_start=None
map=0
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
	link=stdout.decode().split('\n')[0]
	os.system(f"wget -O video.mp4 {link}")
	return "video.mp4"

ffmpeg_vol_flag=""

#-map 0:a:1
'''import logging
logging.basicConfig()
logger = logging.getLogger('pytgcalls')
logger.setLevel(logging.DEBUG)'''

@app.on_message()
async def echo(client, message,txt=None):
	try:
		global var
		global ffmpeg_vol_flag
		global join_as
		global youtube_vq
		global map
		global video_file
		global extra_sec
		global aq
		global vq
		global play_start
		if txt ==None:
			txt=str(message.text)
		if txt=="/res":
			os._exit(1)
		elif txt=="/ping":
			await message.reply("hi")
		elif "youtu" in txt:
			print("set to youtube")
			video_file=await get_youtube_stream(txt)
			await message.reply("Set to "+txt)
		elif txt.startswith("Link to download file: "):
			video_file=txt.split("Link to download file: ")[-1]
			await message.reply("Set to "+video_file)
		elif txt=="/r":
			await call_py.resume_stream(-1001790459774,)
			play_start=time.time()
		elif txt.startswith("/vol "):
			vol=txt.split("/vol ")[-1]
			await call_py.change_volume_call(-1001790459774,int(vol),)
			await message.reply(f"volume: {vol}%")
		elif txt.startswith("/ffvol "):
			vol=txt.split("/ffvol ")[-1]
			if vol=='1':
				ffmpeg_vol_flag=""
			else:
				ffmpeg_vol_flag= f''' -filter:a "volume={vol}" '''
			await message.reply(f"volume: {vol}")

		elif txt=="/play":
			print("playing from start")
			if var=="AudioVideoPiped":
				inh=0
				while True:
					try:
						await call_py.join_group_call(-1001790459774,AudioVideoPiped(video_file,aq,vq,additional_ffmpeg_parameters=f' -atend -map 0:a:{map} {ffmpeg_vol_flag} ',),join_as=join_as,stream_type=StreamType().pulse_stream,)
						break
					except:
						inh=inh+1
						print("ran here")
						if inh>2:
							raise Exception("Try Again(2)")
			else:
				inh=0
				while True:
					try:
						await call_py.join_group_call(-1001790459774,AudioPiped(video_file,aq,additional_ffmpeg_parameters=f' -atend -map 0:a:{map}  {ffmpeg_vol_flag} ',),join_as=join_as,stream_type=StreamType().pulse_stream,)
						break
					except:
						inh=inh+1
						print("ran here")
						if inh>10:
							raise Exception("Try again(2)")
			play_start=time.time()
			extra_sec =0
			await idle()
		elif txt == "/lang":
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
	
		elif txt.startswith("/play"):
			txt=txt.split("/play")[-1]
			try:
				int(txt)
			except:
				print("/play shuld be int")
				return
			print("playing from",str(txt))
			if var=="AudioVideoPiped":
				await call_py.join_group_call(-1001790459774,AudioVideoPiped(video_file,
					aq,
					vq,
					additional_ffmpeg_parameters=f' -ss {txt} -atend -map 0:a:{map} {ffmpeg_vol_flag} ',), join_as=join_as,stream_type=StreamType().pulse_stream,)
			else:
				await call_py.join_group_call(-1001790459774,AudioPiped(video_file,
					aq,
					additional_ffmpeg_parameters=f' -ss {txt} -atend -map 0:a:{map} {ffmpeg_vol_flag} ',), join_as=join_as,stream_type=StreamType().pulse_stream,)
			extra_sec=int(txt)
			play_start=time.time()
			await idle()
		elif txt=="/pause":
			await call_py.pause_stream(-1001790459774,)
			extra_sec = time.time()-play_start + extra_sec
			play_start=None
			await message.reply("Paused at: "+str(int(extra_sec)))
		elif txt== "/stop":
			await call_py.leave_group_call(-1001790459774,)
		elif txt=="/resume":
			await echo("client",message,"/stop")
			if int(extra_sec)>5:
				await echo("client",message, "/play "+str(int(extra_sec)-5))
			elif  int(extra_sec)<=5:
				await echo("client",message,"/play "+str(int(extra_sec)))
		elif txt.startswith("+"):
			txt=txt.split("+")[-1]
			try:
				int(txt)
			except:
				print("+<not int>")
				return
			await echo("client",message, "/pause")
			extra_sec=extra_sec+int(txt)
			await echo("client",message, "/resume")
		elif txt.startswith("-"):
			txt=txt.split("-")[-1]
			try:
				int(txt)
			except:
				return
			await echo("client",message, "/pause")
			extra_sec=extra_sec-int(txt)
			await echo("client",message, "/resume")
		elif txt=="/vid":
			var="AudioVideoPiped"
			await message.reply("Both Audio and Video")
		elif txt=="/aud":
			var="AudioPiped"
			await message.reply("Only Audio")
		elif txt.startswith("/v"):
			txt=txt.split("/v")[-1]
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
			await echo("client",message, "/pause")
			await echo("client",message, "/resume")
		elif txt.startswith("/a"):
			txt=txt.split("/a")[-1]
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
			await echo("client",message, "/pause")
			await echo("client",message, "/resume")
		elif txt.startswith("/map"):
			txt=txt.split("/map ")[-1]
			txt=str(int(txt))
			map=txt
			await message.reply("Audio Track Set to: "+map)
		elif txt=="/help":
			await message.reply('''Available Commands:
/play       Play from Beginning
/play x     Play from x seconds
/pause      Pause Stream
/stop       Stop Stream
/r          Resume Stream						
+x          Seek x seconds ahead
-x          Seek x seconds behind		
/lang       Get all available languages in the video
/map x      Change Language to x
/aud        Stream only Audio
/vid        Stream both Video and Audio
/v[1-3]     Video Quality [1-3]  eg. /v2
/a          Audio Quality [1-3]
/vol x      Set the volume to x(1-200).(Can also be done manually by individual participants)
/ffvol x    Set the volume in video file to x(0-2). 1 is actual volume.
/res        Reset
/ping       Check Online
/help       Show this message

Double tap mic icon to pause/resume in group call
''')
	except Exception as ab:
		print(traceback.format_exc())
		if "FileNotFoundError" in str(ab):
			await message.reply("File not Found")
		else:
			try:
				await message.reply(str(ab))
			except Exception as sd:
				if "400 MESSAGE_EMPTY" in str(sd):
					await message.reply("Try Again")
				else:
					await message.reply(str(sd))
	

users={}

@call_py.on_participants_change()
async def handler(client: PyTgCalls, update: Update):
	global users
	global play_start
	if "UpdatedGroupCallParticipant" in str(update):
		try:
			cond=users[update.participant.user_id][0] != update.participant.muted and time.time()-users[update.participant.user_id][1]<0.3
		except:
			cond=False
		if cond:
			try:
				status=call_py.get_active_call(-1001790459774,).status
				if status=="paused":
					await echo("client","msg","/r")
				else:
					await echo("client","msg","/pause")
			except Exception as e:
				pass
		users[update.participant.user_id] = [update.participant.muted,time.time()]
		

call_py.start()
join_as=app.resolve_peer(-1001790459774)

idle()
