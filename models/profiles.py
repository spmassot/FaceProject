from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, JSONAttribute
from collections import namedtuple

class ProfileModel(Model):
    """
    A person-profile
    """
    class Meta:
        table_name = 'person-profile'
        region = 'us-east-1'

    ExternalID = UnicodeAttribute(hash_key=True)
    convoConfig = JSONAttribute()
    first_name = UnicodeAttribute()
    last_name = UnicodeAttribute()

def make_configr(**kwargs):
    configr = namedtuple(
        'Profile',[
            'attrA',
            'attrB',
            'attrC'
        ]
    )
    return configr(**kwargs) 

if __name__ == '__main__':
    from uuid import uuid4
    ProfileModel.create_table(
        read_capacity_units=1,
        write_capacity_units=1
    )

    profile = ProfileModel(
        uuid4().hex,
        convoConfig=make_configr(
            **{'attrA':1,'attrB':2,'attrC':3}
        ),
        first_name='Fake',
        last_name='Man'
    )
    profile.save()
    print(ProfileModel.count())
    print(profile.ExternalID)
    print(profile.first_name)
    print(profile.last_name)
    profile.delete()
