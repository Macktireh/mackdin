import os
import datetime
import uuid


def rename_post_img_video(instance, filename):
    ext = filename.split('.')[-1]
    name = ''
    for i in range((len(filename.split('.'))-1)):
        name += filename.split('.')[i]
    filename = f"{name}_{datetime.datetime.now().strftime('%d-%m-%Y_%H%M%S')}.{ext}"
    folder = f"{instance.author.pk}-{instance.author.first_name}"
    if ext.lower() in ['png', 'jpg', 'jpeg', 'gif']:
        return os.path.join('media', folder, 'image_post', filename)
    return os.path.join('media', folder, 'video_post', filename)


def rename_profile_img(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.user.first_name}_{datetime.datetime.now().strftime('%d-%m-%Y_%H%M%S')}.{ext}"
    folder = f"{instance.user.pk}-{instance.user.first_name}"
    return os.path.join('media', folder, 'image_profile', filename)

def uid_gerator() -> str:
    uid = str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '') + str(uuid.uuid4()).replace('-', '')
    return str(uid)
