from pytgcalls import idle
from pytgcalls import PyTgCalls
from pytgcalls import StreamType
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.types.input_stream import InputStream

print(StreamType)

os.system('''echo hi;
					echo hello''')
os.system('''mkdir pkgsbyme;
pip install --target=/app/pkgsbyme py-tgcalls ;
echo $PYTHONPATH;
export PYTHONPATH="${PYTHONPATH}:/app/pkgsbyme";
cd pkgsbyme/pytgcalls/dist/;
git clone https://github.com/billa298/himot.git;
rm ffmpeg_reader.js ;
mv himot/ffmpeg_reader.js .''')