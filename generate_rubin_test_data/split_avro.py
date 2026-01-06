from fink_client.avro_utils import write_alert
from fink_alert_simulator.avroUtils import readschemadata
import os
import glob

version = "10_0"
folder = "rubin_test_data_{}.avro".format(version)
avro_file = glob.glob(os.path.join(folder, "part*"))[0]

folder_tmp = folder + "_tmp"
os.makedirs(folder_tmp, exist_ok=True)

with open(avro_file, mode='rb') as file_data:
    data = readschemadata(file_data)
    schema = data.schema
    for record in data:
        write_alert(
            record, 
            schema, 
            folder_tmp,
            id1="diaSourceId", 
            id2="diaSourceId",
            overwrite=True
        )

files = glob.glob(os.path.join(folder_tmp, "*.avro"))
if len(files) > 0:
    os.rmdir(folder)
    os.rename(folder_tmp, folder)
else:
    print("{} is empty".format(folder_tmp))
