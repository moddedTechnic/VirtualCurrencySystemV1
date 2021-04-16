;(() => {
	let loadServiceWorker = false;

	if ('currentScript' in document) {
		const currentScript = document.currentScript;
		let serviceWorker = currentScript.hasAttribute('data-service-worker');
		if (serviceWorker) {
			serviceWorker = currentScript.getAttribute('data-service-worker').toLowerCase() === 'true';
		}
		loadServiceWorker |= serviceWorker;
	} else {
		console.error('Can\'t load service worker - currentScript not in document');
		return;
	}

	if (loadServiceWorker && 'serviceWorker' in navigator) {
		window.addEventListener('load', () =>
			navigator.serviceWorker.register('/service-worker').then(
				(registration) =>
					console.log(
						`Service worker registration successful with scope ${registration.scope}`,
					),
				(err) => console.error(`Service worker registration failed: ${err}`),
			),
		);
	}
})();
