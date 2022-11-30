from rest_framework import serializers
from django.contrib.auth.hashers import make_password    # to bring the password to cleartext or plaintext format and it hashes it out so itbecomes unreadble format for any regular user.

from rest_framework.decorators import authentication_classes,permission_classes
from .models import CustomUser
#Decorators ?  : used to modify pre-written code in Django remotly

class UserSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):    # we are getting validated data here and we do not want to return it this way
        password = validated_data.pop('password')
        instance = self.Meta.model(**validated_data) # extracting password from validated data.
# in the models.py , password was not defined as we do not want it to be visible everywhere but we are defining it here.
# instance will interact with the model and we are gonna save it based on this. instance is coming from meta part.
# to use anything from validated data , we use the ** format. validated data is dictonary containing key-value pair.

# sanitisation(security) if password will be handled in views part.
# Below code is to make sure if password field is not empty.
        if password is not None:
            if len(password)<3:
                raise serializers.ValidationError("Password needs to be atleast of 3 character")
            instance.set_password(password)
            # instance.is_superuser= False # to create the restriction of creating superuser
        instance.save()
        return instance

    # validated data is a key-value pair
    def update(self, instance, validated_data): #instance will always be given in update, we just need to extract.
        for attr,value in validated_data.items():
            if attr== 'password':     # if attribute says that you want to update the password
                instance.set_password(value)
            else:
                setattr(instance,attr,value)
        instance.save()
        return instance

    class Meta:
        model = CustomUser
        extra_kwargs = {'password':{'write_only':True}}   # extra parameters that you want to add/modify with DB.here we are providing functionality of password change.Password is not readable and only writable.

        fields = ('name','email','password','phone','gender',
                  'is_active','is_staff','is_superuser')   # taking thee from admin panel. a superuser becomes an admin.

#       # Previously we were customising all the fields that were present in the model.
# Here we have inherited a class and that class has some methods defined previously, so we need to serialize that data too.
# write_only id is the property to the password setting it True to be only writable.
