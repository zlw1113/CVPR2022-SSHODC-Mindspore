import random
import json

json_path1 = 'data/RIT-HS20/annotationsjson/instances_train_s10.json'
json_path2 = 'data/RIT-HS20/annotationsjson/pseudo.json'
def combine_json():

    with open(json_path1, 'r') as f:
        tn_data = json.load(f)

    with open(json_path2, 'r') as f:
        tn_data_ssl = json.load(f)

    images = []
    ann = []
    for image_tn in tn_data['images']:
        images.append(image_tn)

    for image_ssl in tn_data_ssl['images']:
        images.append(image_ssl)

    for ann_tn in tn_data['annotations']:
        ann.append(ann_tn)

    for index, ann_ssl in enumerate(tn_data_ssl['annotations']):
        ann_ssl['id'] = index + 446
        ann.append(ann_ssl)
    # print(ann[445], ann[446], ann[4758])

    images_test_dict = {"images": images, 'type': tn_data['type'], 'annotations': ann,
                        'categories': tn_data['categories']}

    print('#########split_done##########')

    with open('data/RIT-HS20/annotationsjson/all_pseudo.json', 'w') as test_json:
        json.dump(images_test_dict, test_json)

    # cal_data
    # c1 = []
    # c2 = []
    # c3 = []
    # c4 = []
    # for i, data_anno in enumerate(images_test_dict['annotations']):
    #
    #     if data_anno['category_id'] == 1:
    #         c1.append(data_anno)
    #     elif data_anno['category_id'] == 2:
    #         c2.append(data_anno)
    #     elif data_anno['category_id'] == 3:
    #         c3.append(data_anno)
    #     else:
    #         c4.append(data_anno)
    #
    # print('c1: {} \n c2: {} \n c3: {}'.format(len(c1), len(c2), len(c3)  ) )

    # with open('./train1.json', 'w') as train_json:
    #     json.dump(images_train_dict, train_json)
    #




if __name__ == '__main__':
    combine_json()