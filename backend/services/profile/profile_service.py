from backend.repositories.profile.profile_repository import ProfileRepository
from backend.models.profile.profile import Profile

class ProfileService:
    def __init__(self, profile_repository: ProfileRepository):
        self.profile_repository = profile_repository

    def create_profile(self, profile_data: Profile) -> Profile:
        profile = Profile(**profile_data.dict(), created_at=datetime.now(), updated_at=datetime.now())
        return self.profile_repository.create_profile(profile)

    def update_profile(self, profile_id: int, profile_data: Profile) -> Profile:
        existing_profile = self.profile_repository.get_profile_by_id(profile_id)
        if not existing_profile:
            raise Exception('Profile not found')
        updated_data = profile_data.dict(exclude_unset=True)
        for key, value in updated_data.items():
            setattr(existing_profile, key, value)
        existing_profile.updated_at = datetime.now()
        return self.profile_repository.update_profile(existing_profile)

    def get_profile(self, profile_id: int) -> Profile:
        return self.profile_repository.get_profile_by_id(profile_id)

    def delete_profile(self, profile_id: int) -> None:
        self.profile_repository.delete_profile(profile_id)