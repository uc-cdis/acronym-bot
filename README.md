# acronym-bot

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![GitHub contributors](https://img.shields.io/github/contributors/uc-cdis/acronym-bot.svg)](https://github.com/uc-cdis/acronym-bot/graphs/contributors)

**Why**: There are too many acronyms. The majority of them represent the name of entities (non-profit organizations, professional associations, research institutes, governmental agencies, etc.) whereas some of them are related to biomedicine jargons and others are associated with data security terminology (e.g., FISMA, HIPAA, PHI, PII, etc.). That is why there is a need for a friendly tool that provides the meaning of such acronyms.

**What**: The acronym-bot is a Slack bot that can be invited to any channel to help expand acronyms.

**How**: The Slack bot is written in Python and it utilizes the `python-slackclient` lib (py3) to operate through the RTM (Real Time Messaging) protocol.

How to use:
--
### Expanding acronyms
Simply invite the `@acronym-bot` to any channel and post a message asking it to expand a given acronym, e.g.:
> [you]
> `@acronym-bot expand NHLBI`

And wait for a response like:
> [acronym-bot]
> NHLBI stands for: National Heart, Lung, and Blood Institute

### Adding new acronyms
Just edit the `acronyms.txt` file (add as many new acronyms as you want!), create a PR, get someone else to review and then merge the changes. This will be picked up by the bot immediately, there is no need for any reload / restart.

:warning: It is recommended that the collaborators run: `git config core.hooksPath .githooks` to enable the pre-commit hook that validates the JSON structure of `acronyms.txt`.

Other operational stuff:
--

### Production readiness:
- README :ballot_box_with_check:
- Operational requirements:
  - **Configuration**:
    - Docker build instructions: [Dockerfile](https://github.com/uc-cdis/acronym-bot/blob/develop/Dockerfile) 
    - Kubernetes deployment descriptor: [acronymbot-deployment](https://github.com/uc-cdis/cloud-automation/blob/master/kube/services/acronymbot/acronymbot-deploy.yaml)
    - Secret SLACK_API_TOKEN: Secured in the dev vm to facilitate the creation of the k8s secret, as per the [secret mgmt process](https://github.com/uc-cdis/cloud-automation/blob/master/doc/secrets.md)).
  - **Startup and Shutdown**
    - TBD...
  - Queue Draining: N/A
  - **Software Upgrades**
     - Rolling upgrade (ZDT) through k8s
  - Backups and Restores: N/A
  - **Redundancy**
      - TBD...
  - Replicated Databases: N/A
  - Hot Swaps: N/A
  - **Toggles for Individual Features**
       - TBD...
  - **Graceful Degradation**
       - TBD...
  - Access Controls and Rate Limits: N/A
  - Data Import Controls: N/A
  - **Monitoring**:
    - Grafana dashboard: `dashboard.json`
  - **Auditing**
    - Every change against the Slack bot logic & the acronym list is tracked in Git.
  - Debug Instrumentation: N/A
  - **Exception Collection**:
    - TBD (Logging)...
  - **Documentation for Operations**:
    - Runbook (TBD)... 
