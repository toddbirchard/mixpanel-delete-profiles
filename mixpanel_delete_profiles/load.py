"""Load Mixpanel users from locally stored CSV."""
import pandas as pd
from .log import LOGGER


def load_mixpanel_users():
	"""Create DataFrame of Mixpanel user profiles to be deleted."""
	users_df = pd.read_csv('data/users.csv')
	LOGGER.info(f'Number of users before purge: {len(users_df)}')
	users_df = users_df[users_df.id == 'undefined']
	LOGGER.info(f'Number of users after purge: {len(users_df)}')
	return users_df
