from django.contrib.auth.models import User, Group
from django.db.models import Q

class UserRecommendationService:
    
    @staticmethod
    def find_similar_users(new_user, matching_threshold=1):
        
        new_user_attributes = set(new_user.attributes.attributes)
        
        similar_users = User.objects.filter(
            attributes__attributes__overlap=list(new_user_attributes)
        ).exclude(id=new_user.id)
        
        return similar_users
    

    @staticmethod
    def recommend_groups(new_user):
       
        similar_users = UserRecommendationService.find_similar_users(new_user)
        
        recommended_groups = []
        for user in similar_users:
            recommended_groups.extend(
                user.groups.values_list('name', flat=True)
            )
        
        return list(set(recommended_groups))
    
    @staticmethod
    def auto_group_recommendation(new_user):
      
        recommended_group_names = UserRecommendationService.recommend_groups(new_user)
        
        for group_name in recommended_group_names:
            group, created = Group.objects.get_or_create(name=group_name)
            new_user.groups.add(group)
        
        return recommended_group_names