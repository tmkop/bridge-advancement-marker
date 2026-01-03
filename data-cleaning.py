import json
from datetime import datetime

def filter_messages_from_2026():
    """
    Filters messages from 2026_chatlog_bot.json that are sent by bots, posted after Jan 1st, 2026, 4:37pm, and contain 'has made the advancement'.
    
    Returns:
        list: A list of bot messages from 2026 after the cutoff containing the advancement text.
    """
    with open('2026_chatlog_bot.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    cutoff = datetime.fromisoformat('2026-01-01T16:37:00-05:00')
    messages = data.get('messages', [])
    filtered_messages = [msg for msg in messages if 
                         msg.get('author', {}).get('isBot') == True and 
                         datetime.fromisoformat(msg.get('timestamp', '')) > cutoff and 
                         any('has made the advancement' in embed.get('description', '') for embed in msg.get('embeds', []))]
    
    return filtered_messages
    
    return filtered_messages

if __name__ == "__main__":
    filtered = filter_messages_from_2026()
    print(f"Found {len(filtered)} messages from 2026.")

    # Save the filtered messages to 2026_advancements.json
    with open('2026_advancements.json', 'w', encoding='utf-8') as f:
        json.dump({"messages": filtered}, f, indent=2, ensure_ascii=False)
    print("Filtered messages saved to 2026_advancements.json.")
