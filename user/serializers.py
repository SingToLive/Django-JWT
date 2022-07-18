from rest_framework import serializers
from user.models import User

class UserSerializer(serializers.ModelSerializer):
   class Meta:
        # serializer에 사용될 model, field지정
        model = User
        # 모든 필드를 사용하고 싶을 경우 fields = "__all__"로 사용
        # fields = "__all__"
        fields = ["id"] # 부여되는 아이디만
        
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# TokenObtainPairSerializer를 상속하여 클레임 설정
class SpartaTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
				# 생성된 토큰 가져오기
        token = super().get_token(user)

        # 사용자 지정 클레임 설정하기.
        token['id'] = user.id
        token['username'] = user.username

        return token