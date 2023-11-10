import nfc
from dotenv import load_dotenv
import requests, re, os, time, logging

load_dotenv()
# logging.basicConfig(level=logging.INFO)

fmt = "%(asctime)s %(levelname)s %(name)s :%(message)s"
logging.basicConfig(filename='nyutaisitu.log', level=logging.INFO, format=fmt)

session = requests.Session()
clf = nfc.ContactlessFrontend("usb")
while True:
    time.sleep(2)
    logging.info("カードをかざしてください")
    try:
        tag = clf.connect(rdwr={'on-connect': lambda tag: False})
        tagd = tag.dump()
    except:
        logging.warning("scan error")
        break
    try:
        gakusekiStr = re.findall('\|.*\|', tagd[6])[0]
        gakusekiStr = re.findall('[a-zA-Z0-9]*', gakusekiStr)[1][0:7]
    except:
        logging.info("\n".join(tagd))
        logging.error("parse error")
        continue
    logging.info(gakusekiStr)
    logging.info("カードを検知")
    # print(gakusekiStr)
    try:
        baseUrl = os.environ['API_URL']
    except:
        logging.error("環境変数が正しく設定されていません")
        break
    url='{}?gakuseki_number={}'.format(baseUrl, gakusekiStr)
    try:
        data_response = session.get(url)
    except:
        logging.error("api error")
        continue
    logging.info(data_response.text)
    logging.info("正しく送信されました")
