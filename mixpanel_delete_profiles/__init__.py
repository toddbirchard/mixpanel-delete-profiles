"""Identify incomplete Mixpanel user profiles and delete them."""
from .load import load_mixpanel_users
from .delete import delete_mixpanel_users
from .log import LOGGER


def init_script():
	"""Remove useless profiles from Mixpanel account."""
	users_df = load_mixpanel_users()
	result = delete_mixpanel_users(users_df)
	LOGGER.info(f'Deleted {len(result)} user profiles.')


