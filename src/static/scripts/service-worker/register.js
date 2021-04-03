const loadServiceWorker = false;

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
