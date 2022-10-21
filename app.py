import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

# Listens to incoming messages that contain "ajuda"
@app.message("ajuda")
def message_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    say(
        blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"Olá <@{message['user']}>! Precisa de ajuda? Clique no botão para falar comigo :crystal_ball: :crystal_ball: !"},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Click Me"},
                    "action_id": "button_click"
                }
            }
        ],
        text=f"Hey there <@{message['user']}>!"
    )

@app.action("button_click")
def action_button_click(body, ack, client):
    # Acknowledge the action
    ack()

    res = client.views_open(
        trigger_id=body["trigger_id"],
        view={
            "type": "modal",
            "callback_id": "gratitude-modal",
            "title": {"type": "plain_text", "text": "Helper Box"},
            "submit": {"type": "plain_text", "text": "Submit"},
            "close": {"type": "plain_text", "text": "Cancel"},
            "blocks": [
                {
                    "type": "input",
                    "block_id": "my_block",
                    "element": {"type": "plain_text_input", "action_id": "my_action"},
                    "label": {"type": "plain_text", "text": "Say something nice!"},
                }
            ],
        },
    )

@app.view("gratitude-modal")
def view_submission(ack, body, client,):
    ack()
    #logger.info(body["view"]["state"]["values"])
    #Extra Credit: Uncomment out this section
    thank_you_channel="C0475374C13"
    user_text = body["view"]["state"]["values"]["my_block"]["my_action"]["value"]   
    client.chat_postMessage(channel=thank_you_channel, text=user_text)    

# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()