"""Delete garbage profiles from Mixpanel."""
from mixpanel import Mixpanel
from config import MIXPANEL_API_TOKEN
from .log import LOGGER

mp = Mixpanel(MIXPANEL_API_TOKEN)


def delete_mixpanel_users(users_df):
    """Delete users with invalid IDs."""
    deleted_users = 0
    for profile_id in users_df['profile_id'].values:
        LOGGER.info(f'Deleting {profile_id}')
        mp.people_delete(profile_id)
        deleted_users += 1
    return deleted_users
