import os

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

def download(service, file):
  filepath = file['path']

  if file['mimeType'].endswith('.folder'):
    return

  elif file['mimeType'].startswith('application/vnd.google-apps'):
    doc = file['mimeType'].split('.')[-1]
    if doc in ['spreadsheet', 'doc', 'presentation', 'drawing']:
      if doc == 'spreadsheet':
        mtype = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        ext = 'xlsx'

      elif doc == 'doc':
        mtype = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        ext = 'docx'

      elif doc == 'presentation':
        mtype = 'application/vnd.openxmlformats-officedocument.presentationml.presentation'
        ext = 'pptx'

      elif doc == 'drawing':
        mtype = 'image/svg+xml'
        ext = 'svg'

      filepath += '.' + ext
      request = service.files().export_media(fileId=file['id'], mimeType=mtype)

    else:
      try:
        request = service.files().get_media(fileId=file['id'])

      except:
        print('Skipping, Not Downloadable:', filepath)
        return

  else:
    request = service.files().get_media(fileId=file['id'])

  print("{}  ".format(filepath), end="")
  d = os.path.dirname(filepath)
  if not os.path.exists(d):
    os.makedirs(d)

  with open(filepath, 'wb') as fh:
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
      status, done = downloader.next_chunk()
      print(".", end="")

    print("")

def main():
  client_json = os.path.join(os.path.dirname(__file__), 'client_id.json')
  flow = InstalledAppFlow.from_client_secrets_file(
    client_json,
    scopes=['https://www.googleapis.com/auth/drive']
  )
  creds = flow.run_local_server()
  service = build('drive', 'v3', credentials=creds)
  trashed = []
  page_token = None
  while 1:
    response = service.files().list(q="trashed = true",
                                    spaces='drive',
                                    fields='nextPageToken, files(id, name, parents, mimeType)',
                                    pageToken=page_token).execute()
    items = response.get('files', [])
    for item in items:
      parent = item.get('parents')
      if parent:
        tree = ["gtrash"]
        while True:
          folder = service.files().get(fileId=parent[0], fields='id, name, parents').execute()
          parent = folder.get('parents')
          if parent is None:
            break
          tree.append(folder['name'])

        tree.append(item['name'])
        item['path'] = "/".join(tree)

      else:
        item['path'] = "gtrash/" + item['name']

      trashed.append(item)

    page_token = response.get('nextPageToken', None)
    if page_token is None:
        break

  for file in trashed:
    try:
      download(service, file)

    except:
      print('Error Downloading:', file['path'])

if __name__ == "__main__":
  main()
