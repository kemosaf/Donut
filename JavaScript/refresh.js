
window.onload = () => {
                        //async function startLoad() {
			const fragment = new URLSearchParams(window.location.hash.slice(1));

				const accessToken = fragment.get("access_token");
				const tokenType = fragment.get("token_type");
				window.location.replace(`/profile?token=${accessToken}`);
                        //}
  }