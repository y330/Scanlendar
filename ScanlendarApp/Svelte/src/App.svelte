<script context="module">
	/*-------------------------*/
	const our_app = "scanlendar"
	let result = {}
	/*------------------------*/

	export const prerender = true
	// STATE
	let text = ""
	let event = {
		title: "",
		description: "",
		location: "",
		start_date: "",
		end_date: "",
		start_time: "",
		end_time: "",
	}
	// API CALLS
	async function getCalendarScan() {
		/**
		 * @function: 
		 */
		/*-------*/
		
		/*---need to send the text to the server before fetching.... someone figure out how to do this*/
		/*---------*/
		const res = await fetch("/home")
		result = Object.assign(event, res.json)

		// Get event details from text
	}
	function formatEventForGoogleCalendar() {
		// Format event to fit google calendar params
	}
	function addToGoogleCalendar() {
		// Make api call to google calendar to add event
	}
	// METHODS
	const handleTextChange = (e) => {
		text = e.target.value
		getCalendarScan(text)
	}
</script>

<style lang="scss">
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
		& h1 {
			text-transform: uppercase;
			text-align: center;
			& b {
				color: #ff8a00;
			}
		}
		& h5 b {
			font-size: 50px;
		}
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>

<svelte:head>
	<title>Scanlendar - Our newest creation</title>
</svelte:head>

<main>
	<h1>hello <b>{our_app}</b> users!</h1>
	<img src="/assets/android-chrome-512x512.png" alt="svelte_icon" />
	<p id="slogan"><em>Give us your words, and we'll give you a date(calendar)</em></p>
	<input on:change={handleTextChange} />
	<div color="cornflowerblue">{result.toString}</div>
</main>
