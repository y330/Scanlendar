<script>
	// your script goes here
	import { Button } from "../../node_modules/attractions";
	import Textfield from "../../node_modules/attractions"
	let eventString = "";
	let cleanString = "CLick Me"
</script>

<svelte:head>
	<script src="https://unpkg.com/attractions"></script>
</svelte:head>

<Button on:click{() => cleanString = eventString}>{cleanString}</Button>
<Textfield
	label="Input calendar event in   natural language"
	bind:value={eventString}
	error={eventString.includes("?") && "You confused our NLP model >:("}
/><h1>Welcome to SvelteKit</h1>
<a-button filled="filled">My button</a-button>

<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>

<!-- markup (zero or more items) goes here -->
<style>
	/* your styles go here */

</style>
