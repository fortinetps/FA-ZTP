import codecs
import sadisplay
import os
# from entities.ansible_ztp_data_entities import Locations, DeviceLocations
import organizational_workflow_data_model


desc = sadisplay.describe(
    [getattr(organizational_workflow_data_model, attr) for attr in dir(organizational_workflow_data_model)],
    show_methods=True,
    show_properties=True,
    show_indexes=True,
)


with codecs.open('./output/organizational_workflow_data_model.dot', 'w', encoding='utf-8') as f:
    f.write(sadisplay.dot(desc))

os.system('dot -Tpng ./output/organizational_workflow_data_model.dot > ./output/organizational_workflow_data_model.png')

print('Done! See ./output/organizational_workflow_data_model.png')
