from typing import List

import prompt
import spotipy


def main():
    print('\nToken: %s' % __generate_token(
        prompt.string("Spotify username: "),
        prompt.string("Client ID: "),
        prompt.string("Client Secret: "),
        prompt.string("Redirect URI: ")
    ))


def __generate_token(username: str, client_id: str, client_secret: str, redirect_uri: str) -> str:
    scopes: List[str] = [
        'user-library-read',
        'playlist-read-public',
        'playlist-read-private',
        'playlist-modify-public',
        'playlist-modify-private'
    ]
    return spotipy.util.prompt_for_user_token(
        username,
        ' '.join(scopes),
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        show_dialog=False
    )


if __name__ == '__main__':
    main()
