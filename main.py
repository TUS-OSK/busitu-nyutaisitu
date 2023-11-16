import nfc
from dotenv import load_dotenv
import requests, re, os, time, logging
from pydub import AudioSegment
from pydub.playback import play
# logging
fmt = "%(asctime)s %(levelname)s %(name)s :%(message)s"
# logging.basicConfig(level=logging.INFO, format=fmt)
logging.basicConfig(filename='/home/pi/nyutaisitu.log', level=logging.INFO, format=fmt)

# sound
ASSETS_DIR = '/home/pi/busitu-nyutaisitu/assets/'
success_sound = AudioSegment.from_mp3("{}success.mp3".format(ASSETS_DIR))[:1500]
fail_sound = AudioSegment.from_mp3("{}fail.mp3".format(ASSETS_DIR))

# env for api
load_dotenv()

# get session 
session = requests.Session()
clf = nfc.ContactlessFrontend("usb")
time.sleep(2)
while True:
    logging.info("カードをかざしてください")
    try:
        tag = clf.connect(rdwr={'on-connect': lambda tag: False})
        tagd = tag.dump()
    except:
        logging.warning("scan error")
        play(fail_sound)
        continue
    try:
        gakusekiStr = re.findall('\|.*\|', tagd[6])[0]
        gakusekiStr = re.findall('[a-zA-Z0-9]*', gakusekiStr)[1][0:7]
    except:
        logging.info("\n".join(tagd))
        logging.error("parse error")
        play(fail_sound)
        continue
    logging.info(gakusekiStr)
    logging.info("カードを検知")
    try:
        baseUrl = os.environ['API_URL']
    except:
        logging.error("環境変数が正しく設定されていません")
        play(fail_sound)
        break
    url='{}?gakuseki_number={}'.format(baseUrl, gakusekiStr)
    try:
        data_response = session.get(url)
    except:
        logging.error("api error")
        play(fail_sound)
        continue
    logging.info(data_response.text)
    logging.info("正しく送信されましたa")
    play(success_sound)
