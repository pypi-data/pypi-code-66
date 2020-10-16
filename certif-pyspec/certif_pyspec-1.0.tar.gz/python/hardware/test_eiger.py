
from eigerclient import DEigerClient

client = DEigerClient(host="applab.dectris.com", port=4011, verbose=True)

print( client.detectorConfig("flatfield_correction_applied")['value'] )
client.setDetectorConfig("flatfield_correction_applied", False)
