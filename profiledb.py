from models.profiles import ProfileModel

def put_profile(ext_id, convoConfig, **kwargs):
    ProfileModel(ext_id, convoConfig, **kwargs).save()

def get_profile(ext_id):
    return ProfileModel.query(ext_id).convoConfig
