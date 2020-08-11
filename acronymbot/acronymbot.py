import os
import slack
import requests
import logging
import json

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

slack_token = os.environ['SLACK_API_TOKEN']
# override base_url to use whitelisted domain
rtmclient = slack.RTMClient(
    token=slack_token.strip(), base_url='https://cdis.slack.com/api/'
)


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

                # need to point to raw data in the develop branch (latest acronyms)
                contents_url = "https://api.github.com/repos/uc-cdis/acronym-bot/contents/acronyms.txt?branch=develop"
                contents_url_info = requests.get(
                    contents_url,
                    headers={
                        "Authorization": "token {}".format(
                            os.environ['GITHUB_TOKEN'].strip()
                        )
                    },
                ).json()
                download_url = contents_url_info["download_url"]
                r = requests.get(
                    download_url,
                    headers={
                        "Authorization": "token {}".format(
                            os.environ['GITHUB_TOKEN'].strip()
                        )
                    },
                )
                if r.status_code != 200:
                    raise Exception(
                        "Unable to get file acronyms.txt at `{}`: got code {}.".format(
                            download_url[: download_url.index("token")],
                            response.status_code,
                        )
                    )
                acronyms = json.loads(r.text)
                bot_reply = None
                for k, v in acronyms.items():
                    if search_term.lower() == k.lower():
                        bot_reply = '{} stands for: {}'.format(search_term, v)
                if bot_reply == None:
                    bot_reply = 'Sorry :sadpanda: I couldn\'t find {} in the list of acronyms.'.format(
                        search_term
                    )

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
