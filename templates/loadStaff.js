
window.onload = () => {
			const fragment = new URLSearchParams(window.location.hash.slice(1));

				const accessToken = fragment.get("access_token");
				const expiry = fragment.get('expires_in')
				const scopes = fragment.get('scope')
				const tokenType = fragment.get("token_type");
				window.location.replace(`/staff?token=${accessToken}&expiry=${expiry}&scopes=${scopes}`);
  }