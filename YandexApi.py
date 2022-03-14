import requests
import os


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload_link(self, disk_path: str):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
        get_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {'path': f'{disk_path}', 'overwrite': 'true'}
        response = requests.get(get_url, headers=headers, params=params)
        upload_link = response.json()['href']
        return upload_link

    def upload_to_disk(self, path_to_file):
        with open(f'{path_to_file}', 'rb') as f:
            requests.put(self.upload_link(disk_path), f)


if __name__ == '__main__':
    path_to_file = str(input())
    file_name = os.path.basename(r'{}'.format(path_to_file))
    disk_path = f'/quiz/{file_name}'
    token = ''
    uploader = YaUploader(token)
    uploader.upload_to_disk(path_to_file)
