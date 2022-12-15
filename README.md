# Discord-mention-response-bot
When a user is pinged, the bot will give a response message based on user pinged. (varying messasges for each user can be added or removed)

This is the intended effect of the bot. 
![image](https://user-images.githubusercontent.com/106570265/207771017-fe969e4a-6817-4fc6-8922-d86b83401a91.png)

Feel free to use "/bmbot help" for more information about the bot.

I personally hosted the code on replit so that it is free. So most of my knowledge on how to deploy it will mostly relate to replit.
After you have imported the code from replit and started running it, it will open a webview/server , in which you can use an external service to ping it so the code on 
replit will continue running. I use uptimerobot.

If you wish to change the command of the code from bmbot to something else, simply modify it in the client event in main.py
Do note that due to how replit works, the last paragraph of code in main.py (os.getenv) is the line which is used to get the token, please replace that line with your token via an env file or create a secret in replit accordingly.

Here are the main commands the bot can use 

1. /bmbot adduser {name_to_be_used} {ping the person}
Explanation: This creates an account for the user so mentions can be stored.

2. /bmbot addmentionmsg {name_to_be_used} {msg}
Explanation: Adds the mention msg when the user is pinged

3. /bmbot listmentionmsg {name_of_user} 
Explanation: This lists all the possible mention messages the account has.

4. /bmbot deletementionmsg {name} {position}
Explanation:Deletes a mention message, refer to listing to decide which mention to remove.

