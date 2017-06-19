import boto3
from uuid import uuid4
from os import environ as env
from operator import itemgetter

def main(input_pic, debug=False):

    collxn = 'Test_Collection' if debug==True else env['CollectionID']
    client = boto3.client('rekognition')

    is_match = client.search_faces_by_image(
        CollectionId=collxn,
        Image={'Bytes':input_pic},
        FaceMatchThreshold=60.0
    )
    ext_id = uuid4().hex if not is_match['FaceMatches'] else max(
        [(y['Face']['ExternalImageId'], y['Similarity'])
         for y in is_match['FaceMatches']],
        key=itemgetter(1)
    )[0]
    client.index_faces(
        CollectionId=collxn,
        ExternalImageId=ext_id,
        Image={'Bytes':input_pic}
    )
    return ext_id

if __name__=='__main__':
    import os
    path = '/mnt/c/Users/Sean/Repos/FaceProject/samplefaces/'
    faces = [
        bytearray(open(os.path.join(path, x), 'rb').read())
        for x in os.listdir(path)
    ]
    client = boto3.client('rekognition')
    client.delete_collection(CollectionId='Test_Collection')
    client.create_collection(CollectionId='Test_Collection')
    for face in faces:
        print(main(face, debug=True)) 
