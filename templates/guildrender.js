
window.onload = () => {
			const fragment = new URLSearchParams(window.location.hash.slice(1));
				let req;
				const token = fragment.get("token");
				const server = fragment.get('server')
				const user = fragment.get('user')
				let tag = fragment.get("tag");
				tag = tag.replace('#', '%23')
				const code = fragment.get("code");
				const type = fragment.get("type");

				window.location.replace(`/server?server=${server}&user=${user}&tag=${tag}&code=${code}&token=${token}&type=${type}`);
  }