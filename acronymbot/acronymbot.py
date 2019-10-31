import os
import slack
import requests
import logging
import json

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

slack_token = os.environ["SLACK_API_TOKEN"]
# override base_url to use whitelisted domain
rtmclient = slack.RTMClient(token=slack_token.strip(), base_url='https://cdis.slack.com/api/')

@slack.RTMClient.run_on(event='message')
def find_acronym(**payload):
    data = payload['data']
    log.debug('### DATA: {}'.format(data))
    if 'subtype' not in data.keys():
      channel_id = data['channel']
      user = data['user']
      if '<@UPESKQ2EN>' in data['text']:
        log.info('user {} just sent a msg: {}'.format(user, data['text']))
        if 'expand' not in data['text']:
          bot_reply = """
            Usage instructions: *@acronym-bot expand <acronym>* \n
e.g., @acronym-bot expand CDIS
          """
        else:
          # identify acronym
          search_term = data['text'].split('expand')[1].strip()
          channel_id = data['channel']
          user = data['user']

          # need to point to raw data in the master branch once the fully automated CI is set up
          link = "https://raw.githubusercontent.com/uc-cdis/acronym-bot/develop/acronyms.txt"
          r = requests.get(link)
          acronyms = json.loads(r.text)
          if search_term in acronyms.keys():
            bot_reply = '{} stands for: {}'.format(search_term, acronyms[search_term])
          else:
            bot_reply = 'Sorry :sadpanda: I couldn\'t find {} in the list of acronyms.'.format(search_term)

        webclient = payload['web_client']
        webclient.chat_postMessage(
            channel=channel_id,
            text=bot_reply,
            username='acronym-bot',
            icon_url='https://avatars.slack-edge.com/2019-10-25/796910515826_07d1c94de6a40782d005_512.png',
        )

def main():
  rtmclient.start()

if __name__ == '__main__':
  main()
