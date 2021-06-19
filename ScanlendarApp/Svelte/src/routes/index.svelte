<script context="module">
	export const prerender = true;
</script>

<script>
	import Counter from '$lib/Counter/index.svelte';
</script>

<svelte:head>
	<title>Home</title>
</svelte:head>

<section>
	<h1>
		<div class="welcome">
			<picture>
				<source srcset="scanlendar-transparent.webp" type="image/webp" />
				<img src="scanlendar-transparent.png" alt="Welcome" />
			</picture>
		</div>

		Smart Calendar Tool<br />built with SvelteKit and Django
	</h1>

	<h2>
		try editing <strong>src/routes/index.svelte</strong>
	</h2>

	<Counter />
</section>

<style>
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		flex: 1;
	}

	h1 {
		width: 100%;
	}

	.welcome {
		position: relative;
		width: 100%;
		height: 100%;
		padding: 0 0 calc(100% * 495 / 2048) 0;
	}

	.welcome img {
		position: relative;
		width: 100%;
		height: 100%;
		top: 0;
		display: block;
	}
</style>
