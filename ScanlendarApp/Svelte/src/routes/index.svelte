<script context="module">
	export const prerender = true;
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
		height: 0px;
	}

	.welcome img {
		position: relative;
		width: 200px;
		height: 200px;

		top: 0;
		display: block;
	}
</style>
