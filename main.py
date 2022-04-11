from pyrogram import Client

from pytgcalls import idle
from pytgcalls import PyTgCalls
from pytgcalls import StreamType
from pytgcalls.types.input_stream import AudioVideoPiped
import os

app = Client(
    session_name=os.environ['joma'],
    api_id=int(os.environ['ab']),
    api_hash=os.environ['cd'],
)

call_py = PyTgCalls(app)
call_py.start()
video_file = 'test.mkv'
call_py.join_group_call(
    -1001547787482,
    AudioVideoPiped(
        video_file,
    ),
    stream_type=StreamType().pulse_stream,
)
idle()