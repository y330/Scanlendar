<script context="module">
  import Button, { Label, Icon } from "@smui/button";

  let clicked = 0;

  export const prerender = true;

  // STATE
  let text = "";
  let event = {
    title: "",
    description: "",
    location: "",
    start_date: "",
    end_date: "",
    start_time: "",
    end_time: "",
  };

  // API CALLS
  function getCalendarScan() {
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
    text = e.target.value;
  };
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
  <Button on:click={() => clicked++}>
    <Icon class="material-icons">thumb_up</Icon>
    <Label>Click Me</Label>
  </Button>
  <p class="mdc-typography--body1">
    {#if clicked}
      You've clicked the button {clicked} time{clicked === 1 ? "" : "s"}.
    {:else}
      <span class="grayed">You haven't clicked the button.</span>
    {/if}
  </p>

  <input on:change={handleTextChange} />
</section>
>>>>>>> 3b3cc2195f1e6c7bbc9c02c914d64251c4540775

<style>
  .grayed {
    opacity: 0.6;
  }
</style>
