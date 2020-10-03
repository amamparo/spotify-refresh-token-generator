from typing import List

import prompt
import spotipy


def main():
    print('\nRefresh Token: %s' % __generate_token(
        prompt.string("Spotify username: "),
        prompt.string("Client ID: "),
        prompt.string("Client Secret: "),
        prompt.string("Redirect URI: ")
    ))


def __generate_token(username: str, client_id: str, client_secret: str, redirect_uri: str) -> str:
    scopes: List[str] = [
        'user-library-read',
        'playlist-read-private',
        'playlist-modify-public',
        'playlist-modify-private'
    ]
    sp_oauth = spotipy.SpotifyOAuth(
        client_id,
        client_secret,
        redirect_uri,
        scope=' '.join(scopes),
        username=username,
        show_dialog=True
    )
    code = sp_oauth.get_auth_response()
    token = sp_oauth.get_access_token(code)
    return token['refresh_token']


if __name__ == '__main__':
    main()
