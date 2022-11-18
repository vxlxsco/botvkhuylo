import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(token = 'dobavit')
longpoll = VkLongPoll(vk_session)


def sender(id,text):
    vk_session.method('messages.send', {'chat_id' : id, 'message' : text, 'random_id' : 0})

def reader(message_ids):
    vk_session.method('messages.markAsRead', {'message_ids' : message_ids})


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.from_chat:

                msg = event.text.lower()
                id = event.chat_id
                
                if msg == 'work?':
                    sender(id,'yes')

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        peer = event.peer_id
        message_ids = event.message_id
        reader(message_ids)
         







